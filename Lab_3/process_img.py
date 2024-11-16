import argparse
import cv2
import matplotlib.pyplot as plt

from numpy import ndarray

def arg_parser() -> tuple:
    '''
    Считывание аргументов с консоли
    :return: кортеж, состоящий из пути до изображения и пути, где изображение будет сохранено
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='Path to image')
    parser.add_argument('-dir', '--directory', type=str, help='Path to directory')
    args = parser.parse_args()
    data = (args.path, args.directory)
    return data


def read_file(path: str) -> ndarray:
    '''
    Считывание изображения
    :param path: путь до изображения
    :return: изображение в ndarray
    '''
    img = cv2.imread(path)
    return img


def calc_histogram(img: ndarray) -> list:
    '''
    Расчет параметров гистограммы
    :param img: изображение преобазуемое в гистограмму
    :return: список гистограмм (rgb или бинарных)
    '''
    channels = cv2.split(img)
    if len(channels) == 3:
        histb = cv2.calcHist([img], [0], None, [256], [0, 256])
        histr = cv2.calcHist([img], [1], None, [256], [0, 256])
        histg = cv2.calcHist([img], [2], None, [256], [0, 256])
        hists = [histb, histr, histg]
        return hists
    if len(channels) == 1:
        histbin = cv2.calcHist([img], [0], None, [256], [0, 256])
        hists = [histbin]
        return hists


def make_histogram(hists: list) -> None:
    '''
    Создание гистограммы
    :param hists: список в котором хранятся гистограммы (rgb или бинарные)
    :return: None
    '''
    plt.xlabel("Тон пикселя")
    plt.ylabel("Частота")
    plt.title("Гистограмма изображения")
    if len(hists) == 3:
        plt.plot(hists[0], label='Blue channel', color='b')
        plt.plot(hists[1], label='Red channel', color='r')
        plt.plot(hists[2], label='Green channel', color='g')
    if len(hists) == 1:
        plt.plot(hists[0], label='Binary channel')
    plt.legend()
    plt.show()


def process_binary(img: ndarray) -> ndarray:
    '''
    Создание бинарного изображения
    :param img: обрабатываемое изображение
    :return: бинарное изображение
    '''
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary_img = cv2.threshold(gray_img, 128, 255, 0)
    return binary_img


def showimg(img: ndarray, name: str) -> None:
    '''
    Демонстрация изображения
    :param img: Демонстрируемое изображение
    :param name: Название заголовка
    :return: None
    '''
    cv2.imshow(name, img)
    cv2.waitKey(0)


def getresolution(img: ndarray) -> tuple:
    '''
    Получение разрешения изображения
    :return: None
    '''
    wid = img.shape[1]
    hgt = img.shape[0]
    resolution = (wid, hgt)
    return resolution
