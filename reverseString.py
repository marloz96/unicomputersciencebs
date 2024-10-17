text = input("Enter the text you want reversed: ")

output = ""

length = len(text)

for index in range(1,length+1):
    character = text[-1*index]
    output = output + character

                     
print("original - ",text)
print("reversed - ", output)


