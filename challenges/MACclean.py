# 01 
# Create a new file that contains only unique MAC addresses. Each MAC should be on its own line.
# Abertura e leitura do arquivo
with open("archives/macs.txt") as macfile:
    content = macfile.read().split()
    
    content = list(set(content))

# Escrever no arquivo
with open("archives/unique_macs.txt", 'w', newline='') as newfile:
    for mac in content:
        newfile.write(f"{mac}\n")
print('#' * 80)



# 02
# Create a Python script that reads a text file into a list and then converts the list into a string that has the entire file content.
with open('archives/sample_file.txt') as sample:
    content = sample.read().strip()

    content = "".join(content)
    print(content)
print('#' * 80)


# 03 
# Create a Python script that removes all empty lines including those that contain only spaces from a file.
# Leitura do arquivo e remocão de espaço em branco
# with open('archives/file.txt') as file:
#     content = file.read().split()
#     print("".join(content))

# reading the file in a list
with open('archives/file.txt') as f:
    content_list = f.readlines()

# create a new list eliminating the elements that are empty strings or contain only spaces
tmp_list = []
for line in content_list:
    if line.strip() != '':
        tmp_list.append(line)


#write to a new file
# with open('file_without_blanks.txt', 'w') as f:
#     f.write(''.join(tmp_list))
print('#' * 80)



# 04 - Create a Python function called tail that reads the last n lines of a text file. The function has two arguments: the file name and n (the number of lines to read). This is similar to the Linux `tail` command.
# 05 - Change the solution from the previous challenge so that the script that prints out the last n lines of the file refreshes the output every 3 seconds (as the file changes or updates). This is similar to the tail -f Linux command.

import time
def tail(file, numberOfLine):
    with open(f"archives/{file}") as filetxt:
        content = filetxt.readlines()
        startfrom = len(content) - numberOfLine

        last = (content[startfrom:])
        my_str = ''.join(last)
        return my_str
    
# while True:
#     result = tail('sample.txt', 3)
#     print(result)
#     time.sleep(3)
#     print("#" * 30)

    



# 06 
# Write a Python program to count the number of lines, words, and characters in a text file. This is similar to the Linux `wc` command. Create a function, if possible.

def wc(file):
    with open(file) as archive:
        content = archive.readlines()

        lines = len(content)
        
        words = 0
        for line in content:
            words += len(line.split())

        chars = 0
        for line in content:
            chars += len(list(line))

        return lines, words, chars

print(wc("archives/sample.txt"))
print('#' * 80)



# 07 
# Write a Python program that calculates the net amount of a bank account based on the transactions that are saved in a text file.
with open('archives/banking.txt', 'r') as bankfile:
    content = bankfile.readlines()
    
    total = 0
    for line in content:   
        if line[0] == 'D':
            total += int(line[2:])

        if line[0] == 'W':
            total -= int(line[2:])
    print(total)




# 08 
# Write a Python script that compares line by line two text files and displays the lines that differ.
with open('archives/sample.txt', 'r') as file:
    file1 = file.readlines()

with open('archives/sample_file.txt', 'r') as file:
    file2 = file.readlines()


i = 0
for lines1, lines2 in zip(file1, file2):
    i += 1
    if lines1[0:] != lines2[0:]:
        print(f'file1 ({i}): {lines1[0:]}, file2 ({i}): {lines2[0:]}')


# 09
# Write a Python script that reads the file in a dictionary. The words in the file will be the dictionary keys and the length of each word the corresponding values.
with open('archives/american-english.txt', 'r') as words:
    content = words.readlines()

    new_dict = dict()
    for word in content:
        new_dict[word[0:-1]] = len(word) - 1
    
    for key, value in new_dict.items():
        print(f"{key} -> {value}")
print('#' * 80)


# 10
# Consider the dictionary file from the previous challenge. Write a Python script that finds the first 100 longest words in the file.

words_list = sorted(new_dict.items(), key = lambda x: x[1], reverse=True)
print(words_list[:100])
print("#" * 80)


# 11
#Write a Python script that finds the number of occurrences of each letter of the alphabet in all the words of the dictionary. Make a distinction between lower and uppercase letters.
import string
my_dict = dict()

for alfabet in string.ascii_letters:
    my_dict[alfabet] = 0

with open('archives/american-english.txt', 'r') as words:
    for word in words:
        for char in string.ascii_letters:
            my_dict[char] += word.count(char)

print(my_dict)
print('#' * 80)



# 12
# Change the solution from the previous challenge so that the script considers all letters lowercase (it makes no distinction between lower and uppercase letters).
import string
my_dict = dict()

for alfabet in string.ascii_uppercase:
    my_dict[alfabet.lower()] = 0

with open('archives/american-english.txt', 'r') as words:
    for word in words:
        for char in string.ascii_lowercase:
            my_dict[char] += word.lower().count(char)

print(my_dict)
print('#' * 80)




# 13 Continue the previous challenge and find the 3 most frequently used letters in all English Words.
import string
my_dict = dict()

for alfabet in string.ascii_letters:
    my_dict[alfabet] = 0

with open('archives/american-english.txt', 'r') as words:
    for word in words:
        for char in string.ascii_letters:
            my_dict[char] += word.count(char)

print(sorted(my_dict.items(), key=lambda x:x[1], reverse=True))
