#Tuples
# list1 = [1, 2, 3, 4]
# print(list1[2])
# list1[0] = 0
# print(list1)

# tuple1 = (1, 2, 3, 4, 3, 3, 3)
# print(tuple1[0])
# print(type(tuple1))
# print(tuple1.index(2))
# print(tuple1.count(3))
# a = list(tuple1)
# print(type(a))
# a.append(4)
# tuple1 = tuple(a)
# print(tuple1)
# print(len(tuple1))
#
# tuple2 = ('s', True, 3)
# tuple3 = tuple2 + tuple1
# print(tuple3)
# print(tuple3[3:7])

# for i in tuple1:
#     print(i, end=" ")
#
# for i in range(len(tuple1)):
#     print(tuple1[i])
#
# i = 0
# while i < len(tuple1):
#     print(tuple1[i])
#     i +=1

#SET
# set1 = {1, 6, 3, 9, 2, 2, 2, 2}
# # print(set1)
# list1 = [6, 22, 8, 3]
# set2 = set(list1)
# print(set2)
# print(len(set1))
#
# a = {'abc','ab', 'a', 6, True, 'ghjkl;', False, 'yuioo'}
# b = {1, 2, 3}
# a.add(5)
# a.remove('a')
# a.discard('b')
# a.update(b)
# a.pop()
# a.clear()
# print(a)

# set1 = {1, 2, 3, 8, 8,  0}
# for i in set1:
#     print(i, end=" ")

#DICTIONARIES
# list = [1, 2, 3]
# print(list[0])

# dict1 = {
#     'Almaty':7272,
#     'Astana': 7273,
#     'Kokshetau': 7162
# }
# print(dict1['Almaty'])
# dict2 = {}
# dict1['Oskemen'] = 7234
# print(dict1)

# person = {}
# s = "Ziya Kokshetau 5 4 5 3 4 5 4"
# s = s.split()
# person['name'] = s[0]
# person['city'] = s[1]
# person['marks'] = []
# for i in s[2:]:
#     person['marks'].append(int(i))
# print(person)

# students = [
#     {
#         'name':'Arman',
#         'age': 22,
#         'gpa': 3.3
#     },
#     {
#         'name':'Alice',
#         'age': 19,
#         'gpa': 2.9
#     },
#     {
#         'name':'Tore',
#         'age': 20,
#         'gpa': 3.9
#     }
# ]
# a = 0
# for i in students:
#     a += i['gpa']
#     dev = a / len(students)
#     #if i['name'][0] == "A":
#         #print(i['name'], end=" ")
#     if i['gpa'] > 3.0:
#         print(i['name'], i['gpa'])
# print(dev)


