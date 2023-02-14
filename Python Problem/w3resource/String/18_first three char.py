# def first_three(str):
#     if len(str)>3:
#         rest_str=str[:3]
#         return rest_str
#     else:
#         return str

def first_three(str):
	return str[:3] if len(str) > 3 else str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))