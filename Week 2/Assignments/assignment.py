'''
Write a Python function called read_file() that takes a single parameter
filename, and opens the specified file in read-only mode. 
The function should read the entire contents of the file and return the contents as a string.
'''

def read_file(filename):
  fn = open('Week 2\Assignments\my_file.txt','r')
  actual_file = fn.read()
  print(actual_file)
  fn.close()
    
    # TODO: Open the file in read-only mode and read its contents. Return the contents of the file.
pass

contents = read_file("my_file.txt")
#print(contents)  # Output: "Hello, world!\nI just did my first Assignment of week 2."