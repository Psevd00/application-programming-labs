import os

from icrawler.builtin import GoogleImageCrawler

def download_image(dir_name: str, keyw: str, val: int) -> None:
    """
    Функция выполняет загрузку изображения с помощью GoogleImageCrawler, создает директории (если необходимо) и очищает директории (если необходимо)
    :param dir_name: директория, в которую сохраняются изображения
    :param keyw: ключевое слово
    :param val: количество изображений для загрузки
    :return: None
    """
    if not(os.path.isdir(dir_name)):
        os.mkdir(dir_name)
    for filename in os.listdir(dir_name):
        file_path = os.path.join(dir_name, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    google_crawler = GoogleImageCrawler(
        feeder_threads = 1,
        parser_threads = 2,
        downloader_threads = 3,
        storage={'root_dir': dir_name,"backend": "FileSystem"})
    google_crawler.crawl(keyword = keyw, max_num = val)