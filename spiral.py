def solution_1(n):
    if n % 2 == 1:
        # formula for a number of sequences is (n-1)/2
        seq = int((n - 1) / 2) + 1  # number of sequences including 1 in the center as a sequence
        max_range = 1 + (seq - 1) * 2  # arythemtic sequence
        corners_squared = [x ** 2 for x in
                           range(1, max_range + 1, 2)]  # max_range +1 becauce we also need the case at max_range
        # now when we have the bigest number in each square we have to get the sum, it's another sequence its for odd
        # numbers
        sum = 1
        dif = -2
        print(corners_squared)
        for number in corners_squared[1:]:
            tem = number
            print(tem)
            for x in range(1, 4): 
                tem = tem + number + (x * dif)
                print(tem)
            sum = sum + tem
            dif = dif - 2
    else:
        seq = int(n / 2)
        max_range = 1 + (seq - 1) * 2
        odd_one = max_range ** 2 - (seq * -2)
        corners_squared = [x ** 2 for x in range(1, max_range + 1, 2)]
        sum = 1
        dif = -2
        print(corners_squared)
        for number in corners_squared[1:]:
            tem = number
            for x in range(1, 4):  # it executes 3 times
                tem = tem + number + (x * dif)
            sum = sum + tem
            dif = dif - 2
        sum = sum + odd_one
    pass

def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

def solution_2(n):
    primes = 0
    non_primes = 1
    dimension = 2
    percentage = 100

    while percentage > n:
        if dimension % 2 == 0:
            seq = int(dimension / 2)
            max_range = 1 + (seq - 1) * 2
            odd_one = (max_range + 2) ** 2 + 3 * (seq * -2)

            if isPrime(odd_one):
                primes = primes + 1

            corners_squared = [x ** 2 for x in range(1, max_range + 1, 2)]
            dif = -2

            for number in corners_squared[1:]:
                if isPrime(number):
                    primes = primes + 1
                else:
                    non_primes = non_primes + 1
                for x in range(1, 4):  
                    if isPrime(number + (x * dif)):
                        primes = primes + 1
                    else:
                        non_primes = non_primes + 1
                dif = dif - 2
        if dimension % 2 == 1:
            seq = int((dimension - 1) / 2) + 1
            max_range = 1 + (seq - 1) * 2
            corners_squared = [x ** 2 for x in range(1, max_range + 1, 2)]
            dif = -2

            for number in corners_squared[1:]:
                if isPrime(number):
                    primes = primes + 1
                else:
                    non_primes = non_primes + 1
                for x in range(1, 4): 
                    if isPrime(number + (x * dif)):
                        primes = primes + 1
                    else:
                        non_primes = non_primes + 1
                dif = dif - 2

        percentage = primes / (primes + non_primes) * 100
        dimension = dimension + 1
    pass
