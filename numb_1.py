import os
import csv
from typing import List


def get_absolute_path(class_img: str ) -> List[str]:
    '''
    возвращает список абсолютных путей к изображениям 
    заданного класса в указанной директории.
    '''
    abs_path = os.path.abspath("dataset_1") 
    class_path = os.path.join(abs_path, class_img) 
    image_names = os.listdir(class_path) 
    image_abs_path = [os.path.join(class_path, name) for name in image_names] 
 
    return image_abs_path


def get_relative_path(class_img: str) -> List[str]:
    '''
    возвращает список относительных путей к изображениям 
    заданного класса в указанной директории.
    '''
    rel_path = os.path.relpath("dataset_1")
    class_path = os.path.join(rel_path, class_img)
    image_names = os.listdir(class_path)
    image_rel_path = [os.path.join(class_path, name)for name in image_names]

    return image_rel_path


def main() -> str:

    cat_abs_paths = get_absolute_path('cat')
    cat_rel_paths = get_relative_path('cat')
    dog_abs_paths = get_absolute_path('dog')
    dog_rel_paths = get_relative_path('dog')

    with open('annotasion_1.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        writer.writerow(['Absolute Path', 'Relative Path', 'Class Name'])
        for abs_path, rel_path in zip(cat_abs_paths, cat_rel_paths):
            writer.writerow([abs_path, rel_path, 'cat'])
        for abs_path, rel_path in zip(dog_abs_paths, dog_rel_paths):
            writer.writerow([abs_path, rel_path, 'dog'])


if __name__ == "__main__":
    main()



'''
Написать скрипт для формирования текстового файла-аннотации собранного датасета. 
Файл-аннотация должен представлять собой csv-файл, в котором в первой колонке будет указан 
абсолютный путь к файлу, во второй колонке относительный путь относительно вашего 
Python-проекта, третья колонка будет содержать текстовое название класса (метку класса), 
к которому относится данный экземпляр.
'''