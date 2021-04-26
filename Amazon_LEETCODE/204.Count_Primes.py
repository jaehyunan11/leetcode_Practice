# Count the number of prime numbers
# less than a non-negative number, n.


# Input: n = 10
# Output: 4
# Explanation:
# There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""
    Sieve of Eratosthenes

    n = 10
         0 1 2 3 4 5 6 7 8 9 10
    a = [F,F,T,T,F,T,F,T,F,F,F]

"""
# Algorithm Sieve of Eratosthenes
# -> input : an integer n > 1
# -> output : all prime numbers from 2 through n.

# Let A be an array of Boolean values, indexed by intergers 2 to n
# initially all set to True

# for i = 2,3,4,....not exceeding squat n do
#   if A[i] is True
#       for j = i2, i2+i, i2+2i, i2+3i... not exceeding n do
#           A[j] := False
# return all i such that A[i] is true


# For 𝑛 not to be prime, it needs at least two prime factors.

#   1. Checking till sqrt(n) is enough for prime numbers i.e i*i < n
#   2. mark all as prime.
#   3. as you move along (i to i*i<n) mark every multiple until n as False.
#   4. you donot need start from i for that we can start from i*i i.e j=i*i

class Solution:
    def countPrimes(self, n):
        # Edge case (less than 2 -> no prime number)
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False
        print(is_prime)

        i = 2
        # we only check a number (i) if its square is less than n
        while i*i < n:
            if is_prime[i]:
                # 4,6,8
                # 9
                # 1,4,6,8,9 -> Composite, 2,3,5,7,
                # ex: we can mark off multiples of 5 starting at 5 × 5 = 25, because 5 × 2 = 10 was already marked off by multiple of 2, similarly 5 × 3 = 15 was already marked off by multiple of 3. Therefore, if the current number is p, we can always mark off multiples of p starting at p2, then in increments of p: p2 + p, p2 + 2p, ...
                for j in range(i*i, n, i):
                    is_prime[j] = False
            i += 1
        print(is_prime)
        return sum(is_prime)

# TIME : O(squatNlogNLogN) ## first while loop (squatN) -> each time we "cross out"the multiples of that prime because we know they aren't prime
# For 2, we have to cross out n/2, 3 -> n/3, 5 -> n/5 .... n/last prime <n this is bouded by loglog(n)
# SPACE : O(N) because we keep track the price in a array.


S = Solution()
n = 10
print(S.countPrimes(n))
