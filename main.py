import functools

def join(doc_so_far, sentence):
    doc_so_far = doc_so_far + ". " + sentence
    return doc_so_far 
    
def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    else: 
        sliced_list = sentences[:n]
        reduced_list = functools.reduce(join, sliced_list)
        return reduced_list + "."
