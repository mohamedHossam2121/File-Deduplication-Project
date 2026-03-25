import time
from utils import file_hash, get_all_files, get_valid_directory, handle_deletion

def greedy_dedup(files):
    """
    Detect duplicates using a greedy hash-based approach.
    Returns a dictionary: hash -> list of files with that hash
    """
    duplicates = {}

    for file in files:
        h = file_hash(file)
        if h not in duplicates:
            duplicates[h] = [file]
        else:
            duplicates[h].append(file)

    return duplicates


if __name__ == "__main__":
    directory = get_valid_directory()
    files = get_all_files(directory)

    start_time = time.perf_counter()
    duplicates = greedy_dedup(files)
    end_time = time.perf_counter()

    print("\nGreedy Deduplication Results:")
    found = False
    for h, file_list in duplicates.items():
        if len(file_list) > 1:
            found = True
            print("\nExact duplicates (same hash):")
            for f in file_list:
                print(f" - {f}")

    if not found:
        print("No duplicate files found.")

    print(f"\nExecution Time: {end_time - start_time:.6f} seconds")

    handle_deletion(duplicates)
