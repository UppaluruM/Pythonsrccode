

# Boolean
    # True
    # False
# 1 bit of memory location

is_present = True
is_active = False
is_exists = True
is_completed = False
is_leap = True
is_male = True
is_pass = False


# True - 1    10011001
# False - 0
# 0     - False
# non 0 - True

x = -10
print("Value of x : ", x)
x = bool(x)
print("Bool of val : ", x)

x = 0
print("Value of x : ", x)
x = bool(x)
print("Bool of val : ", x)

is_val = 0
is_val2 = 12

# Binary 0 - False
# Binary 1 - True
# non zero = True   -14 25 3 -567
# zero     = False   0

x = 10
print("Value of x: ", x)
x = bool(x)
print("Value of x: ", x)

res = 10-10
print("Value of x: ", res, bool(res))

# None - False
# not None - True

#  0 vs None
# Entity  : Attributes

# Employee: eid name mailid idcard address sal
# Intern  : eid name mailid idcard addres  sal - None


str1 = ''
print("Bool string  ", bool(str1))
sal = None
print("Value   ", sal, bool(sal))

str1 = 'hello'
print("Bool string  ", bool(str1))
