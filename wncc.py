import math                                                           #math directory included

fr = open('timestat.txt', 'r')                                        #file opened in read mode
count = 0
a = 0
b = 0                                                                 #variables declared
c = 0                                                        
                                                                      #set of 100 data - each set contains 4 lines
while count < 100:                                                    #while loop which rus 100 times
    text1 = fr.readline()                                             #first line is blank
    text2 = fr.readline()                                             #contains time for real
    text3 = fr.readline()                                             #contains time for user
    text4 = fr.readline()                                             #contains time for sys
    
                                                                      #time extracted from the string and converted to float type
    a += float(text2[10:15])                                          #a - contains the sum of all time measured for real 
    b += float(text3[10:15])                                          #b - contains the sum of all time measured for user
    c += float(text4[6:11])                                           #c - contains the sum of all time measured for sys
    count += 1                      
fr.close()                                                            #file closed

                                                                      #average = sum/N
a = a/100                                                             #a - contains the average of real
b = b/100                                                             #b - contains the average of user
c = c/100                                                             #c - contains the average of sys

fr = open('timestat.txt', 'r')                                        #file opened in read mode
count = 0
d = 0
e = 0                                                                 #variable declared
f = 0
while count < 100:                                                    #again while loop which rus 100 times
    text1 = fr.readline()                                             #first line is blank
    text2 = fr.readline()                                             #contains time for real
    text3 = fr.readline()                                             #contains time for user
    text4 = fr.readline()                                             #contains time for sys
    
                                                                      #time extracted from the string and converted to float type
    d += pow((float(text2[10:15]) - a),2)                             #d - contains the sum of square of each real time minus average 
    e += pow((float(text3[10:15]) - b),2)                             #e - contains the sum of square of each user time minus average 
    f += pow((float(text4[6:11]) - c),2)                              #f - contains the sum of square of each sys  time minus average
    count += 1
fr.close()                                                            #file closed

                                                                      #standard deviation = sqrt(sum((Xi-avg)^2)/N)
d = math.sqrt(d/100)                                                  #d - contains the standard deviation of real
e = math.sqrt(e/100)                                                  #e - contains the standard deviation of user
f = math.sqrt(f/100)                                                  #f - contains the standard deviation of sys

fr = open('timestat.txt', 'r')                                        #file opened in read mode
count = 0
l = 0
m = 0                                                                 #variable declared
n = 0
while count < 100:                                                    #again while loop which rus 100 times
    text1 = fr.readline()                                             #first line is blank
    text2 = fr.readline()                                             #contains time for real
    text3 = fr.readline()                                             #contains time for user
    text4 = fr.readline()                                             #contains time for sys
                                                                      
                                                                      #time extracted from the string and converted to float type
    if float(text2[10:15]) < a+d and float(text2[10:15]) > a-d:       #condition on real time to be in the range
        l += 1                                                        #l - counts the number of times real is in range
    if float(text3[10:15]) < b+e and float(text3[10:15]) > b-e:       #condition on real time to be in the range
        m += 1                                                        #m - counts the number of times user is in range
    if float(text4[6:11]) < c+f and float(text4[6:11]) > c-f:         #condition on real time to be in the range
        n += 1                                                        #n - counts the number of times sys  is in range
    count += 1
fr.close()                                                            #file closed
                                                                      #printing the outcome in the desired format
print('Number of runs : 100')
print('Average Time statistics')
print('real ' + str(a) + ' user ' + str(b) + ' sys ' + str(c))
print('Standard deviation of Time statistics')
print('real ' + str(d) + ' user ' + str(e) + ' sys ' + str(f))
print('Number of runs within (average - standard deviation) to (average + standard deviation)')
print('real ' + str(l) + ' user ' + str(m) + ' sys ' + str(n))
