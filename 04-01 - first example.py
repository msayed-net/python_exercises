# open ..> read & write ..> close


f = open('test.txt', 'w')                # same directory    |   ("c:\users\folan\desktop\test.txt") ..> another dir


# 'r'	Open a file for reading. (default)
# 'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# 'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
# 'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# 't'	Open in text mode. (default)
# 'b'	Open in binary mode.
# '+'	Open a file for updating (reading and writing)


# f = open("test.txt")                          # equivalent to 'r' or 'rt'
# f = open("test.txt",'w')                      # write in text mode
# f = open("img.bmp",'r+b')                     # read and write in binary mode


# try:                                            # safe way
#    f = open("test.txt")
#    # perform file operations
# finally:
#    f.close()


# with open("test.txt",) as f:                    # another safe way to be sure flow won't stop  |  no need to close

