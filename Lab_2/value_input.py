import argparse

def value_input() -> argparse.Namespace:
    """
    Функция, которая позволяет вводить ключевое слово, путь к директории, количестзво изображений, путь к файлу для аннотации
    :return: введенные аргументы
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyw', type = str, help = 'Ключевое слово для поиска фотографий')
    parser.add_argument('-dir', '--dir_name', type = str, help = 'Путь к директории')
    parser.add_argument('-val', '--value', type = int, help = 'Количество изображений для скачивания')
    parser.add_argument('-file', '--annotation_file', type = str, help = 'Путь к файлу для аннотации')
    arg = parser.parse_args()
    return arg