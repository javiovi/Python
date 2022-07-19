f = open('mitexto.txt', 'w')
f.write('mi primer atexto\n')
f.close()

f = open('mitexto.txt', 'r+')
f.readline()
f.write('mi segundo texto\n')
f.close()
