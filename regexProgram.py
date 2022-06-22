import re

# Read Text File
f = open("input.txt")
text = f.read()
f.close()

# Create Regular Expression
regularExpression = '[":"][0-9]+'
numbers = str(re.findall(regularExpression, text)).replace(":", "")
print(numbers)
