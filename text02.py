import re

str='X-DSPAM-Confidence:0.8475'

new_str=str[19:]

f=float(new_str)
print(f)
print('---------------------------')

str1='my shcool is qujing university'


s=re.compile(str1)

s=s.sub('shcool','colleg')

print(s)