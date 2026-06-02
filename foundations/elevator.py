#converting the elevator floors
#ground floor in hotels is 0 floor and ground floor in US is 1 floor 

system = input("Enter the system you are using (EU/US): ") 
floor_input = input("Enter the floor number: ") 

if system == "EU": 
    if floor_input == "G": 
        floor = 0 
    elif floor_input == "B": 
        floor = -1 
    else: 
        floor = int(floor_input)
    print (f"US floor: {floor + 1}")
elif system == "US":
     if floor_input == "G":
         floor = 1  
     elif floor_input == "B":
         floor = 0
     else:
         floor = int(floor_input)
     if floor_input == "0":
        print("Invalid. US system has no floor 0.")
     else:
        print(f"EU floor: {floor - 1}")
else:
    print("Invalid system. Please enter either 'EU' or 'US'.")