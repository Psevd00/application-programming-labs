from annotation import annotation_creation
from input import value_input
from dataframe import *


def main():
    try:
        args=value_input()
        annotation_creation(args.dir_name,args.annotation_file)
        df=create_dataframe(args.annotation_file)
        print("DataFrame создан:")
        print(df)
        add_image_dimensions(df)
        print("Размеры изображений добавлены:")
        print(df)
        print("Статистика изображений:")
        print(compute_image_statistics(df))
        df_nf = df
        df=filter_images_by_size(df,args.max_width,args.max_height)
        print("Изображения после фильтрации по размеру:")
        print(df)
        add_area_column(df_nf)
        print("Колонка с площадью добавлена:")
        print(df_nf)
        df_nf=sort_by_area(df_nf)
        print("DataFrame отсортирован по площади:")
        print(df_nf)
        plot_area_distribution(df_nf)
    except Exception as e:(
        print(f'Error: {e}'))


if __name__ == '__main__':
    main()
