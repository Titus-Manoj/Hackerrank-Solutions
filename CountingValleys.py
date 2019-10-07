n=int(input())
s=input()
level=0
valleys=0
for i in s:
	if i=='U':
		level+=1
		if level==0:
			valleys+=1
	else:
		level-=1
print(valleys)
		