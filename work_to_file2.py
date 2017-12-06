way_file = input("Введите путь к файлу, пример(r'/home/vladimir/Desktop/file_1'):").strip()
you_file = open(way_file).readlines()
you_word = input("Введите слово для поска:")
num_line = []
num_for_repet = 0


for i in range(0, len(you_file)):
    if you_word in you_file[i]:
        print('В строке {0}, обнаруженно {1}, совпадений по фрагменту {2}'.format(i+1, you_file[i].count(you_word), you_word))



