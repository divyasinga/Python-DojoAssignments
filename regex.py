import re

def get_matching_words():
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    matches = []
    for word in words:
        if re.search(r'v', word):
 		    matches.append(word)
        elif re.search(r'ss', word):
            matches.append(word)
        elif re.search(r"\w*e\b", word):
            matches.append(word)
        elif re.search(r"b\wb", word):
            matches.append(word)
        elif re.search(r"b\w+b", word):
            matches.append(word)
        elif re.search(r"b\w+b", word):
            matches.append(word)
        elif re.search(r"b\w*b", word):
            matches.append(word)
        elif re.search(r"\w*a\w*e\w*i\w*o\w*u\w*y\w*", word):
            matches.append(word)
        elif re.search(r"(.)\1", word):
            matches.append(word)
    print matches
    print words

get_matching_words()