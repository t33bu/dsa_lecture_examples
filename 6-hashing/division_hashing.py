import random

hash_table_size = 50
hash_table = [None] * hash_table_size
#print(hash_table)

for i in range(20):
    value = random.randint(100,200)
    index = value % hash_table_size
    print('value',value,'to index ',index, end='')
    if not hash_table[index]:
        hash_table[index] = value
    else:
        print(' <- collision!', end='')
    print('')

#print(hash_table)
