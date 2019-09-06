
from struct import pack

f = open('file1', 'wb')
str1 = pack('B', 6)
f.write( str1 )
f.close()

f = open('file2', 'wb')
f.write( pack('B', 6) )
f.write( pack('B', 16) )
f.close()

f = open('file3', 'wb')
for n in range(0, 32):
  f.write( pack('B', n) )
  print(n,f)
f.close()

f = open('file4', 'wb')
for n in range(0, 128):
  f.write( pack('B', n) )
f.close()

