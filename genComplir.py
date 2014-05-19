from subprocess import call
from sys import argv
import core.global_obj as global_obj
import core.lang_wrappers as wrappers
import core.execute_code as execute_code
import os


file_obj =  argv[1]

list_of_code = []
with open(file_obj,"r") as code:
    for line in code:
        line = line.strip("\n") 
        if "#!?" in line and "end" in line:
            list_of_code.append(lang_obj)
            continue
        if "#!?" in line and "start" in line:
            lang_obj = []
        lang_obj.append(line)

os.mkdir("tmp")        
os.chdir("tmp")
files_to_run = []
lists = []
dicts = []
for lang_obj in list_of_code:
    to_run = []

    first_line = lang_obj[0]
    lang = first_line.split("start")[1].lstrip(" ")
    if lang == "cpp":
        lang_file = "tmp.cpp"
    if lang == "java":
        lang_file = "tmp.java"
    if lang == "python":
        lang_file = "tmp.py"
    if lang == "ruby":
        lang_file = "tmp.rb"
    if lang == "perl":
        lang_file = "tmp.pl"

    lang_list = []
    for lang_check,lang_file_check in files_to_run:

        lang_list.append(lang_check)
    
    if lang in lang_list:
        count = lang_list.count(lang)
        if lang == "python":
            lang_file = "tmp"+str(count)+".py"
        if lang =="ruby":
            lang_file = "tmp"+str(count)+".rb"
        if lang == "perl":
            lang_file = "tmp"+str(count)+".pl"
        if lang == "java":
            lang_file = "tmp"+str(count)+".java"
        if lang == "cpp":
            lang_file = "tmp"+str(count)+".cpp"
    
    with open(lang_file,"w") as f:
        for elem in global_obj.check_for_lists(lang_obj,f):
            lists.append(elem)
        for elem in global_obj.check_for_dicts(lang_obj,f):
            dicts.append(elem)

        if lang == "java":
            wrappers.java_start(f)
        if lang == "cpp":
            wrappers.cpp_start(f)

        for obj in lists:
            if lang == "python" or lang == "ruby":
                f.write(obj + " = []\n")
        for obj in dicts:
            if lang == "python" or lang == "ruby":
                f.write(obj + " = {}\n")

        for i in xrange(1,len(lang_obj)):
            lang_obj[i] += "\n"
            f.write(lang_obj[i])
        
        if lang == "java":
            wrappers.java_end(f)
        if lang == "cpp":
            wrappers.cpp_end(f)
    
    to_run.append(lang)
    to_run.append(lang_file)
    
    files_to_run.append(to_run)

execute_code.run(files_to_run)

os.chdir("../")
os.rmdir("tmp")

