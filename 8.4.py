fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for stuff in words:
        if stuff not in lst:
            lst.append(stuff)
        else:
            continue
lst.sort()
print(lst)
