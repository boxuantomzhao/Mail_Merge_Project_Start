#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# First read all the names in the text file
name_list = []
with open("./Input/Names/invited_names.txt",mode="r") as names_file:
    while True:
        line = names_file.readline()
        if not line:
            break

        name_list.append(line.strip())

# Open the starting letter
with open("./Input/Letters/starting_letter.txt", mode = 'r') as template_file:
    template_line = template_file.readline()
    remaining_file = template_file.read()
    # This actually read the remaining file,
    # bc the cursor has already been placed at the second line after .readline()

for name in name_list:
    new_file_name = f"./Output/ReadyToSend/letter_for_{name}.txt"
    new_line = template_line.replace("[name]",name)

    with open(new_file_name,mode="w") as current_file:
        current_file.write(f"{new_line} {remaining_file}")


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp