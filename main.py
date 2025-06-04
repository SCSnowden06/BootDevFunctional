def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    new_tuple = prefix + document
    new_new_tuple = (new_tuple, )
    # documents(new_doc)
    return documents + new_new_tuple
    
