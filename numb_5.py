import os


class InstanceIterator:
    def __init__(self, class_label: str):
        self.class_label = class_label
        self.path = os.path.join("dataset_1", class_label)
        self.names = os.listdir(self.path)
        self.names.append(None)

    def __iter__(self):
        return self

    def __next__(self):
        if self.names:
            name = self.names.pop(0)
            if name is not None:
                return os.path.join(self.path, name)
            else:
                raise StopIteration
        else:
            raise StopIteration

def main() -> None:
    class_label = "cat"
    iterator = InstanceIterator(class_label)
    for instance, _ in zip(iterator, range(10)):
        print(instance)

if __name__ == "__main__":
    main()