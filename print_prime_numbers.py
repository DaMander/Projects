def print_primes(number):
    for num in range(1,number):
        if number%num == 0 and num != 1:
            break
        else:
            if num == number-1:
                print(number)
    number += 1
    print_primes(number)

print_primes(1)