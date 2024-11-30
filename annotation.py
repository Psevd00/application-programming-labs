import csv
import os

def annotation_creation(dir_name: str, annotation_file: str) -> None:
    """
    Функция создает аннотацию, создаёт csv-файл, записывает заголовок ('Relative path', 'Absolute path') и заносит относительный и абсолютный пути.
    :param dir_name: директория с изображениями
    :param annotation_file:csv файл аннотации
    :return: None
    """

    with open(annotation_file, mode = 'w', newline = '', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        headers = ['Relative path', ' Absolute_path']
        writer.writerow(headers)
        list_img = os.listdir(dir_name)

        for img in list_img:
            if img.endswith(("jpg", "jpeg", "png")):
                abs_path = os.path.abspath(os.path.join(dir_name, img))
                rel_path = os.path.relpath(abs_path, start = ".")
                writer.writerow([rel_path, abs_path])
            else:
                raise ValueError("This is not an image file")

