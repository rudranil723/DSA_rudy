# # Python program to print all permutations using
# # Heap's algorithm

# # Generating permutation using Heap Algorithm
# def heapPermutation(a, size):

# 	# if size becomes 1 then prints the obtained
# 	# permutation
# 	if size == 1:
# 		print(a)
# 		return

# 	for i in range(size):
# 		heapPermutation(a, size-1)

# 		# if size is odd, swap 0th i.e (first)
# 		# and (size-1)th i.e (last) element
# 		# else If size is even, swap ith
# 		# and (size-1)th i.e (last) element
# 		if size & 1:
# 			a[0], a[size-1] = a[size-1], a[0]
# 		else:
# 			a[i], a[size-1] = a[size-1], a[i]


# # Driver code
# a = [1, 2, 3]
# n = len(a)
# heapPermutation(a, n)

# # This code is contributed by ankush_953
# # This code was cleaned up to by more pythonic by glubs9

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = set()
        for i in range(2,n+1):
            if all(i%p != 0 for p in primes):
                primes.add(i)
        M = 10**9 + 7
        def fact(k):
            res = 1
            for i in range(2,k+1):
                res = (res*i)%M
            return res
        return fact(len(primes))*fact(n-len(primes))%M
