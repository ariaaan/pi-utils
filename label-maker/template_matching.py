import cv2
import numpy as np


def get_template_position(source, template):
    y_size = template.shape[0]
    x_size = template.shape[1]

    result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
    y, x = np.unravel_index(result.argmax(), result.shape)

    return x, y, x + x_size, y + y_size


def save_output(source, x1, y1, x2, y2, filename='out.jpg', box_color=(0, 255, 0), border=3):
    cv2.rectangle(source, (x1, y1), (x2, y2), color=box_color, thickness=border)
    cv2.imwrite(filename, source)


def show_output(source, x1, y1, x2, y2, box_color=(0, 255, 0), border=3):
    cv2.rectangle(source, (x1, y1), (x2, y2), color=box_color, thickness=border)
    cv2.imshow('Output image', source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
