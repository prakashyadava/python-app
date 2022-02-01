PLACEHOLDER = "[name]"

with open("name.txt") as name:
    names = name.readlines()

with open("letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,name)
        # print(new_letter)
        file_name = f"letter_for_{name}.txt"
        with open(file_name,"w") as send_file:
            send_file.write(new_letter)

# print(letter_content)