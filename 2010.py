spisok = []

while True:
    line_1 = input("Введите")

    if line_1 == "/s":
        break
    spisok.append(line_1)

way_file = input("Введите путь и названия для сохранения файла, пример(/home/vladimir/Desktop/file_1):").strip()
open_file = open(way_file)

for i in spisok:
    g = i[0]
    i = g.upper
    open_file.appe(i)



