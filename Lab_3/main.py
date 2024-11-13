import cv2

from process_img import *


def main():
    global binary_img, img
    path_to_image, path_to_folder = arg_parser()
    try:
        img = read_file(path_to_image)
        resolution = getresolution(img)
        print(f'{resolution[0]}x{resolution[1]}')
        showimg(img, "Считанное изображение")
    except ProcessLookupError:
        print("Ошибка чтения файла")
    try:
        make_histogram(calc_histogram(img))
    except Exception:
        print("Ошибка построения гистограммы")
    try:
        binary_img = process_binary(img)
        showimg(binary_img, "Бинарное изображение")
        make_histogram(calc_histogram(binary_img))
    except Exception:
        print("Ошибка обработки изображения в бинарное")
    try:
        cv2.imwrite(path_to_folder, binary_img)
    except Exception:
        print("Ошибка записи бинарного изображения")


if __name__ == "__main__":
    main()