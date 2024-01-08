num1 = 42 #variable declaration; data type-number
num2 = 2.3 #variable declaration; data type-number
boolean = True #data type - boolean
string = 'Hello World' #data type - string; variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #data type - list, intialize; variable declaration 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #data type - dictionary, initialize; variable declaration 
fruit = ('blueberry', 'strawberry', 'banana') #tuple, initialize; var declaration
print(type(fruit)) #type check 
print(pizza_toppings[1]) #list, access value
pizza_toppings.append('Mushrooms') #list, add value
print(person['name']) #dictionary, access value
person['name'] = 'George' #dictionary, change value
person['eye_color'] = 'blue' #dictionary, add value
print(fruit[2]) #tuple, access value

if num1 > 45: 
    print("It's greater") 
else:
    print("It's lower") #conditional if else statement

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") #else if statement

for x in range(5):
    print(x) #for loop from 0 to 5 with increment 1
for x in range(2,5):
    print(x) #for loop from 2 to 5 increment 1
for x in range(2,10,3): 
    print(x) #for loop from 2 to 10 increment 3
x = 0
while(x < 5):
    print(x)
    x += 1  #while loop start 0, end 5, increment 1

pizza_toppings.pop() #list remove from end
pizza_toppings.pop(1) #list remove from postion 1

print(person)
person.pop('eye_color')
print(person) #prints dict, removed var from dict, prints dict

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #for loop 2 if statements re a list

def print_hello_ten_times():
    for num in range(10):
        print('Hello') #function defined, for loop 0 to 10 incr 1

print_hello_ten_times() #calls above function

def print_hello_x_times(x):
    for num in range(x):
        print('Hello') #creates funciton with parameter for for loop range

print_hello_x_times(4) #calls above function with for loop range 0 to 4 inc 1

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') #same as above except range starts 0 ends 10 inc 1

print_hello_x_or_ten_times() 
print_hello_x_or_ten_times(4) #calls function with default range of 10, and calls again with new range of 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)