# q3 distance travel 

time=float(input("Enter the time(hour)"))
distance=float(input("Enter the Distance(kilometer)"))
speed=distance/time
print(speed) #debug purpose
if speed>40:
	print("apply brake")
else:
	print("keep going")


# q4 prime number test

def check_prime(input_variable:int) ->bool:
	cnt=0
	for  i in range(1,input_variable+1):
		if input_variable%i == 0:
			cnt+=1
		else:
			continue

		if cnt>2:
			break

	if cnt==2:
		return True
	else:
		return False

for i in range(1,10001):
	
	print(f" {i}  {check_prime(i)} ",end=' ')
	if i%10==0:
		print()

# q5 print of 5

num=int(input("enter the number"))
for i in range(1,num+1):
	for ii in range(num,0,-1):
		print(ii,end=' ')
	print()

lst=[i for i in range(1,11)]

def sm(lst:list) -> float:
	sm=0
	for i in lst:

		if i%2==0:
			 sm+=i**2

	return sm




print(list(map(lambda x: x**2 if x%2==0 else x ,lst)))

# lm=lambda lst,sm=0:sm+=i**2 if i%2==0 else continue for i in lst
# print(lm(lst))
print(sm(lst))
