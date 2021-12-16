class ListIter:

    def __init__(self, nested_list):
        self.cursor = -1
        self.nested_list = nested_list
        self.inner_list = None

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        while True:
            if self.inner_list:
                yield from self.inner_list
                self.inner_list = None
            else:
                self.cursor += 1
                if self.cursor == len(self.nested_list):
                    break
                value = self.nested_list[self.cursor]
                if type(value) is list:
                    self.inner_list = ListIter(value)
                else:
                    yield value


def my_generator(target: list):
    start = 0
    end = len(target)
    while start < end:
        value = target[start]
        if type(value) is list:
            yield from my_generator(value)
        else:
            yield value
        start += 1


def main():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
        [[1, [2]], 5],
        [11, 7]
    ]
    print('Flat list in iterator:')
    for item in ListIter(nested_list):
        print(item)
    print('_' * 30)
    print('Flat list in generator:')
    for item in my_generator(nested_list):
        print(item)


if __name__ == '__main__':
    main()
