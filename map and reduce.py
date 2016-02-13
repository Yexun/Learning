# Change str to float,OMG! I nearly crazy.
def str2float(s):
	def num(x):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]
	s1,s2=s.split('.')
	def f(x,y):
		return x*10+y
	res=reduce(f,map(num,s2))
	i=len(str(res))
	while i>0:
		res/=10
		i-=1
	return reduce(f,map(num,s1))+res
print('str2float(\'123.456\') =', str2float('123.456'))
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

# Change str to float,OMG! I nearly crazy.
def str2float(s):
	def num(x):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]
	s1,s2=s.split('.')
	def f(x,y):
		return x*10+y
	res=reduce(f,map(num,s2))
	i=len(str(res))
	while i>0:
		res/=10
		i-=1
	return reduce(f,map(num,s1))+res
print('str2float(\'123.456\') =', str2float('123.456'))
