
am1 = []
am1_dims = 0.0
am2 = []
am2_dims = 30.01
while am1_dims <= 30.01:
    am1.append(round(am1_dims, 2))
    am1_dims = am1_dims + 0.01

while (am2_dims >= 30.01) and (am2_dims <= 82.73):
    am2.append(round(am2_dims, 2))
    am2_dims = am2_dims + 0.01

while True:
    try:
        which_fin = float(input("enter your volume_"))
    except ValueError:
        break
    print(which_fin)
    if which_fin in am1:
        print("am1")
    elif which_fin in am2:
        print("am2")
    else:
        print("no matching fins")
