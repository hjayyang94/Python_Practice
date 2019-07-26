# message = "Hello, I'm working as intended, double checking"

# print(message)

# message = "Now I've editted the text"

# print(message)

# message = "this is a title"

# print(message.title())
# print(message.upper())
# print(message)

# print(message.lower())

# first = "Jay"
# last = "Yang"

# print(first + " " + last)
# print("Python")
# print("\tfirst")

# numb = 23

# print ("Happy " + str(numb) + "rd Bday")

#						this is a comment. They are denoted with the #-sign. You can do it with a "ctrl + /" shortcut.

#											The following codes are for lists. 

fruits = ['banana', 'strawberry', 'orange']

print(fruits)
print(fruits[0])
print(fruits[-1])  #negative numbers give things starting at the end of the list
print(fruits[-2]) 

fruits[0] = "surprise" #changing a value in a list
print(fruits)

fruits.append("pineapple") #appending an item to a list
print(fruits)

empty = [] #creating an empty list
empty.append("something")
empty.append("everything")
empty.append("nothing")
print(empty)

popped = empty.pop()  #pop() removes last item from list and returns the removed item.
popped2 = empty.pop(0) # can pop with adding index number.

print(popped)
print("popped2: " + popped2)
print(empty)

del empty[0]   	#deleting an item in a list

print(empty)

empty.insert(0, "inserting")	#insert item at given index
print(empty)

empty.append("1")
empty.append("2")
empty.append("1")
empty.remove("inserting") #remove item by value
print(empty)
empty.remove("1")         #removes FIRST item found with given value.
print(empty)

numbers = [1,2,3,4,5,6,2,3,5,4,3,1]

numbers.sort() #sorting through things alphabetical/numerically

print(numbers)

numbers.sort(reverse=True) #reverse sort
print(numbers)

numbers.reverse()
print(numbers)  #can reverse list order
print(len(numbers)) #len gives length of list

for x in numbers:	#for looping through a list. equivalent to for each loop
	print(x)

for x in range(1,5): #for loop in 1~(5-1)
	print(x)


print(min(numbers)) #minimum in the list
print(max(numbers))	#maximum in the list
print(sum(numbers)) #sum of list

squares = [values**2 for values in range(1,10)]
print(squares)

#4.3 #	for n in range(1,21):
#		print(n)

million = [num for num in range(1,1000001)]
#for mil in million:
#	print(mil)

#print(min(million))
#print(max(million))
#print(sum(million))

for n in range(1,10,2):
	print(n)

threes = [x*3 for x in range(1,11)]
print(threes)

cubes = [x**3 for x in range(1,11)]
print(cubes)


print(cubes[0:5]) #up to but not including index 5
print(cubes[:5])
print(cubes[5:])

copy = cubes[:] #without the [:], copy becomes a reference to cubes and not a copy, 
#				thus any changes to cubes would appear in copy and vise versa

cubes.append("cubes")
print(copy)

print("The first three items in the list are: ")
print(cubes[:3])
print("The three items in the middle of the list are: ")
print(cubes[int((len(cubes)/2)):(int(len(cubes)/2)+3)])


cars = ['w','bm','bmw','bmws']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

if 'toyota' not in cars:
	print("success!")

elif 'w' in cars:
	print("There is a w")
else:
	print("else")


alien_color = 'green'

if alien_color == 'green':
	print("you win! gain 5 points")
else:
	print('you gain 10 points')

simple_dict = {'color': 'green', 'points': 5}

print(simple_dict['color'])

simple_dict['new'] = 'newTaks'

print(simple_dict['new'])

#use del simple_dict['new'] to delete key-value pair

new_dict = { #create multiple keys with values during initiation
	'three' : '3',
	'one' : '1',
	'two' : '2'
	
}

for key, value in sorted(new_dict.items()):
	print("\nkey: " + key)
	print("value: " + value)


favorite_places = {
	'Jay' : "Korea",
	'Kat' : "Imperial",
	'Rob' : "Guam"

}

print("These are the favorite places for each person.")

for name, place in favorite_places.items():
	print(name + "'s favorite place to go to is " + place + ".")


#msg = input("This is an input by the user. Type something: ")   #Sublime Text does not take in inputs from user.

#print("Message received: "+ msg)

before = ['hello','tomorrow','third']
after = []

while before:  #while before is not empty
	current = before.pop()
	after.append(current)
	print(current)

print(before)
print(after)


#Functions

def first_Function():
	print('this is my first function')


def name(name='Joe'):  #setting defaults 
	print(name)

name()

def sum(x,y):
	return x+y

print(sum(1,2))

def t_shirt(size, message):
	print("Thank you for ordering a " + size +"-sized shirt.")
	print("The following message will be written on the shirt: " + message)

t_shirt("Large", "Hello, World")

def full_Name(first,last,middle=''):
	if middle:
		print((first + " " + middle + " " + last).title())
	else:
		print((first + " " + last).title())

full_Name('Hyun','Yang','Jay')
full_Name('Hyun','Yang')
