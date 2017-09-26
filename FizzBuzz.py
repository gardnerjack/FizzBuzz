def FizzBuzz(n):
        print('\n'.join([('' if i%3 else 'Fizz')+('' if i%5 else 'Buzz') or str(i) for i in range(1, n)]))

n = int(input("Enter a number: "))
FizzBuzz(n)
