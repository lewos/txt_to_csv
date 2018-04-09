from itertools import tee, izip_longest

def split_text(text, list_of_sep): 
    parts = [text[i:j] for i,j in izip_longest(list_of_sep,list_of_sep[1:])]
    return parts

def text_to_csv(path_text_file,name_list, list_of_sep, path_new_file):
    old = open(path_text_file, 'r') 
    new_file = open(path_new_file, 'w')
    name_list.append("\n")
    new_file.write((",").join(name_list))
    for line in old:
        list_parts = split_text(line,list_of_sep)
        new_file.write(write_new_file(list_parts,new_file))
    new_file.close()

def write_new_file(list_parts,path_new_file):
    return ",".join(list_parts)