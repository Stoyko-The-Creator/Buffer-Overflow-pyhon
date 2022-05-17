## Used to remove bad chars from the prepared payload.


badchars = ['00','40']# enter bad chars in hex. Each entry must be a string

while  type(badchars[0])== str:# checks if front val is string
  badchars.append(int(badchars.pop(0),16))# if front val is string front val gets popped, converted to a base10 int, and then appended to the end of the list

for x in range(0,256):
  if x not in badchars:# x is in bad chars then x is not printed
   print("\\x" + "{:02x}".format(x), end='')

print("\n\nAre we the baddies?") 



