
# Predict what double("22") will do. Then run the code and check. Did it do what you expected? Why did it return the value it did?


# double("22") returns "2222".

# "22" is a string, so * 2 repeats the string twice.


def half(value):
return value / 2

def double(value):
return value * 2

def second(value):
return value[1]

print(double(22))
print(double("hello"))
print(double("22"))

print(second(22))
print(second(0x16))
print(second("hello"))
print(second("22"))

