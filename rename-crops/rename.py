import os
import glob
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description='crop-renamer')
parser.add_argument('crop_folder', help='path for the images folder')
args = parser.parse_args()

# Check if argument is a folder
if not os.path.isdir(args.crop_folder):
    parser.print_help()
    sys.exit()

# Start renaming
file_filter = '*.jpg'
crop_files = glob.glob(os.path.join(args.crop_folder, file_filter))

# For each file in crop_folder
for crop_file in tqdm(crop_files):
    # Given that the crop is in the format 'sq-<class_id>-<object_id>-<filename>.jpg'
    split = os.path.basename(crop_file).split("-")

    # Rename it to the new format '<filename>.<class_id>.<object_id>.jpg'
    new_filename = "-".join(split[3:])[:-4] + "." + str(int(split[1]) - 1) + "." + split[2] + ".jpg"
    new_filename = os.path.join(args.crop_folder, new_filename)

    os.rename(crop_file, new_filename)
