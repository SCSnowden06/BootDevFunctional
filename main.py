def change_bullet_style(document):
    split_doc = document.split("\n")
    joined_string = "\n".join(list(map(convert_line, split_doc)))
    return joined_string
    




def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
