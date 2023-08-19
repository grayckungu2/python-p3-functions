def greet(firstname, lastname):
    print(f"Hi {firstname}{lastname}")
    print("Welcome aboard")
    
 #arguments   
greet("moshi", "kui")
greet("levi", "kiptoo")

#type of functions 
#functions perform task
#calculate and return value
def increment(number,by):
    return number + by


#defualt value
print(increment(2,5))

#use keyword argument
#print(increment(2,by=1))
#print(increment(2,1))
#result = increment(2,1)
#print(result)
#def mutiply(*numbers):
   # for number in numbers:
     #   print (number)


#mutiply(2,3,4,5)
#defualt arguments 
#optional parameters
def multiply(*numbers):
    total=1 
    for number in numbers:
        total*=number
    return total


print (multiply(2,3,4,5))
#number of arguments
#*arg,wait and what
def saveuser(**user):
    print(user["age"])

saveuser(id=1,name="john",age=22)  
#this is how dictonarries work

#scope this refer to the region of the code where the variable is defined
def greet():
    message="a"


def greet(name):
    global message
    message="b"
greet("mosh")   
print(message)

print(message)

#fizz-buzz
def fizzbuzz(input):
    if input/3==0:
        return"fizz"
    if input /5 ==0:
        return "buzz"
    if(input/3==0) and(input/5==0):
        return "fizzbuzz"
    return input


print(fizzbuzz(15))


change_the_world = "change yourself"

def change_yourself():
    global change_the_world
    change_the_world = "world changed"



print(change_the_world)
 