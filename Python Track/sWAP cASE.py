def swap_case(s):
    svar = ""
    for i in range(len(s)):
        if (s[i].isupper()):
            svar = svar + s[i].lower()
        elif s[i].islower():
            svar=svar+ s[i].upper()
        else:
            svar = svar+s[i]
    return svar
    

