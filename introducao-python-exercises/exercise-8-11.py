def validate_string(string, min, max):
    return min <= len(string) <= max
        
print(validate_string("", 1, 5))
print(validate_string("ABC", 2, 5))
print(validate_string("ABCEFG", 3, 5))
print(validate_string("ABCEFG", 1, 10))