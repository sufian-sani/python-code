def caesar_encrypt(str,n):
    str=str.lower()
    ls_str=list(str)
    ls_str_len=len(ls_str)
    count_alp=0
    get_ls=[]
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(ls_str_len):
        if str[i] in lowercase:
            count_alp+=1
    if ls_str_len==count_alp:
        for i in range(ls_str_len):
            for j in range(len(lowercase)):
                if str[i]==lowercase[j]:
                    get_ls.append(lowercase[j+n])

    return get_ls

code = caesar_encrypt('abc', 2)
print()
print(code)
print()
'''
def caesar_encrypt(realText, step):
	outText = []
	cryptText = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for eachLetter in realText:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)
	return outText

code = caesar_encrypt('abc', 2)
print()
print(code)
print()
'''