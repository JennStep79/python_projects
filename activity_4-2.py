# acivity for errors
fileName = input("Please enter hte name of the file you would like to read: ")
 # Open a file for reading.
contents = myfile.readlines() # Read in the content by line.
myfile.close() # Explicitly close the file
print(contents) #print the contents of the file

class FileManipulator:
    def __init__(self, file_name):
        self.contents = None
        while self.contents == None:
            try:
                myfile = open(file_name, 'r')
                contents = myfile.readlines()
            except (FileNotFoundError, TypeError, OSError) as e:
                print(f"Input file not found or misconfigured. {e}")
                file_name = input("Pleae enter the name of the file you would like to read: ")
            else:
                print(self.contents)
                self.myfile.close()

    def reverse(self, new_filename):
        try:
            new_file = open(new_filename, "w")
            reversed = self.contents[::-1]
            new_file.write(reversed)
        except (FileNotFoundError, TypeError, OSError) as e:
            print(f"Input file not found or misconfigured. {e}")
                

f = FileManipulator('tmp.txt')

'''
test code:

f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp2.txt")
'''