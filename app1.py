from operator import truediv
######################
print ("hi this is frist code")
print ("*" * 10)
studen_count = 1000
studen_course = "programing"
rating = 100.1
is_register = True
print (len(studen_course))
print (studen_course[0])
print (studen_course[-1])
print (studen_course[0:3])
print (studen_course[0:])
print (studen_course[:3])
print (studen_course[:])
print ("this is a cours \n \"of\" \n programing")
######################
frist = "jack"
last = "vinson"
print (frist + " " + last)
full = f"{frist} {last}"
print (full)
print (frist.upper())
print (frist.lower())
print (frist.title())
print (frist.strip())
print (frist.rstrip())
print (frist.find("p"))
print (frist.replace("p","q"))
######################
print (10 + 5)
print (10 - 5)
print (10 * 5)
print (10 / 5)
print (10 // 5)
print (10 % 5)
print (10 ** 5)
######################
import math
print (round(5.9))
print (abs(-5.9))
print (math.ceil(5.9))
######################
x = input ("x: ")
y = int (x) + 5
print (f"x {x},y : {y}")
######################
10 > 5
10 >= 5
10 < 5
10 <= 5
10 == 5
10 != 5
"orange" > "apple"
"orang" == "ORANGE"
ord ("o")
ord ("O")
######################
age = 40
if age > 30:
    print ("old ")
    print("realy old")
elif age > 40:
    print ("you are old man")
else:
    print ("your young man")
print ("but your alway young")
######################
message = "young" if age <= 25 else "old"
print(message)
######################
#logical operator -> and or not
######################
for number in range (5):
    print ("loop")
######################
for number in range (5):
    print ("loop",number)
######################
for number in range (5):
    print ("loop",number)
######################  
for number in range (1,4):
    print ("loop",number)
######################
for number in range (1,20,5):
    print ("loop",number)
######################
succesful = True
for number in range (3):
    print("attempt")
    if succesful:
        print("successful")
        break
    else:
        print("attempted faild")
######################
while_number = 100
while while_number > 0:
    print(while_number)
    while_number //=2
######################    
