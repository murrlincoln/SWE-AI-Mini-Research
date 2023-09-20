, making sure the first letter of every word is capitalized, and return the newly formatted string

def capitalizer(string):
    string_list = string.split()
    capitalized_list = []
    for word in string_list:
        capitalized_list.append(word.capitalize())
    return " ".join(capitalized_list)