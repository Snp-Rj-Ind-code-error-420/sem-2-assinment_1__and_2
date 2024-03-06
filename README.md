
# UNIVERSITY ASSINGNMENT (credit:LUMINAR) 

- sem-2-assinment_1__and_2

> [!tip]
> yea give some star guys

- [x] only important question
- [ ] theory not available (diy from pdf)

## Q3 distance travel 
```
time=float(input("Enter the time(hour)"))
distance=float(input("Enter the Distance(kilometer)"))
speed=distance/time
print(speed) #debug purpose
if speed>40:
	print("apply brake")
else:
	print("keep going")

```
## Q4 prime number test
```
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
```
## Q5 print of 5
```
num=int(input("enter the number"))
for i in range(1,num+1):
	for ii in range(num,0,-1):
		print(ii,end=' ')
	print()
```
## Q6 sum and square
```lst=[i for i in range(1,11)]

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

```



# python assingment 2 
## Q2 ii slicing Python 
```
str_to_Slice="I LOVE PYTHON LANGUAGE"

print(len(str_to_Slice))
print(str_to_Slice[7:13])# sliced
```
## Q3 split and join
```
str_to_join_split="Hello world, how are you?"
# print(str_to_join_split.split(' ')) # debug 
splitted_list=str_to_join_split.split(' ')
print('-'.join(splitted_list))


student_info={"name":'ola','age':'12','grade':'6','city':'disney'}

print(student_info['age'])

print(student_info['city'])
student_info['city']='tokyo'
print(student_info['city'])
```
