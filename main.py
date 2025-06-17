#def change_bullet_style(document):
#    split_doc = document.split("\n")
#    joined_string = "\n".join(list(map(convert_line, split_doc)))
#    return joined_string
    

#def convert_line(line):
#    old_bullet = "-"
#    new_bullet = "*"
#    if len(line) > 0 and line[0] == old_bullet:
#        return new_bullet + line[1:]
#    return line
################################################################################



def remove_invalid_lines(document):
    #print(document)
    iterable_document = document.split("\n")
    for line in iterable_document:
        print(f"look for this \n{line}\n")
        if line.startswith("-"):
            print("this logic is doing something") 
        return iterable_document
    #print(iterable_document)
    #print(f"this is iterable document \n {iterable_document}")
    pass
