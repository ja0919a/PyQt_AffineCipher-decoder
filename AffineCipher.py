def encode(crypt,mod,a,b,case,foreign):
    m=len(mod)
    result=""
    for i in range(len(crypt)):
        temp=crypt[i]
        if case==0:
            state=temp.isupper()
            temp=temp.lower()
        elif case==1:
            temp=temp.lower()
        if temp in mod:
            x=mod.index(temp)
            x=a*x+b
            x=x%m
            if case==0:
                if state:
                    result+=mod[x].upper()
                else:
                    result+=mod[x]
            else:
                result+=mod[x]
        else:
            if foreign==0:
                result+=crypt[i]
    return result

def decode(crypt,mod,a,b,case,foreign):
    m=len(mod)
    result=""
    for i in range(len(crypt)):
        temp=crypt[i]
        if case==0:
            state=temp.isupper()
            temp=temp.lower()
        elif case==1:
            temp=temp.lower()
        if temp in mod:
            x=mod.index(temp)
            aa=1
            while a*aa%m!=1:
                aa+=1
            x=aa*(x-b)
            x=x%m
            if case==0:
                if state:
                    result+=mod[x].upper()
                else:
                    result+=mod[x]
            else:
                result+=mod[x]
        else:
            if foreign==0:
                result+=crypt[i]
    return result
        
    
    