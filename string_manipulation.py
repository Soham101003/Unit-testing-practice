def string_cap(name):
    if not isinstance(name,str):
        raise ValueError("Should be string")   
    return name.strip().capitalize()

