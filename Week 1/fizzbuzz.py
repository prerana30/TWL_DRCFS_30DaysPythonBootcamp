#divisible by 3, print fizz
# divisible by 5, print Buzz
# divisible by both 3 and 5 print fizzbuzz
# if divisible by none, print the number as it as

# solution:
# 1. For number input we use for loop.
# 4 conditional statement for checking divisibility.

for i in range(0,100):
    if i % 5 == 0 and i %  3 ==0:
        print('fizzbuzz')
    elif  i % 3 == 0:
      print('fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
        