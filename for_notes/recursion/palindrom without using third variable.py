# this is not recursion


def isPalindrome(n):

    # Find the appropriate divisor
    # to extract the leading digit
    divisor = 1
    while (n / divisor >= 10):
        divisor *= 10

    while (n != 0):

        leading = n // divisor #taking out the first number
        trailing = n % 10 #taking out the last number

        # If first and last digit
        # not same return false
        if (leading != trailing):
            return False

        # Removing the leading and
        # trailing digit from number
        n = (n % divisor)//10

        # Reducing divisor by a factor
        # of 2 as 2 digits are dropped
        divisor = divisor/100

    return True


# Driver code
n = int(input())
if(isPalindrome(n)):
    print('Yes, it is palindrome')
else:
    print('No, not palindrome')

# This code is contributed by Danish Raza
