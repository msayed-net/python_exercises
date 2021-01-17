try:
    f = open("test.txt",mode='w', encoding='utf-8')
    f.writelines('\n This is just test')
finally:
   f.close()

with open('test.txt') as fi:
    print(fi.read())