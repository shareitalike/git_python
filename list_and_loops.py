
cou={"India","Aus","Cuba","Ireland"}

count=0
out=[]
for cou in cou:
    # if cou[0] == 'I':
    if cou.startswith('I'):
        count = count+1
        out.append(cou)
print(count)
print(out)

