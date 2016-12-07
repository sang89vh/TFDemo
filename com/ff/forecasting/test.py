import math

from com.ff.forecasting.Person import Person

str = "12"
sum = int(str)
print(sum + 10)
pi = 3.14
print(pi)
print("Hello", "World")
t = (11, 22, 33, 44, 55)
for i in t:
    print(i, end=" ")
friends = {
    'tom': '111-222-333',
    'jerry': '666-33-111'
}
print(friends)
print(friends['tom'])
for key in friends:
    print(key, ":", friends[key])

del friends['tom']
print(friends)

print(friends.keys())
print(friends.values())
print(friends.get('jerry'))

print(math.pi)

print(type(friends))

print(id(friends))

test1 = True
test2 = 'a'
if test1:
    print('test1')
elif test2 == 'a':
    print('test 2')

p1 = Person('tom')  # now we have created a new person object p1
print(p1.whoami())
print(p1.name)
