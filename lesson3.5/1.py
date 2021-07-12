# Windows:
# C:\directory\file

# Unix:
# /directory/file

# ThisIsName, thisisname

path = "/dir/file"

path = "c:/dir/file"

# LF -> \n
# CR LF -> \r\n

file = "./test.txt"

# s = open(file, mode="r")
s = open(file, mode="w")
# ch = s.read(1)
# while ch != '':
#     print(ch, end='')
#     ch = s.read(1)

# line = s.readline(1)
# while line != '':
#     print(line, end='')
#     line = s.readline(1)

# lines = s.readlines(1)

s.write("My new text")
# print(lines)

s.close()

