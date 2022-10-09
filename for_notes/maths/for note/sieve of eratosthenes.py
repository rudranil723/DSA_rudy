# # Sieve of Eratosthenes is a method for finding all primes up to
# # (and possibly including) a given natural.
# # This method works well when is relatively small,
# #  allowing us to determine whether any natural
# # number less than or equal to is prime or composite.

# Given a number n, print all primes smaller than or equal to n.
# It is also given that n is a small number.
#  For instance here if n is 10, the output should be “2, 3, 5, 7”.
# If n is 20, the output should be “2, 3, 5, 7, 11, 13, 17, 19”.



n = int(input())
ar = []
for i in range(2, n+1):
    if i not in ar:
        for j in range(i*i, n+1, i):
            ar.append(j)
print(ar)
