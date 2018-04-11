numbers1 = [1,2,3,4,5]

for item in numbers1:
    print(item)

numbers = ["A", "B", "C", "D"]
for item in numbers:
    print("Name is:", item)

run=True
current = 1

while run:
    if current == 10:
        run = False
    else:
        print(current)
        current +=1