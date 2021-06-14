# a = [1, 1.5, 'asdf', True]

# for i in range(len(a)):
#     print(a[i], end=" ")

# n = int(input())
# r = []
# for i in range(n): #print(a[0])
#     print(i, end=" ")
#     t = int(input())
#     if t % 2 == 0:
#         r.append(t) # 3 5 6 3 8
# print(r, end=" ")

# # сколько положительных цифр в списке
# n = int(input())
# a = []
# cnt = 0
# for i in range(n):
#     t = int(input())
#     a.append(t)
# for i in a:
#     if i > 0:
#         cnt+=1
# print(cnt)

#var 2
# n = int(input())
# cnt = 0
# for i in range(n):
#     t = int(input())
#     if t > 0:
#
#         cnt+=1
# print(cnt)

# пока не введется 0 будет заполняться список
# a = list()
# while True:
#     t = int(input())
#     if t != 0:
#         a.append(t)
#     else:
#         a.sort()
#         for i in a:
#             print(i, end=" ")

# task D from informatics
# n = int(input())
# a = []
# for i in range(n):
#     t = int(input())
#     a.append(t)
#
# for i in range(1, n):
#     if a[i] > a[i-1]:
#         print(a[i])

# n = input() # 1 2 3 45
# arr = n.split()
# arr2 = []
# for i in arr:
#     arr2.append(int(i))
#
# for i in range(1, len(arr2)):
#     if arr[i] > arr2[i-1]:
#         print(arr2[i])

# slova = input()
# arr = slova.split()
# for i in range(1, len(arr)):
#     if len(arr[i]) > len(arr[i-1]):
#         print(arr[i])


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a[0][1])
# for i in a:
#     for j in i:
#         print(j, end=" ")
#     print()

#task E from informatics
# n = input()
# arr = n.split(',')
# arr2 = []
#
# for i in arr:
#     arr2.append(int(i))
# for i in range(1, len(arr2)):
#     if (arr2[i] > 0 and arr2[i-1] > 0) or (arr2[i] < 0 and arr2[i-1] < 0):
#         print(arr[i-1], arr2[i])
#         break

#task F
# n = input()
# arr = n.split()
# arr2 = []
# cnt = 0
#
# for i in arr:
#     arr2.append(int(i))
# for i in range(1, len(arr2)):
#     if arr2[i-1] < arr2[i] > arr2[i+1]:
#         cnt+=1
# print(cnt)

#task G
# n = input()
# arr = n.split()
# arr2 = []
#
# for i in arr:
#     arr2.append(int(i))
#
# mx = arr2[0]
# index = 0
# for i in range(len(arr2)):
#     if arr2[i] > mx:
#         mx = arr[i]
#         index = i
# print(mx, index)

