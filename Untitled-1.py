import os,time
bus=[['O' for x in range(4)] for y in range(8)]
print(bus)

if bus[0][3] =="O":
     bus[0][3]="X"

for f in bus:
     print(f)