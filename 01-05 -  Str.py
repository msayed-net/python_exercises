# quotes count
# 'Hello'
# "Hello"
# '''Hello'''                       # Multilines

# Defining string
str1 = str('Hello, Ahmed')
str2 = str("Hello, Ali")
str3 = str('''Hello,
            Mohamed''')

print('Test 1 : {0}'.format(str1[7:12]))                                 # Ahmed
print('Test 2 : {0}'.format(str2[7:10]))                                 # Ali
print('Test 3 : {0}'.format(str3[-7:]))                                  # Mohamed
print('Test 3 : {0}'.format(str3[-7:] + str2[6:10] + str1[6:12]))        # Multi strings together

# some tricks
# print('a' in str1)                                                     # Membership test
# print('''He Said "what's there?"''')                                     # Correct Format
# print('He Said "what\'s there?"')                                        # Correct Format
# print("He Said \"what's there?\"")                                       # Correct Format

# .format() | .lower()  |  .upper() | .join()  |  .split()  |  .find()  |  .replace()

