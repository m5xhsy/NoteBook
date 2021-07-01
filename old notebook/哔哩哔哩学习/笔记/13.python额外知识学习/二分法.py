#有序才可以用二分法
lst1=[1,5,12,19,35,69,72,100,124,256,395,624,952,1202]


#普通二分法
n=5
left=0
right=len(lst1)
while left<=right:
    dim=(left+right)//2
    if n > lst1[dim]:
        left=dim+1
    if n < lst1[dim]:
        right=dim-1
    if n == lst1[dim]:
        print('找到了')
        break




#递归二分法

# def func(n,lst,left,right):
#     if left<=right:
#         mid = (left + right) // 2
#         if n>lst[mid]:
#             left=mid+1
#             k=func(n,lst,left,right)
#         if n<lst[mid]:
#             right=mid-1
#             k=func(n, lst, left, right)
#         if n==lst[mid]:
#             print("找到了")
#             return mid
#     else:
#         print('没找到')
#         return -1
#     return k
# s=func(35,lst1,0,len(lst1)-1)
# print(s)





