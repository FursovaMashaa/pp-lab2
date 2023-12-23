import os
import csv
import shutil
from typing import List


def name_change(past_name: str, new: str, file_types: List[str]) -> None:
    '''
    переименовывает файлы в указанной директории и копирует их в новую директорию.
    '''
    absolute_path = os.path.abspath(new)
    relative_path = os.path.relpath(new)
    for file_type in file_types:
        path = os.path.join(os.path.abspath(past_name), file_type)
        list_img = os.listdir(path)
        for img in list_img:
            new_name = f'{file_type}_{img}'
            shutil.copy(os.path.join(path, img), os.path.join(new, new_name))
            with open('annotation_2.csv', 'a', newline='') as f_csv:
                writer = csv.writer(f_csv, delimiter=',')
                writer.writerow([os.path.join(absolute_path, new_name),
                                 os.path.join(relative_path, new_name), file_type])


                


def main() -> None:
    class_name = ['cat', 'dog']

    past_title = 'dataset_1'
    new_title = 'dataset_2'

    if not os.path.isdir(new_title):
        os.mkdir(new_title)
        
    name_change(past_title, new_title, class_name)

if __name__ == "__main__":
    main()


'''
Написать скрипт для копирования датасета в другую директорию таким образом, 
чтобы имена файлов содержали имя класса и его порядковый номер. То есть из 
dataset/class/0000.jpg должно получиться dataset/class_0000.jpg. Для того 
чтобы осталась возможность определить принадлежность экземпляра к классу 
создать файл-аннотацию
'''
