str1 = "abc"
str2 = "xyz"
str3 = str1 + " " + str2
print(str3)
new_str1 = str3[4:6] + str1[2]
#print(new_str1)
new_str2 = str3[:2] + str2[2]
#print(new_str2)
str3 = new_str1 + " " + new_str2
print(str3)
