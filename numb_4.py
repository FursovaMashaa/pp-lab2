import os
from typing import Optional


def get_instance(mark: str) -> Optional[str]:
    path = os.path.join("dataset_1", mark)
    names = os.listdir(path)
    names.append(None)
    def generator():
        for i in range(len(names)):
            if names[i] is not None:
                yield os.path.join(path, names[i])
            elif names[i] is None:
                yield None
    return generator().__next__



def main() -> None:
    class_1 = 'cat'
    # class_2 = 'dog'

    get_instance_func = get_instance(class_1)
    instance = get_instance_func()
    while instance is not None:
        print(instance)
        instance = get_instance_func()

if __name__ == "__main__":
    main()
