import os 
import sys
bnm=list(map(int,input().rstrip().split()))
b=int(bnm[0])
n=int(bnm[1])
m=int(bnm[2])
k=list(map(int,input().rstrip().split()))
d=list(map(int,input().rstrip().split()))
s=[]
if min(k)+min(d)>b:
	print('-1')
elif min(k)+min(d)<=b:
	for i in k:
		for j in d:
			sum=i+j
			if sum<=b:
				s.append(sum)
	print(max(s))
print("nice")
