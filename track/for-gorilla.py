import sys

lines = []
for l in sys.stdin.readlines():
    lines.append(l.rstrip('\r\n'))
    
print(lines)