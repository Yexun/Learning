# Print out Pascal's Triangle
# Used for loop,I think I need a little more time to use generator
def triangles(x):
	a=[1]
	print(a)
	for i in range(x):
		i=len(a)-1
		if i>0:
			while i>0:
				a[i]=a[i]+a[i-1]
				i-=1
			a+=[1]
			print(a)
		else:
			a+=[1]
			print(a)
triangles(int(input("input number: ")))

# This time used generator.Gosh,it's nearly drive me crazy.TOO HARD.
def triangles(x):
	a=[1]
	yield(a)
	for i in range(x):
		i=len(a)-1
		if i>0:
			while i>0:
				a[i]=a[i]+a[i-1]
				i-=1
			a+=[1]
			yield(a)
		else:
			a+=[1]
			yield(a)
# Just in Pycharm,cmd will be crash.
x=int(input("input number: "))
T=triangles(x)
n=0
for T in triangles(x):
    print(T)
    n+=1
    if n == x:
        break
# This is used in cmd
n=triangles(10)
next(n)
