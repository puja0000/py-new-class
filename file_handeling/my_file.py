my_file1=open("bill_note.txt",'w+')

my_file1.write("hello\n")

my_file1.seek(0)

print(my_file1.read())

my_file1.close()

