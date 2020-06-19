from math import log10

valores = [31,
           96,
           4,
           6,
           2,
           61,
           93,
           40,
           5,
           8,
           2,
           61,
           93,
           87,
           53,
           53,
           17,
           25,
           69,
           29,
           19,
           31,
           11,
           49,
           72,
           96,
           85,
           17,
           22,
           91,
           86,
           35,
           34,
           61,
           25,
           5,
           55,
           6,
           94,
           73,
           56,
           20,
           16,
           21,
           48,
           88,
           97,
           9,
           36,
           22,
           21,
           27,
           91,
           51,
           79,
           78,
           32,
           99,
           21,
           4,
           4,
           7,
           14,
           30,
           72,
           96,
           36,
           50,
           8,
           32,
           89,
           26,
           96,
           53,
           91,
           3,
           7,
           2,
           19,
           1,
           49,
           81,
           83,
           43,
           74,
           48,
           16,
           10,
           19,
           70,
           44,
           51,
           14,
           62,
           67,
           65,
           18,
           72,
           28,
           32,
           63,
           51,
           8,
           35, ]


def merge(s1, s2):
    i = j = k = 0
    res = []
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            res[k] = s2[i]
            i += 1
        else:
            res[k] = s2[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(s1):
        res[k] = s1[i]
        i += 1
        k += 1

    while j < len(s2):
        res[k] = s2[j]
        j += 1


def merge_sort(s):
    if len(s) > 1:
        mid = len(s) // 2
        l = s[:mid]
        r = s[mid:]
        merge_sort(l)
        merge_sort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                s[k] = l[i]
                i = i + 1
            else:
                s[k] = r[j]
                j = j + 1
            k = k + 1

        while i < len(l):
            s[k] = l[i]
            i = i + 1
            k = k + 1

        while j < len(r):
            s[k] = r[j]
            j = j + 1
            k = k + 1


def quick_sort(v):
    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]  # arbitrario, podría ser otro

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick(arr, low, pi - 1)
            quick(arr, pi + 1, high)

    n = len(v)
    quick(v, 0, n - 1)


def heap_sort(v):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    ls = len(v)

    for k in range(ls // 2 - 1, -1, -1):
        heapify(v, ls, k)

    for k in range(ls - 1, 0, -1):
        v[k], v[0] = v[0], v[k]
        heapify(v, k, 0)


def python_native_sort(v):
    v.sort()


class CountingSorter:
    count = []
    def sort(self, v):
        m = max(v) + 1
        self.count = [0] * m
        for a in v:
            self.count[a] += 1
        i = 0
        for a in range(m):
            for c in range(self.count[a]):
                v[i] = a
                i += 1
        return v


class RadixSort:

    def __init__(self, base=10):
        self.base = base

    def get_digit(self, number, pos):
        return (number // self.base ** pos) % self.base

    def prefix_sum(self, array):
        for i in range(1, len(array)):
            array[i] = array[i] + array[i - 1]
        return array

    def radixsort(self, l):
        passes = int(log10(max(l)) + 1)
        output = [0] * len(l)

        for pos in range(passes):
            count = [0] * self.base

            for i in l:
                digit = self.get_digit(i, pos)
                count[digit] += 1

            count = self.prefix_sum(count)

            for i in reversed(l):
                digit = self.get_digit(i, pos)
                count[digit] -= 1
                new_pos = count[digit]
                l[new_pos] = i

            l = list(output)
        return output

    def __call__(self, l):
        self.radixsort(l)

def print_sorted(v, sort_function):
    sort_function(v)
    print(f"sort function: ${sort_function}")
    print(f"result: ${v}")


print_sorted(valores.copy(), python_native_sort)
print_sorted(valores.copy(), heap_sort)
print_sorted(valores.copy(), quick_sort)
print_sorted(valores.copy(), merge_sort)
counting_sorter = CountingSorter()
radix_sort = RadixSort()
print_sorted(valores.copy(), counting_sorter.sort)
print_sorted(valores.copy(), radix_sort)