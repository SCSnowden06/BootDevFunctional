test_tuple = [
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        
    ),
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        
    ),
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        
    ),
    (
        [("code", [".py", ".js"]), ("markup", [".html", ".xml"])],
        
    ),
]

def file_type_getter(file_extension_tuples):
    dict1 = {}
    i = 1

    for tuple in file_extension_tuples:
        for item in tuple:
            for thing in item:                              #thing is a tuple; e.g. ('markup', ['.html', '.xml'])
                for piece in thing[1]:
                    #print(piece)
                    #print(f"this is a thing0 {thing[0]} \n")
                    dict1.update({piece : thing[0]})

    return(dict1)
 

print(file_type_getter(test_tuple))