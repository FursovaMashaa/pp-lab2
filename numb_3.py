import os
import csv
import shutil
from typing import List
import random


def name_change(past_name: str, new: str, file_types: List[str]) -> None:
    absolute_path = os.path.abspath(new)
    relative_path = os.path.relpath(new)
    for file_type in file_types:
        path = os.path.join(os.path.abspath(past_name), file_type)
        list_img = os.listdir(path)
        for img in list_img:
            # Генерируем случайный номер
            random_num = random.randint(0, 10000)
            # Получаем расширение файла
            ext = os.path.splitext(img)[1]
            # Создаем новое имя файла в формате "номер.расширение"
            new_name = f"{random_num}{ext}"
            # Копируем файл с новым именем
            shutil.copy(os.path.join(path, img), os.path.join(new, new_name))
            # Записываем информацию о файле в файл-аннотацию
            with open('annotation_3.csv', 'a', newline='') as f_csv:
                writer = csv.writer(f_csv, delimiter=',')
                writer.writerow([os.path.join(absolute_path, new_name),
                                 os.path.join(relative_path, new_name), file_type])

def main() -> None:
    class_name = ['']
    past_title = 'dataset_1'
    new_title = 'dataset_3'
    if not os.path.isdir(new_title):
        os.mkdir(new_title)
    name_change(past_title, new_title, class_name)

if __name__ == "__main__":
    main()