'''
FizzBuzz Problem:

Given a number n, for each integer i in the range from 1 to n inclusive, print
one value per line as follows:
- if i is a multiple of both 4 and 5, print FizzBuzz
- If i is multiple of 4 (but not 5) print Fizz.
- If i is multiple of 5 (but not 4) print Fizz.
- If i is not a multiple of 4 or 5, print value of i
'''
#TIME COMPLEXITY: O(N)
#SPACE COMPLEXITY: O(1)
def fizz_buzz(number):
    count_four = count_five = 0

    for num in range(1, number + 1):
        count_four += 1
        count_five += 1

        res = ""
        if count_four == 4:
            res += "Fizz"
            count_four = 0
        if count_five == 5:
            res += "Buzz"
            count_five = 0

        print(res if res else num)

#Driver Code
n = 30
fizz_buzz(n)