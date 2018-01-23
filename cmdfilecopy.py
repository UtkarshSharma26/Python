from sys import argv
script, inp, out = argv

target1 = open(inp,'r')
target2 = open(out,'a')

x=target1.read()
y=target2.write(x)

target1.close()
target2.close()