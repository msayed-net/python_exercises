
q1 = str(input('1+1 = \n a=0 , b=1 , c=2 , d=3 \n >>> '))
q2 = str(input('10-19 = \n a=9 , b=-9 , c=10 , d=-10 \n >>> '))
q3 = str(input('12*2 = \n a=12 , b=20 , c=22 , d=24 \n >>> '))
q4 = str(input('9/3 = \n a=1 , b=2 , c=3 , d=9 \n >>> '))
q5 = str(input('50**1 = \n a=1 , b=5 , c=50 , d=51 \n >>> '))
q6 = str(input('1**3 = \n a=3 , b=-3 , c=33 , d=1 \n >>> '))
q7 = str(input('8-80 = \n a=72 , b=-72 , c=88 , d=-88 \n >>> '))
q8 = str(input('15+18 = \n a=32 , b=38 , c=35 , d=33 \n >>> '))
q9 = str(input('14/14 = \n a=14 , b=1 , c=4 , d=-14 \n >>> '))
q10 = str(input('2**4 = \n a=32 , b=16 , c=36 , d=-36 \n >>> '))

counter = int(0)

if q1 == 'c':
    counter += int(1)
else:
    pass
if q2 == 'b':
    counter += int(1)
else:
    pass
if q3 == 'd':
    counter += int(1)
else:
    pass
if q4 == 'c':
    counter += int(1)
else:
    pass
if q5 == 'c':
    counter += int(1)
else:
    pass
if q6 == 'd':
    counter += int(1)
else:
    pass
if q7 == 'b':
    counter += int(1)
else:
    pass
if q8 == 'd':
    counter += int(1)
else:
    pass
if q9 == 'b':
    counter += int(1)
else:
    pass
if q10 == 'b':
    counter += int(1)
else:
    pass

print('The result is : {0} from 10 '.format(counter))

if counter >= int(5):
    print('Congratulations')
else:
    print('نـشـوفـك فـى الـصـيـف يـاهـنـدسـة')