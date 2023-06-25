from random import randint, choice
from datetime import datetime

a = [randint(1, 999999999) for i in range(10000)]
# a.sort()
# print(a)

# value = int(input())
value = 1234513


def quick_sort(not_sorted_list):
    if len(not_sorted_list) <= 1:
        return not_sorted_list
    else:
        q = choice(not_sorted_list)
        l_nums = [n for n in not_sorted_list if n < q]
        e_nums = [q] * not_sorted_list.count(q)
        b_nums = [n for n in not_sorted_list if n > q]
        return quick_sort(l_nums) + e_nums + quick_sort(b_nums)


def bubble_sort(not_sorted_list):
    N = len(not_sorted_list)
    i = 0
    while i < N - 1:
        j = 0
        while j < N - 1 - i:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1



def binary_search(value, sorted_list):
    left = 0
    right = len(a) - 1
    center = (left + right) // 2
    count = 1
    while a[center] != value:
        count += 1
        if value > a[center]:
            left = center + 1
        else:
            right = center - 1
        center = (left + right) // 2
        if left >= right:
            break

    if value == a[center]:
        print("ID =", center)
    else:
        print("No value")
    print('count =', count)

time_before = datetime.now()
print('до - ', time_before)
# binary_search(345, a)
# a.sort()
# quick_sort(a)
bubble_sort(a)
time_after = datetime.now()
print('после - ', time_after)
print('время выполнения -', time_after - time_before)
