from random import randint
ind1 = "110101010101"
ind2 = "010001001010"
pivot = randint(0,len(ind1))
ind1_n = ind1[:pivot] + ind2[pivot:len(ind1)]
ind2_n = ind2[:pivot] + ind1[pivot:len(ind1)]
print ind1,ind2
print ind1_n,ind2_n
