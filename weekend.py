import random
# x = 5
# print(x)

# def values():
#     x = 3
#     print(x)

# values()
# print(x)

# x = 1
# y = 2.8
# z = 1j

# a = float(x)
# b = int(y)
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))
# print(random.randrange(1,90))

# for i in "sudharsan":
#     print(i)

# print(len("sudharsan"))
# print(len('8989'))

# print('dha' not in 'sudhArsan')

# print("su,dharsan".replace('su', ''))
# print("su,dharsan".split(','))

# price = 34
# print(f"I am a python developer with {price:.5f} years of experience.")

# txt = "Good night Sam!"
# mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
# print(txt.translate(mydict))

# canActivate = False
# if canActivate:
#     print('True')
# else:
#     print('False')

# for i in range(3 , 30 , 2):
#     print(i)

def trim(func):
    def transform():
        return func().upper()
    return transform

@trim
def myFunction():
    return 'Sudharsan'

print(myFunction())

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())