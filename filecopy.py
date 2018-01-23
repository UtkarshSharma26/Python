#copying a file in other file
target = open("hello.txt",'r')

x=target.read()

tar = open("bye.txt",'a')

y=tar.write(x)
print y
tar.close()
target.close()