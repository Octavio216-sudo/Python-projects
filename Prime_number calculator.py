def is_prime(num):
    prime_string = ""
    div_count = []
    prime_or_not = True
    print("divisors for ", num, ":")
    for i in range(2, num):
        if num % i == 0:
            div_count.append(i)
    if len(div_count) == 0 and num > 1:
        prime_or_not = True
        prime_string = " this number is prime"
    else:
        prime_or_not = False
        prime_string = " this number is not prime"
    print(div_count, prime_string)

set_number = int(input("Enter a number to check if it is prime or not: "))
is_prime(set_number)

