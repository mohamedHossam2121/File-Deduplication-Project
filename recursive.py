import time
from utils import file_hash, get_all_files, handle_deletion, get_valid_directory

def recursive_dedup(files, index=0, duplicates=None):
    if duplicates is None:
        duplicates = {}

    if index == len(files):
        return duplicates

    current_file = files[index]
    h = file_hash(current_file)

    if h not in duplicates:
        duplicates[h] = [current_file]
    else:
        duplicates[h].append(current_file)

    return recursive_dedup(files, index + 1, duplicates)


if __name__ == "__main__":
    directory = get_valid_directory()
    files = get_all_files(directory)

    start = time.perf_counter()
    duplicates = recursive_dedup(files)
    end = time.perf_counter()

    print("\nRecursive Deduplication Results:")
    found = False
    for h, file_list in duplicates.items():
        if len(file_list) > 1:
            found = True
            print("\nExact duplicates:")
            for f in file_list:
                print(f" - {f}")

    if not found:
        print("No duplicate files found.")

    print(f"\nExecution Time: {end - start:.6f} seconds")

    handle_deletion(duplicates)
