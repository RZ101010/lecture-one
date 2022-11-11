strWithSpace = "12 34"
anotherWord = "basketball"
print("first str: " + strWithSpace)
print("second str: " + anotherWord)
index = 0
for letter in strWithSpace:
    if not letter.isspace():
        pass
    else:
        newStr = strWithSpace[:index] + " " + anotherWord + " " + strWithSpace[index:]
        print("new str: " + newStr)
    index = index + 1

