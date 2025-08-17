#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open(r'C:\Users\91970\Desktop\100 Days of Code - The Complete Python Pro Bootcamp\Day_24_Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt') as letter:
    letter_template = letter.read()

names = open(r'C:\Users\91970\Desktop\100 Days of Code - The Complete Python Pro Bootcamp\Day_24_Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt')


names_list = list(names)
names.close()
clean_names=[]
for name in names_list:
    clean_names.append(name.replace('\n', ''))

new_letters=[]
# clean_letters=[]

for name in clean_names:
    letter_text=letter_template.replace('[name]',name)
    new_letters.append(letter_text)
    with open(f"{name}.txt",'w') as file:
        file.write(letter_text)
# for letter in new_letters:
#     clean_letters.append(letter.replace('\n',''))

