for i in range(-9, 10):
    if i % 4 == 0:
        print(f"{i} is divisible by 4")
    else:
        print(f"{i} is not divisible by 4")
        
for num in range(-9, 10):
    if num > 1:  # primes are greater than 1
        for i in range(2, num):
            if (num % i) == 0:  # if the number is divisible by any number between 2 and itself
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")