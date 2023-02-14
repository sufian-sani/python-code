items='red,black,pink,green'
words = [word for word in items.split(",")]

print(','.join(sorted(list(set(words)))))