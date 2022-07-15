# 1
def isEven1(value): return value % 2 == 0

def isEven2(value): return value & 1 == 0
# Я думаю, вторая реализация оптимальнее, так как менее ресурсозатратная
# С другой стороны, первая реализация понятнее для чтения

# 2
class ring_buffer1:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def get(self):
        if len(self.queue) == 0:
            return None
        else:
            res = self.queue[0]
            self.queue = self.queue[1:]
            return res

    def put(self, value):
        if len(self.queue) == self.capacity:
            self.queue = self.queue[1:]
        self.queue.append(value)

class ring_buffer2:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.head = -1
        self.tail = 0

    def inc(self, index):
        if index + 1 == len(self.queue):
            return 0
        else:
            return index + 1

    def get(self):
        if self.head == -1:
            return None
        else:
            res = self.queue[self.head]
            self.head = self.inc(self.head)
            return res

    def put(self, value):
        if self.tail == self.head:
            self.head = self.inc(self.head)
        if self.head == -1:
            self.head = self.tail
        self.queue[self.tail] = value
        self.tail = self.inc(self.tail)
# Первая реализация более понятна и легче читаема, но ресурсозатратнее

# 3
def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = 0
        while i - j > 0 and lst[i - j] < lst[i - j - 1]:
            lst[i - j], lst[i - j - 1] = lst[i - j - 1], lst[i - j]
            print(lst, i, j)
            j += 1
    return lst

def mergesort(lst):
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        return [min((lst[0], lst[1])), max(lst[0], lst[1])]
    else:
        fst = mergesort(lst[:(len(lst) // 2)])
        snd = mergesort(lst[(len(lst) // 2):])
        res = []
        i = 0
        j = 0
        while i < len(fst) and j < len(snd):
            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1
            else:
                res.append(snd[j])
                j += 1
        res += fst[i:] + snd[j:]
        return res

def timsort(lst):
    if len(lst) <= 64:
        return insertion_sort(lst)
    else:
        return mergesort(lst)
# Сортирует слиянием, так как данная сортировка имеет наиболее оптимальную сложность в лучшем, худшем и среднем случаях
# При количестве элементов до 64-ёх, использует сортировку вставками, так как на небольшом количестве элементов работает быстрее