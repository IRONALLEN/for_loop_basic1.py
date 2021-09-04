
# task1 - Print all integers from 0 to 150.
for x in range (0, 151):
    print(x)

#task 2 Multiples of Five
for x in range (5, 1005, 5):
    print(x)

#task 3 Counting, the Dojo Way if divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range (1, 101, 1):
    if x % 10 == 0:
        print("Coding")
    elif x % 5 == 0:
        print("Coding Dojo")
    else:
        print(x)

#task 4 Whoa. That Sucker's Huge
x = 0
for sum in range (1, 500001, 1):
    x = x + sum
print(x)

#task 5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range (2018, 0, -4):
    print(x)

#task 6 Flexible Counter - Set three variables: lowNum, highNum, mult.
lowNum = 2
highNum = 40
mult = 4
for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)
