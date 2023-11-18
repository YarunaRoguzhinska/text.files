with open("one.txt","r",  encoding="utf-8") as file:
    data1=file.read(1)
with open("two.txt","r",  encoding="utf-8") as file:
    data2=file.read(1)
sum= int(data1)+int(data2)
with open("tree.txt","w",  encoding="utf-8") as file:
    file.write(str(sum))