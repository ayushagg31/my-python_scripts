import os

file_list = os.listdir(r"/home/ayush/PycharmProjects/untitled/prank/prank")
cwd = os.getcwd()
print(cwd)
os.chdir(r"/home/ayush/PycharmProjects/untitled/prank/prank")
for file_name in file_list:
    os.rename(file_name,file_name.translate(None,"0123456789"))
os.chdir(cwd)
