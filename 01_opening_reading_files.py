
# OPENING FILES

#Opening file using r (read) and t (text)

f = open('README.md', 'rt')

content = f.read()
print(content)
print('#' * 80)



# There is a way to open and close the file automatically
# When we use with, we just have to to do whatever we want to do and the document will be automatically closed. 
with open('README.md') as file:
    content = file.read()
    print(content)

print(file.closed)
print('#' * 80)





# READING FILES INTO A LIST




# We can read a file with split lines
with open('README.md') as f:
    content = f.read().splitlines()
    print(content)

print('#' * 80)


# We can read the file and create a list, after that we can create a loop interate with the elements of the list

with open('README.md') as f:
    content = list(f)
    print(content)
print('#' * 50)

# Iterate over the file
with open('README.md') as file:
    for f in file:
        print(f, end='')
print('#' * 50)




# READING  TO TEXT FILES
# Writing something to the file
with open('texts.txt', 'w') as file:
    file.write('Many example using many tools\n')
    file.write('Network is still very important\n')
    

# Adding something to the file
with open('texts.txt', 'a') as file:
    file.write('You have to learn Network\n')
print('#' * 80)



# READING AND WRITING IN A FILE
# The fils must to exist in this case
with open('texts.txt', 'r+') as f:
    f.write('OSPF and BGP are very important protocols')









