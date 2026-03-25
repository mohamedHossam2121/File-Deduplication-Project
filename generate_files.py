import os
import shutil

BASE_DIR = "test_files_large"
os.makedirs(BASE_DIR, exist_ok=True)

# Step 1: Create base files (originals)
base_contents = {
    "base1.txt": "Hello World",
    "base2.txt": "Algorithms\nrecursive\ngreedy\ndnc",
    "base3.txt": "Deduplication project"
}

for filename, content in base_contents.items():
    with open(os.path.join(BASE_DIR, filename), "w") as f:
        f.write(content)

# Step 2: Create duplicates of each base file
NUM_DUPLICATES = 40  # change scale here

for base_file in base_contents.keys():
    for i in range(NUM_DUPLICATES):
        src = os.path.join(BASE_DIR, base_file)
        dst = os.path.join(BASE_DIR, f"{base_file}_copy_{i}.txt")
        shutil.copy(src, dst)

print("Duplicate files generated successfully.")
