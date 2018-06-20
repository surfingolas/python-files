fun = "you,<9365>"
stuff = fun.split("<")
this = list(stuff[1])
my = this[:-1]
fun = int(''.join(my))
print(fun + 1000)
