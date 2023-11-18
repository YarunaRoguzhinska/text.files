with open("one.txt","r",  encoding="utf-8") as file:
    data=file.read()
f=int(data)*2

with open("two.txt","w",  encoding="utf-8") as file:
    file.write(str(f))