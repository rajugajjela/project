import re


str='my numbers 12 124 1 234 2345678 1980 19811'
fi= re.findall(r"\b\d{3,5}\b", str)
print(fi)
