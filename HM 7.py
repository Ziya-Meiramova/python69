# 1
# list1 = [1, 2, 3, 5, 5, 5]
# list1.append("Hi")
# list1.insert(0, True)
# print(list1)
# list1.append([9, 6, 3])
# list1.insert(3, ( 2, 'ghjkl'))
# print(list1[3])
# list1.remove("Hi")
# print(list1)
# print(list1.count(5))

#2
# list1 = [1, 2, 3, 5, 4, 3, 5]
# print(list1[0], list1[-1])
# if len(list1) == len(set(list1)):
#     print("No")
# else:
#     print("Yes")

# dict1 = {
#     'one': 1,
#     'two': 2
# }
# dict1['three'] = 3
# dict1[(3, 4, 5)] = [3, 5, 7]
# print(dict1[(3, 4, 5)])
# del dict1['two']
# print(dict1)
# print(dict1.keys())
# print(dict1.values())


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
# for i in students:
#     if i['age'] > 21:
#         print(i['name'])

#USERS
users =[{
    'login':'qwerty',
    'password': 'asdf',
    'name': 'Bolat'
},
    {
    'login':'qw',
    'password': '',
    'name': 'Bolat'
},
    {
    'login':'',
    'password': 'fghjk',
    'name': ''
    }
]
for i in users:
    if i['name'] == '' or i['login'] == '' or i['password'] == '':

        users.remove(i)
        continue
    # for j in i.values():
    #     if j == '':
    #         users.remove(i)
    #         break
    #     else:
    #         continue
print(users)






