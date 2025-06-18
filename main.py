def remove_invalid_lines(document):
    iterable_document = document.split("\n")
    iterated_document = []
    for line in iterable_document:
        if line.startswith("-") == False:
            iterated_document.append(line)
    joined_string = "\n".join(iterated_document)
    return joined_string