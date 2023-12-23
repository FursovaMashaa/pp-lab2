import os
from typing import Optional


def get_instance(mark: str) -> Optional[str]:
    '''
    возвращает относительрный путь для объекта класса, переданного
    в функцию Если такого пути нет, функция возвращает None.
    '''
    path = os.path.join("dataset_1", mark)
    names = os.listdir(path)
    names.append(None)
    for i in range(len(names)):
        if names[i] is not None:
            yield os.path.join(path, names[i])
        elif names[i] is None:
            yield None
   


def main() -> None:

    class_ = 'cat'
    print(*get_instance(class_))


if __name__ == "__main__":
    main()

'''
Написать скрипт, содержащий функцию, получающую на входе 
метку класса и возвращающую следующий экземпляр (путь к нему) 
этого класса. Экземпляры идут в любом порядке, но не повторяются. 
Когда экземпляры заканчиваются, функция возвращает None.
'''