import zipfile
import os
import random

# Path to HLW zip
zip_path = "hlw_1_2.zip"
extract_dir = "sample_data/images"
split_path = "sample_data/split/train_valid.txt"

# Number of images to sample
NUM_IMAGES = 10000

# Extract image paths from the ZIP
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    all_files = [f for f in zip_ref.namelist() if 
f.lower().endswith(('.jpg', '.jpeg')) and not f.startswith('__MACOSX')]
    sampled_files = random.sample(all_files, min(NUM_IMAGES, 
len(all_files)))

    # Extract selected files
    for f in sampled_files:
        zip_ref.extract(f, extract_dir)

# Save filenames to train_valid.txt (relative to `images/`)
with open(split_path, 'w') as f:
    for fpath in sampled_files:
        rel_path = os.path.relpath(fpath, start="hlw_1_2/images")
        f.write(f"{rel_path}\n")

print(f"Extracted {len(sampled_files)} images to {extract_dir}")
print(f"Wrote {split_path}")

