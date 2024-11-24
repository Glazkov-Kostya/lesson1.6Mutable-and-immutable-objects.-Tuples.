# кортеж (tuple) - неизменям но может хранить внутри себя неизм. об., -
# - занемает меньше места чем список(list).
# чтобы проверить сколько занимаем места, используем команду .__sizeof__()
tuple_ = 1,2,3,4,True,'String'
list_ = [1,2,3,4,True,'String']
tuple_2 = (1,2,3,4)
tuple_3 = tuple([1,2,3,4])
print(tuple_)
print(list_)
print(tuple_2)
print(tuple_3)
print(tuple_[0])
print(tuple_.__sizeof__())
print(list_.__sizeof__())
tuple_4 = ([1,2], 0)
print(tuple_4)
tuple_4[0][0] = 2
print(tuple_4)
tuple_5 = ([1,2], 0) + (1,2)
print(tuple_5)
tuple_6 = ([1,2], 0) * 3
print(tuple_6)