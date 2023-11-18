q= input("Введи цитату")
while q != "ні":
    with open("one.txt", "a", encoding="utf-8") as file:
        file.write("\n hgfx"+q)
        q= input("Введи цитату")

with open("one.txt", "r", encoding="utf-8") as file:
    data= file.read()
print(data)