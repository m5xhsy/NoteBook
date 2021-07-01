import random
import time

random.seed(5)
lis = list(range(1000))


random.shuffle(lis)


#
# # @timer
#
# def bubble_sort(lis):
#     for i in range(len(lis)):
#         change = False
#         for j in range(len(lis) - i - 1):
#             if lis[j] > lis[j + 1]:
#                 lis[j], lis[j + 1] = lis[j + 1], lis[j]
#                 change = True
#         if not change:
#             break
#     return lis
#
#
# print(bubble_sort(lis))


# def timer(func):
#     def inner(*args):
#         start = time.time()
#         print("结果:",func(*args))
#         print("总用时:",time.time()-start)
#     return inner
#
#
# def _quick_sort(lis, left=0, right=len(lis) - 1):
#     if left < right:
#         mid = partition(lis, left, right)
#         lis = _quick_sort(lis, left, mid - 1)
#         lis = _quick_sort(lis, mid + 1, right)
#     return lis
#
#
# def partition(lis, left, right):
#     tmp = lis[left]
#     while left < right:
#         while left < right and lis[right] >= tmp:
#             right -= 1
#         lis[left] = lis[right]
#         while left < right and lis[left] <= tmp:
#             left += 1
#         lis[right] = lis[left]
#     lis[left] = tmp
#     return left
#
# @timer
# def quick_sort(lis):
#     return _quick_sort(lis)
#
#
# quick_sort(lis)

# import random
# import time
# random.seed(5)
# lis = list(range(1000))
# random.shuffle(lis)
#
# def build_heap(lis, low, high):
#     tmp = lis[low]
#     i = low  # 根节点
#     j = i * 2 + 1  # 右孩子
#     while j <= high:  # 防止越界
#         if j + 1 <= high and lis[j] > lis[j + 1]:  # 右孩子存在，且右孩子比左孩子小，j指向小的孩子,
#             j += 1
#         if tmp > lis[j]: # 父节点比左右孩子要大
#             lis[i] = lis[j] # 把孩子节点放到父节点上去
#             i = j  # 指定孩子节点为父节点，进行下一轮比较
#             j = i * 2 + 1
#         else:break
#     lis[i] = tmp # 比完后i节点为空,把之前父节点补上
#
# def topk(lis, k):
#     heap = lis[0:k] # 切片k个元素,建立堆
#     for i in range(k // 2 - 1, -1, -1): # 构造小根堆
#         build_heap(heap, i, k - 1)
#     for i in range(k, len(lis)):       # 哪k以后的值和小根堆最小的值比较，
#         if lis[i] > heap[0]:        # 如果这个值比根节点大就替换,剩下的都是大的值
#             heap[0] = lis[i]
#             build_heap(heap, 0, k - 1) # 替换后进行排序
#     for i in range(k - 1, -1, -1):    # 取值 ，取出来和最后位置替换，然后high指向上一个位置
#         heap[0], heap[i] = heap[i], heap[0]
#         build_heap(heap, 0, i - 1)
#     return heap
#
# print(topk(lis, 5))


# import random
#
# l1 = list(range(0, 20, 2))
# print(l1)
# l2 = list(range(1, 12, 2))
# print(l2)
# li = l1 + l2
# print(li)
# random.seed(5)
# random.shuffle(li)
# print(li)
# print("\n\n")
#
#
# def marge(li, low, mid, high):
#     i = low
#     j = mid
#     tmp = []
#     while i < mid and j < high + 1:
#         if li[i] <= li[j]:
#             tmp.append(li[i])
#             i += 1
#         else:
#             tmp.append(li[j])
#             j += 1
#     while i < mid:
#         tmp.append(li[i])
#         i += 1
#     while j < high + 1:
#
#         tmp.append(li[j])
#         j += 1
#     for item in range(low, high):
#         li[item] = tmp[item - low]
#     print("-->", li[low:high + 1])
#
#
#
#
# def marge_sort(li, low, high):
#     if low < high:
#         mid = (low + high) // 2
#
#
#         marge_sort(li, low, mid)
#         marge_sort(li, mid+1, high)
#
#         marge(li, low, mid, high)
#
#
# marge_sort(li, 0, len(li) - 1)
# print("aaa",li)



import random
l1 = list(range(1,10,2))
print(l1)
l2 = list(range(0,12,2))
print(l2)
li = l1 + l2
print(li)


def marge(li,low,mid,high):
    i = low
    j = mid + 1
    tmp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1
    li[low:high+1] = tmp
#     for item in range(low,high):
#         li[item] = tmp[item-low]

marge(li,0,len(l1)-1,len(li)-1)
print(li)
random.seed(5)
random.shuffle(li)
print(li)


def marge_sort(li,low,high):
    if low < high:
        mid = (low + high) // 2
        marge_sort(li,low,mid)
        marge_sort(li,mid+1,high)
        marge(li,low,mid,high)

marge_sort(li,0,len(li)-1)
print(li)