def get_median_font_size(font_sizes):
    sorted_list = sorted(font_sizes)
    if len(sorted_list) == 0:
        return None
    elif len(sorted_list) %2 == 0:
        return sorted_list[((len(sorted_list) // 2) -1)]
    else: 
        return sorted_list[(len(sorted_list) // 2)]
    
    
