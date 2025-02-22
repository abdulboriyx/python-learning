#list, tuple, set and dictionary

# list1 = ['LB', 'RB', 'RW', 'LW', 10.1, 10]
# list1[0] = 'CF'
# print(list1)

# tuple1 = ('CB', 'CDM', 'CMF', 'AMF', 10, 7)
# print(tuple1)

# set1 = set([1, 2, 3, 3, 4, 4, 5])
# print(set1)

wc_winners = set(['Messi', 'Zidane', 'Maradona', 'Henry'])
bd_winners = set(['Messi', 'Zidane', 'Ronaldinho', 'CR'])

union_winners = wc_winners | bd_winners #combine all elements from both sets
intersected_winners = wc_winners & bd_winners #return elements that are in both sets
different_winners = wc_winners - bd_winners
symmetric_winners = wc_winners ^ bd_winners


print(union_winners)
print(intersected_winners)
print(different_winners)
print(symmetric_winners)