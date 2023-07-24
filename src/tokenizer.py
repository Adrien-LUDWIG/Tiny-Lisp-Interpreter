def tokenize(source_code):
    return source_code.replace("(", " ( ").replace(")", " ) ").split()
