# import textwrap
#
# def wrap(string, max_width):
#     line=''
#     for line in (textwrap.wrap(sample_text, width)):
#         line=''.join(line)
#     return line
#
# sample_text=input()
# width=int(input())
#
# print(wrap(sample_text, width))

# sample_text=input()
# sample_text='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# width=4
#
# # textw=''
#
# # for line in (textwrap.wrap(sample_text, width)):
# #     textw=''.join(line)
#
# # print(line)
# textw = textwrap.wrap(sample_text, width)
# print(textw)
# listToStr = '\n'.join([str(elem) for elem in textw])
# print(listToStr)

import textwrap

def wrap(string, max_width):
    listToStr=''
    textw = textwrap.wrap(sample_text, width)
    listToStr = '\n'.join([str(elem) for elem in textw])
    return listToStr

sample_text=input()
width=int(input())

print(wrap(sample_text, width))