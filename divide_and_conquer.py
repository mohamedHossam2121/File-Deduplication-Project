import time
from utils import file_hash, get_all_files, get_valid_directory, handle_deletion

def divide_and_conquer(files):
    if len(files) == 0:
        return {}

    if len(files) == 1:
        return {file_hash(files[0]): [files[0]]}

    mid = len(files) // 2
    left = divide_and_conquer(files[:mid])
    right = divide_and_conquer(files[mid:])

    for h, file_list in right.items():
        if h in left:
            left[h].extend(file_list)
        else:
            left[h] = file_list

    return left


if __name__ == "__main__":
    directory = get_valid_directory()
    files = get_all_files(directory)

    start = time.perf_counter()
    duplicates = divide_and_conquer(files)
    end = time.perf_counter()

    print("\nDivide & Conquer Deduplication Results:")
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
