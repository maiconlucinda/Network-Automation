# 01
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
# Leitura e concatenação
with open('archives/sample_file.txt') as sample:
    content = sample.read().strip()

    content = "".join(content)
    print(content)
print('#' * 80)


# 03
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



# 04
def tail(file, numberOfLine):
    with open(f"archives/{file}") as filetxt:
        content = filetxt.readlines()
        startfrom = len(content) - numberOfLine

        last = (content[startfrom:])
        my_str = ''.join(last)
        return my_str
    

result = tail('sample.txt', 3)
print(result)