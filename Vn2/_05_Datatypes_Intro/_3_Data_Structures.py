'''
Data types: Numbers : int float
            Boolean : True False
            String  : 'hello' 'madhu' "VN2"

'''
'''
String     - 1 hour
List       - 1 hour
Tuple      - 10M
Dictionary - 1 hour
Set        - 10M
'''
print("----------String--------------")
# STRING  --> Collection of characters
x = 'Hello World'   # left  to right indexing
    #012345678910
print("Value of x: ", x, id(x), type(x))

name = "Madhu"
print("Name is : ", name, type(name))

passw = '#@$#@$32424SDFDSFfdsfsdf'
print("Name is : ", passw, type(passw))

print("-----------CRUD Operations------------")
x = 10    # CREATE
print(x)  # RETRIEVE
x = 20    # UPDATE
del x     # DELETE


x = 10
y = x + 15


# CRUD
# 1. CREATE
   #    12345678910
str1 = 'Hello World'
    #   0123456789
# 2. RETRIEVE
print("Message : ", str1)
print("Message : ", str1[0])    # Indexing
print("Message : ", str1[4])    # Indexing
print("Message : ", str1[0:5])  # Slicing
print("Message : ", str1[2:7])  # Slicing



#UPDATE
str2 = str1 + ' Welcome'
print("Message : ", str1)
print("Message : ", str2)

# DELETE
del str1


# LIST
print("----------List--------------")

list1 = [13, 22, 43, 24, 55]
      #  0   1    2   3   4  Indexing will be performed while stroing values
print("List1 : ", list1)
print("List1 : ", list1[0])   # indexing
print("List1 : ", list1[2])
print("List1 : ", list1[1:3])  # slicing

print("Before update : ", list1)
# UPDATE
list1[2] = 44
print("After update : ", list1)
del list1[4]
# del list1
print("List1 : ", list1)


list1 = [1.3, 2.2, 3.6, 4.7, 5.4]
print("List1 : ", list1)
list1 = [True, False, True, False, True]
print("List1 : ", list1)
list1 = ['hello', 'world', 'madhu']
print("List1 : ", list1)
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("List1 : ", list1)
print("List1 : ", list1[1])
print("List1 : ", list1[1][2])
list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
list1 = [{'id': 100}, {'name': 'Madhu'}]
list1 = [{1, 2, 3}, {4, 5, 6}]

# print(list1[0][1])
print(list1[0]['id'])

list1 = [1.1, 3, 4.2, True, False, 0, None, 'Hello', [1, 2, 3]]
print("List1 : ", list1)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Adding lists : ", list1+list2)


print("----------Tuple--------------")
tup1 = (1, 2, 3, 4, 5)
print("Tuple1 : ", tup1)
tup1 = (1.3, 2.2, 3.6, 4.7, 5.4)
print("Tuple1 : ", tup1)
tup1 = (True, False, True, False, True)
print("Tuple1 : ", tup1)
tup1 = ('hello', 'world', 'madhu')
print("Tuple1 : ", tup1)
tup1 = (1.1, 3, 4.2, True, False, 0, None, 'Hello', [1, 2, 3])
print("Tuple1 : ", tup1)
tup1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Tuple1 : ", tup1)
print("Tuple1 : ", tup1[1])
print("Tuple1 : ", tup1[1][2])
print("Tuple1 : ", tup1[2][1])
# del tup1[1]
del tup1

print("----------Dictionary--------------")

emp_details = [100, 'Madhu Nettem', 200000, 'Bangalore', 'ORACLE', 'M']

order_details = [12345, 534324, 432, 43, 3, 'Samsung S13', 'Bangalore']

# key value pair association
emp_details = {'eid': 100,
               'name': 'Madhu Nettem',
               'sal': 200000,
               'loc': 'Bangalore',
               'office': 'ORACLE',
               'gender': 'M'
               }
# key value pair association
# dict key : # int,float,bool,string,tuple

ord_details = {'order_no': 12345,
               'ref_no': 534324,
               'price': 432,
               'tax': 43,
               'quantity': 3,
               'prod_desc': 'Samsung S13',
               'del_loc': 'Bangalore'
               }
'''
key = eid
value = 100
'eid':100 --> Item  i.e, key:value
'''
print("Dictionary :", emp_details)
print("Dictionary keys :", emp_details.keys())
print("Dictionary keys :", list(emp_details.keys()))
print("Dictionary values :", list(emp_details.values()))
print("Dictionary values :", list(emp_details.items()))  # list of tuples


print("-------------Set---------------")  # int,float,bool,string,tuple
set1 = set({})
print("Set1   : ", set1)
set1 = {1, 2, 3, 4, 5, 6, 6}
print("Set1   : ", set1)

# print("Set1 : ", set1[2]) Indexing is not allowed in set and dict
# Inside set, dict,set, list are not allowed
