import hashlib
import os



def get_valid_directory():
    """
    Prompt user for a directory path and validate it.
    """
    directory = input("Enter directory path to scan: ").strip()

    if not os.path.exists(directory):
        raise ValueError("Path does not exist.")

    if not os.path.isdir(directory):
        raise ValueError("Path is not a directory.")

    return directory


def file_hash(filepath):
    """Compute SHA-256 hash of a file"""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

def get_all_files(directory):
    """Recursively collect all file paths"""
    files = []
    for root, _, filenames in os.walk(directory):
        for name in filenames:
            files.append(os.path.join(root, name))
    return files

def get_file_time(filepath):
    """Return file modification time"""
    return os.path.getmtime(filepath)

def handle_deletion(duplicates):
    """
    Safe deletion logic shared by all algorithms
    """
    choice = input("\nDo you want to delete duplicate files? (yes/no): ").lower()
    if choice != "yes":
        print("Deletion cancelled.")
        return

    policy = input("Keep which file? (oldest/newest): ").lower()
    if policy not in ["oldest", "newest"]:
        print("Invalid option. Deletion cancelled.")
        return

    print("\nDeletion log:")
    for file_list in duplicates.values():
        if len(file_list) > 1:
            file_list.sort(key=get_file_time)
            if policy == "newest":
                file_list.reverse()

            original = file_list[0]
            for duplicate in file_list[1:]:
                try:
                    os.remove(duplicate)
                    print(f"Deleted: {duplicate} (kept {original})")
                except Exception as e:
                    print(f"Error deleting {duplicate}: {e}")
