front_foot = ['am1', 'am2', 'am3', 'john john']
all_around = ['john john', 'mb2', 'am3', 'controller']
stupid = ['john john', 'mb2', 'controller', 'am3']
fin_choice = []
final = []
top = dict()
new_final = dict()
for stuff in front_foot:
    fin_choice.append(stuff)
for stuff in all_around:
    fin_choice.append(stuff)
for stuff in stupid:
    fin_choice.append(stuff)
for stuff in fin_choice:
    top[stuff] = top.get(stuff, 0) + 1
for template,stuff in top.items():
    super = (stuff,template)
    final.append(super)
print(super)
