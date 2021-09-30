f = open('input.txt','r')
lines = f.readlines()

count = 0
final = []
tmp = ''
for line in lines:
    a = line[:-1]
    if a != ' ':
        if count == 0:
            a = a[0].lower() + a[1:]
        tmp += a
        count += 1
    if a == ' ':
        final.append(tmp)
        tmp = ''
        count = 0

for i in final:
    print(i, end=' ')
            
