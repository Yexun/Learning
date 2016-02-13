L="abcde"
sum=0
# part1
for i in L:
  print(ord(i))
  sum+=ord(i)
# same as part1
S=map(ord,L)
for i in S:
	print(i)
	sum+=i
print('sum=',sum)
