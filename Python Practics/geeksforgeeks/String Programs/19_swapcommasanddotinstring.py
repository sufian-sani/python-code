a='14, 625, 498.002'
print('Orginal: ',a)
a=a.replace(', ','th')
print('1st step :',a)
a=a.replace('.',', ')
print('2st step :',a)
a=a.replace('th','.')
print('Final step :',a)