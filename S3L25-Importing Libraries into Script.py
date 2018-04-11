import re
string = "I AM sumit"
print(string)

#For UPPERCASE Letters
new=re.sub('[A-Z]', '', string)
print(new)

#For lowecase letters
new=re.sub('[a-z]', '', string)
print(new)