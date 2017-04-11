import os
import cv2
import glob
import argparse


# Parse arguments
parser = argparse.ArgumentParser(description='extract_video_frames')

parser.add_argument('input_file', help='path of the input video file')
parser.add_argument('output_folder', help='path of the ouptut folder')

args = parser.parse_args()


# Check if arguments are folders
if not os.path.isfile(args.input_file) or not os.path.isdir(args.output_folder):
    parser.print_help()
    sys.exit()


# Main
FRAME_FORMAT = '{:06d}.jpg'

cap = cv2.VideoCapture(args.input_file)

count = 0

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imwrite(os.path.join(args.output_folder, FRAME_FORMAT.format(count)), frame)
    count += 1
