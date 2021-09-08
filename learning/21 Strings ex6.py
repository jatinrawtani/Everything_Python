str = 'X-DSPAM-Confidence: 0.8475'
num=str.find(':')
a=float(str[num+2:])
print('The number in the given data is = ',a)