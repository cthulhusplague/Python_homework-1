Exercise #1
# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

for i in range(1000):
    if i == 5:
        break
    print(i)

​
Exercise #2
# Get first prime numbers up to 100

# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

for i in range(2, 100, 2):
    print(i)

Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

Age = input('What is your age? ')

if Age == '0-17':
    print('You are a kid.')
elif Age == '18-50':
    print('You are an adult.')
elif Age != '51-65':
    print('You are also an adult')
else:
    print('Senior')