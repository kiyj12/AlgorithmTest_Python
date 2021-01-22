import re

sentence = input()


for i in range(len(sentence)):
    int_str = re.findall("\d", sentence)

    str_str = re.findall("[A-Z]", sentence)

str_str = sorted(str_str)       # sorted() 는 list를 반환한다.
s = ""
d = 0
for i in range(len(str_str)):
    s = s + str(str_str[i])
    
for j in range(len(int_str)):
    d += int(int_str[j])


result = s + str(d)

print(result)