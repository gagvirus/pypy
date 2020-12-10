file = open('.gitignore', 'r')  # second argument - r / w / a / wb

print(file.read(100))  # arg -> number of bytes to read

print(file.readlines())

file.close()

with open('.gitignore') as f:
    print(f.read())
