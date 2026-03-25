import time
from utils import get_valid_directory, get_all_files
from greedy import greedy_dedup
from recursive import recursive_dedup
from divide_and_conquer import divide_and_conquer

def measure_time(func, files, runs=5):
    total = 0
    for _ in range(runs):
        start = time.perf_counter()
        func(files)
        total += time.perf_counter() - start
    return total / runs


if __name__ == "__main__":
    directory = get_valid_directory()
    files = get_all_files(directory)

    print(f"\nTotal files scanned: {len(files)}\n")

    t_greedy = measure_time(greedy_dedup, files)
    t_recursive = measure_time(recursive_dedup, files)
    t_dnc = measure_time(divide_and_conquer, files)

    print("Execution Time Comparison:")
    print(f"Greedy: {t_greedy:.6f} seconds \nRecursive: {t_recursive:.6f} seconds \nDivide&Conquer: {t_dnc:.6f} seconds")