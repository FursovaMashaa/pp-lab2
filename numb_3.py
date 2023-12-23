import os
import csv
import shutil
from random import sample


def copy_dataset_with_random_numbers(past_name: str, new: str) -> None:
    '''
    копирует изображения из старой директории в новую директорию ,
    добавляя случайное число из диапазона от 0 до 9999 в качестве имени файла.
    '''
    absolute_path = os.path.abspath(new)
    relative_path = os.path.relpath(new)
    random_number = sample(range(0, 10000), 1988)
    counter = 0
    for name in os.listdir(past_name):
        path = os.path.join(os.path.abspath(past_name), name)
        list_img = os.listdir(path)
        for img in list_img:
            new_n = str(random_number[counter]).zfill(4)
            shutil.copy(os.path.join(path, img), os.path.join(new, F'{new_n}.jpg'))
            with open("annotation_3.csv", "a") as f:
                writer = csv.writer(f, delimiter=",", lineterminator="\r")
                writer.writerow([os.path.join(absolute_path, F'{new_n}.jpg'),
                                 os.path.join(relative_path, F'{new_n}.jpg'), name])
                counter += 1

def main() -> None:
    
    past_title = 'dataset_1'
    new_title = 'dataset_3'
    
    if not os.path.isdir(new_title):
        os.mkdir(new_title)

    copy_dataset_with_random_numbers(past_title, new_title)

if __name__ == "__main__":
    main()


'''
Написать скрипт, создающий копию датасета таким образом, 
чтобы каждый файл из сходного датасета получил случайный 
номер от 0 до 10000, и датасет представлял собой следующую 
структуру dataset/номер.jpg. Для того чтобы осталась возможность 
определить принадлежность экземпляра к классу создать файл-аннотацию.
'''