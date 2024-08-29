def unique_characters_extractor(x):
    extracted = []
    for val in x:
        if val not in extracted:
            extracted.append(val)
    return (extracted)

def index_collector(string, character):
    indices = []
    for index, char in enumerate(string):
        if char == character:
            indices.append(index)
        else:
            continue
    return indices