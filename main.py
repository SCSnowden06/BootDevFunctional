def change_bullet_style(document):

    #print(f"this part is the document\n{document}\n\n")
    split_doc = document.split("\n")
    #print(split_doc)
    #print(list(map(convert_line, split_doc)))

    joined_string = "\n".join(list(map(convert_line, split_doc)))
    #print(f"this part is thie joined string\n{joined_string}")
    #print("\n".join(converted_document))
    return joined_string
    #return converted_document.join("\n")




def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
