# file = open("text.txt")
#read all content/read n number of characters
#print(file.read())

#read a single line
#print(file.readline())
#print(file.readline())

# line = file.readline()
#
# while line != "":
#     print(line)
#     line = file.readline()

# readlines stores values in a list
# for line in file.readlines():
#     print(line)
#
# file.close()

# ********************WRITING**********************
# with this operation, no need for close command
# open ("text.txt" , "r"/"w") opens file in read or write mode
with open("text.txt", "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("text.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)