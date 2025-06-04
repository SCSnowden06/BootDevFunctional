def format_line(line):
    stripped = line.strip()
    uppered = stripped.upper()
    replaced = uppered.replace('.', '')
    suffixed = replaced + '...'
    return suffixed
    
    
    
