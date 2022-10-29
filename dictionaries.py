# # Dictionary  (Hash table)
#
# # TODO продумать проект для полицейской БД
#
# # 1 option
# d = {}
#
# # 2 option
#
# d = dict()
#
# # 3 option
#
# d = {
#     'key': 'value'
# }
#
# alph = {
#     1: 'A',
#     2: 'B'
# }
#
# viter = {
# +
# 'params': {
#         'weight': 180,
#         'height': 111,
#     },
#     'height': 170,
#     'weight': 80,
#     'sense_of_humor': 100,
# }
#
# # x = ['Yehor', 'Yehor']
# # print(set(x))
#
# # print(viter['params']['height'])      Nested DS
#
# # 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
# # print(dir(viter))
# #
# # height = viter.get('height')
# # print(height)
# #
# # # print(viter.items())
# #
# # print(viter.keys())     # dict_keys(['height', 'weight', 'sense_of_humor'])
# # print(list(viter.keys()))   # ['height', 'weight', 'sense_of_humor']
# #
# # print(viter.values())       # dict_values([170, 80, 100])
# # print(list(viter.values()))   # [170, 80, 100]
# int(#
# int(#
# # my_int(keys = list(viter.keys())
# # priint(nt(my_keys[0:2])
int()  #
int()  #
# monthint(s = {
#     1int(: 'Jan',
#     2int(: 'Feb',
# int(}
# printint((months)  # {1: 'Jan', 2: 'Feb'}
int()  #
# sometint(hing = months.pop(2)           # Don't do this, only in case you need it!
# printint((something)
# printint((months)
int()  #
# # int(1
# printint((months[2])int(

name = input("Input name:")
age = int(input("Input age:"))
height = int(input("Input height:"))
weight = int(input("Input weight:"))
salary = int(input("Input salary:"))
address = (input("Input address:"))
ed_list = []
a = int(input('Сколько вы хотите значений ввести ?'))
for i in range(a):
    education = input('')
    ed_list.append(education)
d = {
    "name": name,
    "age": age,
    "height": height,
    "weight": weight,
    "salary": salary,
    "address": address,
    "education": ed_list,
}
print(d)
for key in d:
    print(f"{key} = {d[key]}")
    print('\n\n\n\n')
    print(key, d[key])



