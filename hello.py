print("Hello, git!")

def FizzBuzz(n):
        for i in range(1, 101):
                    print(('' if i%3 else 'Fizz')+('' if i%5 else 'Buzz') or i)

n = int(input("Enter number: "))
FizzBuzz(n)

