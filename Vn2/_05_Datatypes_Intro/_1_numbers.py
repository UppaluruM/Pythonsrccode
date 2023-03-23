# 1. Numbers:
    # int
    # float
    # complex

x = 10  # int
print("Value of x : ", x)


# Convert from float to int
x = 10.4  # float
print("Value of x: ", x)
x = int(x)
print("Value of x: ", x)


# Convert from int to float
x = 10
x = float(x)
print("Value of x : ", x)


'''
Functions: f(x)
-----------------
print() : To print the content
type()  : To get type of variable or value
id()    : To get address of value in integer format 
input() : To receive data dynamically 
-----------
int()   : converts other format to integer
float() : converts other format to float 
complex() : Ignore it 
bool()  : converts other format to boolean

'''

x = 10
print("Value of x  ", x)
print("Type of x : ", type(x))
print("ID of x   : ", id(x))
x = float(x)
print("Float of x : ", x)
x = int(x)
print("Int of x : ", x)
