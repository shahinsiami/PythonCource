from audioop import mul


def great():
    print("function")
    print("execute")


great()
##################
def full_name(first_name,last_name): #parameter
    print(first_name + " " + last_name)


full_name("jack","robinson") #argument
##################
def welcome(name):
    print(f"hi {name}")


welcome("jack")
print(welcome("jhon"))  #retun value of welcome , defualt return none or a value
##################
def increment(number,by):
    return number + by


print(increment(2,by=1)) #use by for this argument that read beter
##################
def default_parameter (number,by=1):
    return number + by


print(default_parameter(5))
##################
def pack_number(*numbers):
    print (numbers)


pack_number(1,2,3,4,5)
#list []
#tuples {}
##################
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1,2,3,4,5))
##################
def save_user(**user):
    print(user)


save_user(id=1,name="jack",age=30)
##################
message = "a"
def global_function(name):
    global message
    message = "b"

global_function("hi")
print(message)   #bad practice
##################
def fizz_buzz(input):
    if (input % 3==0) and (input % 5 == 0):
        return "fizzbuzz"
    if input % 3 == 0:
        return  "fizz"
    if input % 5 == 0:    
        return "buzz"
    

print(fizz_buzz(15))
##################