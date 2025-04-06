# READING A FILE
file = open("word.txt", "r")
data = file.read()
print(data)

file =  open("word2.txt", "w")
data = file.write("My Name is Dennis".upper())

file = open("word2.txt", "r")
data = file.read()
print(data)