def characterAnalysis(s):     
    d = {}     for char in s:  
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] *= -1
    return len(d)

print(characterAnalysis('bib'))