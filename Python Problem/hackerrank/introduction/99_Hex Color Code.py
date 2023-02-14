#[A-Fa-f0-9]{3,6}
import re

line = False
line_input=int(input())

for _ in range(line_input):
    single_line=input()
    if '{' in single_line:
        line=True
    elif '}' in single_line:
        line=False
    elif line:
        for color in re.findall('#[A-Fa-f0-9]{3,6}',single_line):
            print(color)

