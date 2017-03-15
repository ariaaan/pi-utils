import os
import cv2
import glob
import argparse
import numpy as np


def mirror_horizontal(image_path, output_folder):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = image.copy()

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".mh.jpg")

    for row in range(height):
        new_image[row, :] = image[(height - 1) - row, :]

    cv2.imwrite(output_path, new_image)


def mirror_vertical(image_path, output_folder):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = image.copy()

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".mv.jpg")

    for col in range(width):
        new_image[:, col] = image[:, (width - 1) - col, ]

    cv2.imwrite(output_path, new_image)


def rotate_90(image_path, output_folder):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = np.rot90(image, 3)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".r90.jpg")

    cv2.imwrite(output_path, new_image)


def rotate_180(image_path, output_folder):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = np.rot90(image, 2)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".r180.jpg")

    cv2.imwrite(output_path, new_image)


def rotate_270(image_path, output_folder):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = np.rot90(image, 1)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".r270.jpg")

    cv2.imwrite(output_path, new_image)


def saturation(image_path, output_folder, saturation):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = image.copy()
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2HSV).astype("float32")

    (h, s, v) = cv2.split(new_image)
    s = s * saturation
    s = np.clip(s, 0, 255)

    new_image = cv2.merge([h, s, v])

    new_image = cv2.cvtColor(new_image.astype("uint8"), cv2.COLOR_HSV2BGR)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".sat.jpg")

    cv2.imwrite(output_path, new_image)


def saturation(image_path, output_folder, saturation):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = image.copy()
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2HSV).astype("float32")

    (h, s, v) = cv2.split(new_image)
    s = s * saturation
    s = np.clip(s, 0, 255)

    new_image = cv2.merge([h, s, v])

    new_image = cv2.cvtColor(new_image.astype("uint8"), cv2.COLOR_HSV2BGR)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".sat.jpg")

    cv2.imwrite(output_path, new_image)


def brightness(image_path, output_folder, level):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = image.copy()
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2HSV).astype("float32")

    (h, s, v) = cv2.split(new_image)
    v = v * level
    v = np.clip(v, 0, 255)

    new_image = cv2.merge([h, s, v])

    new_image = cv2.cvtColor(new_image.astype("uint8"), cv2.COLOR_HSV2BGR)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".bri.jpg")

    cv2.imwrite(output_path, new_image)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description='data-augmentator')

    parser.add_argument('input_folder', help='path for the input folder')
    parser.add_argument('output_folder', help='path for the output folder')

    args = parser.parse_args()

    # Augmentate the data in the input folder
    file_filter = '*.jpg'
    image_files = glob.glob(os.path.join(args.input_folder, file_filter))

    for image_file in image_files:
        #mirror_horizontal(image_file, args.output_folder)
        #mirror_vertical(image_file, args.output_folder)
        #rotate_90(image_file, args.output_folder)
        #rotate_180(image_file, args.output_folder)
        #rotate_270(image_file, args.output_folder)
        #saturation(image_file, args.output_folder, 0.5)
        brightness(image_file, args.output_folder, 0.5)
