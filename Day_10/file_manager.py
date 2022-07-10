import os

# Absolute path for this file
this_file_path= os.path.abspath(__file__)
#print(this_file_path)

# "os.path.dirname" retrieves the directory for whatever file or directory is input
BASE_DIR=os.path.dirname(this_file_path)
ENTIRE_PROJECT_DIR=os.path.dirname(BASE_DIR)
#print(BASE_DIR, ENTIRE_PROJECT_DIR)


email_txt=os.path.join(BASE_DIR, "templates", "email.txt")

content = ""

with open(email_txt, 'r') as f:
    content = f.read()

print(content.format(name="Atiba"))