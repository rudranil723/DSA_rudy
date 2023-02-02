str = input("enter :")
lower = 0
upper = 0
for i in str:
    if (i.islower()):
        lower += 1
    else:
        upper += 1
print("lower ", lower)
print("upper", upper)
