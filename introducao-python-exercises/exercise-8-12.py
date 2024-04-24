def string_in_list(string, list):
    return string in list
    
L = ["AB", "CD", "EF", "FG"]

print(string_in_list("AB", L))
print(string_in_list("CD", L))
print(string_in_list("EF", L))
print(string_in_list("FG", L))
print(string_in_list("XYZ", L))