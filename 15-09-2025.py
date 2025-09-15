# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)

# welcome = lambda m : 'Welcome, ' + m

# print(welcome('Sally'))
# print(welcome('Mike'))

# setTuple = ('apple', 'banana', 'cherry')
# set1 = set(setTuple)

# print(set1, type(set1))

# user = {
#     'name': 'john',
#     'age': 25,
# }

# print(user.get('age'))
# print(user, type(user))

# user = dict(name='john', age=25, languages=['python', 'java'])
# print(user, type(user['languages']))

