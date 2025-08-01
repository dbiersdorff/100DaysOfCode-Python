#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

with open("Day24/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = (names_file.readlines())

print(names)

letter = ""
with open("Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for i in range(0, len(names)):
    names[i] = names[i].strip()


for name in names:
    new_letter = letter.replace("[name]", name)
    new_file = open(f"Day24/Mail Merge Project Start/Output/letter_for_{name}", "w")
    new_file.write(new_letter)