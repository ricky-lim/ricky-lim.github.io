import numpy as np
import argparse


def create_matrix(rows, cols, operation):
    """Create and manipulate matrices based on operation type"""
    match operation:
        case "random":
            return np.random.rand(rows, cols)
        case "identity":
            return np.eye(rows)
        case "zeros":
            return np.zeros((rows, cols))
        case "ones":
            return np.ones((rows, cols))
        case _:
            return None


def analyze_matrix(matrix):
    """Perform statistical analysis on matrix"""
    stats = {
        "Mean": np.mean(matrix),
        "Std Dev": np.std(matrix),
        "Min": np.min(matrix),
        "Max": np.max(matrix),
        "Sum": np.sum(matrix),
        "Determinant": np.linalg.det(matrix)
        if matrix.shape[0] == matrix.shape[1]
        else "N/A",
    }
    return stats


def main():
    parser = argparse.ArgumentParser(description="Matrix Operations CLI")
    parser.add_argument(
        "operation",
        choices=["random", "identity", "zeros", "ones"],
        help="Type of matrix to create",
    )
    parser.add_argument("rows", type=int, help="Number of rows")
    parser.add_argument("cols", type=int, help="Number of columns")

    args = parser.parse_args()

    matrix = create_matrix(args.rows, args.cols, args.operation)
    stats = analyze_matrix(matrix)

    print(f"\n🔢 Generated {args.operation.upper()} Matrix ({args.rows}x{args.cols}):")
    print(matrix)
    print("\n📊 Matrix Analysis:")
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
