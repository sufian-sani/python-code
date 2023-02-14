def reverse_string_words(str):
    for line in str.split('\n'):
        return (' '.join(line.split()[::-1]))

print(reverse_string_words("Python Exercises."))