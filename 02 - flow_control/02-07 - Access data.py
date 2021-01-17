Ali = int(97641)
Ahmed = int(15154)
Mohamed = int(121905)


ID = str(input('Who are you?? \n >>> '))
if ID == 'Ali':
    Ali_pass = int(input('Your password please : '))
    if Ali_pass == Ali:
        print('Access granted')
    else:
        print('Sorry, you are not authorized')

elif ID == 'Ahmed':
    Ahmed_pass = int(input('Your password please : '))
    if Ahmed_pass == Ahmed:
        print('Access granted')
    else:
         print('Sorry, you are not authorized')

elif ID == 'Mohamed':
    Mohamed_pass = int(input('Your password please : '))
    if Mohamed_pass == Mohamed:
        print('Access granted')
    else:
        print('Sorry, you are not authorized')

else:
    print('Sorry, you are not authorized')
