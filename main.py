def file_type_getter(file_extension_tuples): 
    dict1 = {}
    
    for file_type, extensions in file_extension_tuples:
        for ext in extensions:
            dict1[ext] = file_type  

    return lambda ext: dict1.get(ext, "Unknown")

