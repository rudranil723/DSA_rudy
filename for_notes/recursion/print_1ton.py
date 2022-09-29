from pyautogui import ImageNotFoundException


def show(n):
    arr = []
    if n <= 0:
        return 0
    else:
        arr.append(n)
        show(n-1)

        def reverselist(a, start, end):
            while start < end:
                a[start], a[end] = a[end], a[start]
                start += 1
                end += 1
        reverselist(arr)

        return reverselist


n = int(input())
print(show(n))
