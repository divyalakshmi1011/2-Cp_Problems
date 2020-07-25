# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"
def substrings(test_str):
    res = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]
    return res

def longestcommonsubstring(s1, s2):
    if(len(s1) == 0 or len(s2) == 0):
        return ""
    l1 = len(s1)
    l2 = len(s2)
    x = ""
    if(l1 < l2):
        l = substrings(s1)
        for i in l:
            if i in s2:
                if(len(x) == len(i)):
                    if(i > x):
                        x = i
                elif( len(x) < len(i)):
                    x = i
    else:
        l = substrings(s11)
        for i in l:
            if i in s1:
                if( len(x) < len(i)):
                    x = i
    return x

print(longestcommonsubstring("abcABC", "zzabZZAB"))
