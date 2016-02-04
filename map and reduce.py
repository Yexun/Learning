def normalize(name):
    return name.title()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def res(x,y):
	return x*y
def prod(L):
	return reduce(res,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
