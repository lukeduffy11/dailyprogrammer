# Create a program that will ask the users name and age, have it print that information.
# For extra credit, have the program log this information in a file to be accessed later.


name = raw_input("Please enter your name: ")
age = raw_input("Please enter your age: ")
print "Your name is " + name + ", and you are " + age + " years old."

# Open file, and allow appending. This will create a file at this location if one does not exist.
filename = "/home/luke/Documents/python_programming/log_for_easy1.txt"
f = open(filename, 'a')
f.write(name + '\t' + age + '\n')
f.close()

print "The log can be found at " + filename
