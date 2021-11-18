nested_list = [
    ['a', 7, None],
    ['d', False, {}],
    [2.8, 'h', 'i']
]


class ListIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.cursor = -1
    def __iter__(self):
        self.text = sum((self.my_list), [])
        return self
    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.text):
            raise StopIteration
        return self.text[self.cursor]

list_iterator = ListIterator(nested_list)
for item in list_iterator:
    print(item)
print('*****************' * 4)
def my_iterator(my_list, index=0):
    text = sum((my_list), [])
    while index < len(text):
        yield text[index]
        index += 1

for item in my_iterator(nested_list):
    print(item)