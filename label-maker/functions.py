import os
import cv2
import glob
from tqdm import tqdm
from template_matching import get_template_position


def label_images(images_folder, crop_folder, label_folder, relative=False):
    # Get a list of every .jpg file in the images_folder
    file_filter = '*.jpg'
    image_files = glob.glob(os.path.join(images_folder, file_filter))

    # For each file in the images_file slist
    for image_file in tqdm(image_files):
        image_filename = os.path.basename(image_file)

        # Find the crops corresponding to that image
        file_filter = os.path.join(crop_folder, image_filename[:-4] + '*.jpg')
        crop_files = glob.glob(file_filter)

        label_filename = os.path.join(label_folder, image_filename[:-4] + '.txt')
        label_file = open(label_filename, 'w')

        image = cv2.imread(image_file)
        height, width, _ = image.shape

        # For each crop
        for crop_file in crop_files:
            class_id = crop_file.split(".")[-3]

            # Find the crop position in the image
            crop = cv2.imread(crop_file)
            box = get_template_position(image, crop)

            if relative:
                box = convert_to_relative((width, height), box)

            x1, y1, x2, y2 = box
            string = '{} {} {} {} {}\n'.format(class_id, x1, y1, x2, y2)

            # Write the position in the label file
            label_file.write(string)


def convert_to_relative(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x1 = (box[0] + box[2])/2.0
    y1 = (box[1] + box[3])/2.0
    w1 = box[2] - box[0]
    h1 = box[3] - box[1]
    x1 *= dw
    w1 *= dw
    y1 *= dh
    h1 *= dh
    return x1, y1, w1, h1
