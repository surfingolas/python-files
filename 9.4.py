name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        fun = line.split()
        print(fun)
        super = fun[1]
        counts[super] = counts.get(super,0) + 1
bigword = None
bigcount = None
for word,count in counts.items():
    if bigword is None or bigcount < count:
        bigword = word
        bigcount = count
print(bigword, bigcount)
