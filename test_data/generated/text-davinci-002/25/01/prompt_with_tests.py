def longestCommonSubstring(string1, string2):
    if len(string1) < len(string2):
        shorterstring = string1
        longerstring = string2
    else:
        shorterstring = string2
        longerstring = string1
        
    for idx in range(len(shorterstring), 0, -1):
        if shorterstring[idx-1] in longerstring:
            start = longerstring.index(shorterstring[idx-1])
            if shorterstring[idx-1: ]== longerstring[start: start+idx]:
                return shorterstring[idx-1: ]
    return ''