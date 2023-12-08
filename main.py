# a='babdcddc'
# a=sorted(a)
# c=1
# print(a)
# print(len(a))
# for i in range(0,len(a)-1):
#     if a[i]!=a[i+1]:
#         print(a[i],end='')
#         print(c,end='')
#         c=1
#     else:
#         c+=1
# if c>=1:
#     print(a[len(a)-1],end='')
#     print(c,end='')
    
    
MAX = 26

def compress_string(s, n):
    freq = [0] * MAX
    
    for i in range(n):
        print(ord(s[i]))
        print(ord('a'))
        print(freq[ord(s[i]) - ord('a')])
        freq[ord(s[i]) - ord('a')] += 1

    for i in range(MAX):
        if freq[i] == 0:
            continue
        print(chr(i + ord('a')) + str(freq[i]), end='')

# Example usage:
s = "abcaabbbcc"
n = len(s)
compress_string(s, n)
