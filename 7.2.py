# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
linx = None
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if linx == None:
        linx = float(line[19:].strip())
        count = count + 1
        continue
    linx = linx + float(line[19:].strip())
    count = count +1
print("Average spam confidence:", linx / count)
