token = open('videos.txt','r')
linestoken=token.readlines()
tokens_column_number = 1
resulttoken=[]
for x in linestoken:
    resulttoken.append(x.split('|'))
token.close()
title =[]
id = []
tag=[]

for x in resulttoken:
    title.append(x[0].strip())

for x in resulttoken:
    id.append(x[1].strip())


for x in resulttoken:
    tag.append(x[2].strip())

for vids in resulttoken:
    vids[1] = vids[1].strip()
    vids[2] = vids[2].strip()

print(resulttoken)