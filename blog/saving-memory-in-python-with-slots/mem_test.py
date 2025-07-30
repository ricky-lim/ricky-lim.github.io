import random
import importlib
import sys
import resource
from datetime import datetime

N = 10_000_000


def random_timestamp():
    return random.randint(0, int(datetime.now().timestamp()))


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <module-to-test>")
    sys.exit(1)

module_name = sys.argv[1].replace(".py", "")
module = importlib.import_module(module_name)


mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Create a list of Measurement objects
measurements = [module.Measurement(i, random_timestamp()) for i in range(N)]

mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

mem_consumption = mem_final - mem_init

print(f"Initial RAM usage: {mem_init:_} KB")
print(f"Final RAM usage: {mem_final:_} KB")
print(f"Memory consumption: {mem_consumption:_} KB")
