# ADDITION/SUBTRACTION

#you can NOT do subtraction with strings
f = "frog"
d = "og"
#print(f-d)

g=["dog","cat", "fish"]
#can not subtract string from list
#print(g - "fish")

h = ["fish"]
#can not subtract list from list
#print(g-h)

#you CAN subtract bools, it uses their integer value
r = False
j = True
print (r-j)

# MULTIPLICATION

#if you multiply an int to a str, it repeats the str by int number of times
a = "wednesday"
b = 2
print (a*b)

#if you multiply an int and a bool, it returns the int value of the bool TIMES the int 
print(b*r)

#if you multiply an int and a list, it will store the items in the list the INT number of times
print(g*b)

#you can NOT multiply a str and another str
w = "1"
#print(w*f)

# DIVISION

#int/int returns float if they can't divide evenly
print (x/b)

#int/float returns float
print(x/1.3)

#bool/int returns float if they can't divide evenly
print(True/5)

#str/int DOES NOT WORK
#print("cat"/2)

#str/bool DOES NOT WORK
#print("cat"/False)

#list/int DOES NOT WORK
#print(g/3)

#you can NOT divide by zero in python
#print(3/0)

#/ returns a float
#// returns an int
print(2/1)
print(2//1)
#// rounds down and returns float
print(9.4//2)
#returns a float bc divisor is a float
print(9//1.5)

#rounds down and returns int bc both values are int
print(9//2)

#// by a float returns the answer without its remainder
print(9//1.3)