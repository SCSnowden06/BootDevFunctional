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
    
    for tuple in file_extension_tuples:
        for item in tuple:
            for thing in item:                              #thing is a tuple; e.g. ('markup', ['.html', '.xml'])
                for piece in thing[1]:
                    dict1.update({piece : thing[0]})        # .html is file_extension_tuples.tuple.item.thing[1].piece

    return(dict1)
 
#def get_with_lambda(dictionary, key): {
#    dictionary.get(key, "Unknown")
#}

lambda_function = lambda dictionary, key : dictionary.get(key, "Unknown")

print(file_type_getter(test_tuple))

#print(get_with_lambda(file_type_getter(test_tuple), ".py"))
print(lambda_function(file_type_getter(test_tuple), ".docx"))