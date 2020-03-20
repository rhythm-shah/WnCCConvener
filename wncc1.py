import math

fr = open('timestat.txt', 'r')
count = 0
a = 0
b = 0
c = 0
while count < 100:
    text1 = fr.readline()
    text2 = fr.readline()
    text3 = fr.readline()
    text4 = fr.readline()
    a += float(text2[10:15])
    b += float(text3[10:15])
    c += float(text4[6:11])
    count += 1
fr.close()

a = a/100
b = b/100          
c = c/100

fr = open('timestat.txt', 'r')
count = 0
d = 0
e = 0
f = 0
while count < 100:
    text1 = fr.readline()
    text2 = fr.readline()
    text3 = fr.readline()
    text4 = fr.readline()
    d += pow((float(text2[10:15]) - a),2)
    e += pow((float(text3[10:15]) - b),2)
    f += pow((float(text4[6:11]) - c),2)
    count += 1
fr.close()

d = math.sqrt(d/100)
e = math.sqrt(e/100)
f = math.sqrt(f/100)

fr = open('timestat.txt', 'r')
count = 0
l = 0
m = 0
n = 0
while count < 100:
    text1 = fr.readline()
    text2 = fr.readline()
    text3 = fr.readline()
    text4 = fr.readline()
    if float(text2[10:15]) < a+d and float(text2[10:15]) > a-d:
        l += 1
    if float(text3[10:15]) < b+e and float(text3[10:15]) > b-e:
        m += 1
    if float(text4[6:11]) < c+f and float(text4[6:11]) > c-f:
        n += 1
    count += 1
fr.close()

print('Number of runs : 100')
print('Average Time statistics')
print('real ' + str(a) + ' user ' + str(b) + ' sys ' + str(c))
print('Standard deviation of Time statistics')
print('real ' + str(d) + ' user ' + str(e) + ' sys ' + str(f))
print('Number of runs within (average - standard deviation) to (average + standard deviation)')
print('real ' + str(l) + ' user ' + str(m) + ' sys ' + str(n))
