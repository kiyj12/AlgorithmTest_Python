# p.323 나중에 풀자...

import re
stc = input()

halfnum = round(len(stc)/2)

for i in range(halfnum):
    ch = halfnum -i
    for j in range(halfnum//ch):
        pattern = stc[j:j+ch]
        plist = re.findall(pattern, stc)
        if len(plist) > 1:

        
    