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
    iterated_document = []
    for line in iterable_document:
        #print(line)
        if line.startswith("*"):
            iterated_document.append(line)
        #print(f"this is the iterated one \n{iterated_document}\n\n")
    joined_string = "\n".join(iterated_document)
    #print(f"this one is joined \n{joined_string}")
    return joined_string
    
    #print(iterable_document)
    #print(f"this is iterable document \n {iterable_document}")
    pass
