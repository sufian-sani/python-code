def add_string(str):
    c_str=str[-3:]
    if len(str)<3:
        return str
    elif c_str == "ing":
        return str+"ly"
    else:
        return str+"ing"

print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))