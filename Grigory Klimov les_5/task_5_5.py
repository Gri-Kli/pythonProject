# Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
# Сначала написал логику без применения множеств. Потом подумал, что раз в уроке проходили множества, то
# нужно их использовать и написал используя множество.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# unique_list = []
# not_uniq_list = []
# while len(src) != 0:
#     y = src.pop()
#     if y in src or y in not_uniq_list:
#         not_uniq_list.append(y)
#     else:
#         unique_list.append(y)
#
# unique_list.reverse()
#
# print(unique_list)


unique_list = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_list.add(el)
    else:
        unique_list.discard(el)
    tmp.add(el)
print(list(unique_list))
unique_list_ord = [el for el in src if el in unique_list]
print(unique_list_ord)
