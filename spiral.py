# Project Euler Problem 28 Number spiral diagonals

# This function returns sum of the numbers on diagonals on n x n spiral
def diagonals_sum(n):
    if n % 2 == 1:
        # Formula for a number of sequences is (n-1)/2
        seq = int((n - 1) / 2) + 1  # Number of sequences including 1 in the center as a sequence
        max_range = 1 + (seq - 1) * 2  # Arithmetic sequence
        corners_squared = [x ** 2 for x in
                           range(1, max_range + 1, 2)]
        # Max_range +1 because we also need the case at max_range Now when we have the biggest number in each square
        # We have to get the sum, it's another sequence its for odd numbers
        sum = 1
        dif = -2
        for number in corners_squared[1:]:
            tem = number
            for x in range(1, 4):
                tem += number + (x * dif)
            sum += tem
            dif -= 2
    else:
        seq = int(n / 2)
        max_range = 1 + (seq - 1) * 2
        odd_one = max_range ** 2 - (seq * -2)
        corners_squared = [x ** 2 for x in range(1, max_range + 1, 2)]
        sum = 1
        dif = -2

        for number in corners_squared[1:]:
            tem = number
            for x in range(1, 4):  # it executes 3 times
                tem += number + (x * dif)
            sum += tem
            dif -= 2
        sum += odd_one

    return sum
