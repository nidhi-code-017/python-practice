
with open("names.txt","w") as file:
    while True:
     name = input("Enter a name :")
     if name == "done":
         break
     
     file.write(name + "\n")
print(" \n Names from this file:")
# number = 1
with open("names.txt","r") as file:
    # for name in file:   
       for number,name in enumerate(file,start=1):  # Go through the file and give me a number along with each line, starting from 1
         print(f"{number}. {name .strip()}")  # Print the number and the name, stripping any extra whitespace
        #  number += 1

#        