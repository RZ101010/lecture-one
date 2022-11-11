str = "axxxbyyc"
print("str: " + str)
midlle = str[2]

#new positions of chars
firstChar = str[int(len(str)/2)]
print("First char: " + firstChar)
midlleChar = str[-1]
print("Midlle char: " + midlleChar)
lastChar = str[0]
print("Last char: " + lastChar)

#replace chars
temp = list(str)
temp[0] = firstChar
str = "".join(temp)

temp[int(len(str)/2)] = midlleChar
str = "".join(temp)

temp[-1] = lastChar
str = "".join(temp)

print("str: " + str)