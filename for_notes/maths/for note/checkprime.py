# using count (c) variable
#
#
# n = int(input())
# c = 0
# if n > 1:
#     for i in range(2, int(n/2)+1):
#         if n % i == 0:
#             c += 1
#             break
#     if c > 0:
#         print('no')
#     else:
#         print('yes')
# else:
#     print('yes')


n = int(input())
if n > 1:
    for i in range(2, int(n/2)+1):
        if n % 2 == 0:
            print('no')
            break
        else:
            print('yes')
else:
    print('yes')
