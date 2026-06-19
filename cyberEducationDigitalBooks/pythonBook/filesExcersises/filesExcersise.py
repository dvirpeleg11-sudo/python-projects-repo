input_file = open(r"C:\Dvir\dear_prudence.txt", 'r')
current_line = input_file.readline()
while current_line != "":
    print(current_line, end="")
    current_line = input_file.readline()

input_file.close()

with open(r"/cyberEducationDigitalBooks/pythonBook/filesExcersises/dear_prudence.txt", 'a') as second_input_file:
    second_input_file.write('Dear Prudence open up your eyes\n')

"""with is great because even if we will have an exception, it will close the file."""
