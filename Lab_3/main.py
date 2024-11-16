import cv2

from process_img import *


def main():
    path_to_image, path_to_folder = arg_parser()
    try:
        img = read_file(path_to_image)
        resolution = getresolution(img)
        print(f'{resolution[0]}x{resolution[1]}')
        showimg(img, "Считанное изображение")
        make_histogram(calc_histogram(img))
        binary_img = process_binary(img)
        showimg(binary_img, "Бинарное изображение")
        make_histogram(calc_histogram(binary_img))
        cv2.imwrite(path_to_folder, binary_img)
    except Exception as exp:
        print(exp)

if __name__ == "__main__":
    main()
