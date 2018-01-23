inp= raw_input("Name of the present file to be copied ")
out=raw_input("Name of new file ")

target1 = open(inp,'r')
target2 = open(out,'a')

x=target1.read()
y=target2.write(x)

target1.close()
target2.close()