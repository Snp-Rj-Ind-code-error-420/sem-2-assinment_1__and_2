# python 
# Q2 ii slysing Python 

str_to_Slice="I LOVE PYTHON LANGUAGE"

print(len(str_to_Slice))
print(str_to_Slice[7:13])# sliced

# Q3 split and join

str_to_join_split="Hello world, how are you?"
# print(str_to_join_split.split(' ')) # debug 
splitted_list=str_to_join_split.split(' ')
print('-'.join(splitted_list))


student_info={"name":'ola','age':'12','grade':'6','city':'disney'}

print(student_info['age'])

print(student_info['city'])
student_info['city']='tokyo'
print(student_info['city'])