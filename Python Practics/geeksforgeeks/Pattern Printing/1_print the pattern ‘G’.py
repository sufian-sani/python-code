n=int(input())

for row in range(0,n):
    for col in range(0,n):
        if ((col==0 and row!=0 and row!=n-1) or ((col==1) and (row==0 or row==n-1)) or ((col==n-5) and (row==0 or row==n-4 or row==n-1)) or ((col==n-4) and (row==0 or row==n-4 or row==n-1)) or ((col==n-3) and (row>n-5 and row<n-1))):
            print('* ',end=' ')
        else:
            print(' ',end=' ')
    print()

'''
# Python Learn program to print pattern G 
def Pattern(line): 
	pat="" 
	for i in range(0,line):	 
		for j in range(0,line):	 
			if ((j == 1 and i != 0 and i != line-1) or ((i == 0 or
				i == line-1) and j > 1 and j < line-2) or (i == ((line-1)/2) 
				and j > line-5 and j < line-1) or (j == line-2 and
				i != 0 and i != line-1 and i >=((line-1)/2))): 
				pat=pat+"*"
			else:	 
				pat=pat+" "
		pat=pat+"\n"
	return pat 

# Driver Code 
line = 7
print(Pattern(line)) 

'''