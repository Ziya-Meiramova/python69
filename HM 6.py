# task 1
# i = list(input().split())
# mn = 10001
# for k in range(len(i)):
#     s = int(i[k])
#     if s<mn and s > 0:
#         mn = s
# print(mn)

#task 2
# n = input()
# arr = n.split()
# arr2 = []
# for i in arr:
#     arr2.append(int(i))
# for i in reversed(arr2):
#     print(i, end=" ")
# task 3
# i = list(input().split())
# cnt = 0
# for k in range(len(i)):
#     s = int(i[k])
#     if s < 0:
#         cnt+=1
# print(cnt)

#task 4
# n = input()
# arr = n.split()
# arr2 = []
# for i in arr:
#     arr2.append(int(i))
# for i in range(1, len(arr2), 2):
#     arr2[i-1], arr2[i] = arr2[i], arr2[i-1]
#     print(arr2[i])
# for i in arr2:
#     print(i, end=" ")

#task 5
n = input()
arr = n.split()
arr2 = []
for i in arr:
    arr2.append(int(i))
mx = arr2[0]
mn = arr2[0]
index_mx = 0
index_mn = 0

for i in range(len(arr2)):
    if arr2[i] > mx:
        mx = arr2[i]
        index_mx = i
    elif arr2[i] < mn:
        mn = arr2[i]
        index_mn = i
arr2[index_mx] = mn
arr2[index_mn] = mx
for i in arr2:
    print(i, end=" ")













