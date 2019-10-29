import sys

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}!'.format(who_to_greet)
    return greeting


name = input('What is your name?\n')
print(greet('World'))
print(greet(name))
