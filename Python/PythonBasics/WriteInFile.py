# read the file and store all the lines in a list
# reverse the list
# Write the reversed list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()   # initial list  ['apple\n', 'ball\n', 'cat\n', 'dog\n', 'egg\n', 'fan\n', 'gravity']
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)




