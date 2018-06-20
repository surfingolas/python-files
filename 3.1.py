hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Enter rate:')
r = float(rate)
if h <= 40:
    print(h * r)
else:
    print((40 * r) + ((r * 1.5) *(h - 40)))
