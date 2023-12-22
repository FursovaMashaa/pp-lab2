import os
import csv
from typing import List


def get_absolute_path(class_img: str ) -> List[str]:
    
    abs_path = os.path.abspath("dataset_1") 
    class_path = os.path.join(abs_path, class_img) 
    image_names = os.listdir(class_path) 
    image_abs_path = [os.path.join(class_path, name) for name in image_names] 
 
    return image_abs_path


def main() -> str:

    cat_abs_paths = get_absolute_path('cat')
    dog_abs_paths = get_absolute_path('dog')
    

    with open('annotasion_1.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        writer.writerow(['Absolute Path', 'Class Name'])
        for abs_path  in zip(cat_abs_paths):
            writer.writerow([abs_path, 'cat'])
        for abs_path in zip(dog_abs_paths,):
            writer.writerow([abs_path, 'dog'])


if __name__ == "__main__":
    main()