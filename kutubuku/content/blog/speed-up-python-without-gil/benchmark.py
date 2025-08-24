#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# ///

"""Simple Python GIL vs No-GIL Benchmark"""

import subprocess
import re

SCRIPT_NAME = "is_prime.py"
RUNS = 3


def run_test(python_version):
    cmd = ["gtime", "-v", "uv", "run", "-p", python_version, SCRIPT_NAME]
    result = subprocess.run(cmd, capture_output=True, text=True)
    out = result.stderr

    # Wall time: “Elapsed ... time ... : 0:00.26”
    m = re.search(r"Elapsed.*?:\s*(\d+):(\d+)\.(\d+)", out)
    if m:
        min_, sec, cs = map(int, m.groups())
        wall = min_ * 60 + sec + cs / 100
    else:
        raise ValueError("Could not parse wall time")

    # CPU: “Percent of CPU this job got: 93%”
    cpu = int(re.search(r"Percent of CPU this job got:\s*(\d+)%", out).group(1))

    # Memory: “Maximum resident set size (kbytes): 19008”
    kb = int(re.search(r"Maximum resident set size.*?:\s*(\d+)", out).group(1))
    mem = kb / 1024

    return wall, cpu, mem


def run_benchmark(ver, label):
    print(f"Testing {label}...")
    walls, cpus, mems = [], [], []
    for i in range(RUNS):
        w, c, m = run_test(ver)
        walls.append(w)
        cpus.append(c)
        mems.append(m)
        print(f"  Run {i+1}: {w:.2f}s, {c:3d}%, {m:5.1f}MB")
    return sum(walls) / RUNS, sum(cpus) / RUNS, sum(mems) / RUNS


def main():
    gil = run_benchmark("3.14", "Python 3.14 (GIL)")
    nogil = run_benchmark("3.14t", "Python 3.14t (No GIL)")

    speedup = gil[0] / nogil[0]
    cpu_gain = nogil[1] / gil[1]
    mem_gain = nogil[2] / gil[2]

    headers = ["Metric", "Python 3.14 (GIL)", "Python 3.14t (No GIL)", "Improvement"]
    rows = [
        [
            "**Wall Time**",
            f"{gil[0]:5.2f} s",
            f"{nogil[0]:6.2f} s",
            f"**{speedup:.2f}× faster**",
        ],
        [
            "**CPU Usage**",
            f"{gil[1]:6.0f} %",
            f"{nogil[1]:6.0f} %",
            f"**{cpu_gain:.1f}× cores**",
        ],
        [
            "**Memory Usage**",
            f"{gil[2]:6.1f} MB",
            f"{nogil[2]:6.1f} MB",
            f"**{mem_gain:.2f}× overhead**",
        ],
    ]

    # Compute column widths using headers and all rows
    cols = list(zip(*([headers] + rows)))
    widths = [max(len(cell) for cell in col) for col in cols]

    # Build format strings
    sep = "|" + "|".join("-" * (w + 2) for w in widths) + "|"
    fmt = "|" + "|".join(" {:<" + str(w) + "} " for w in widths) + "|"

    # Print table
    print(fmt.format(*headers))
    print(sep)
    for row in rows:
        print(fmt.format(*row))


if __name__ == "__main__":
    main()
