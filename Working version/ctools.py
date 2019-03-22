#from re import *
def increment(a):
    if type(a)!=str:
        return a+1
    if a.isalnum()!=True:
        return 1
    temp=""
    carry=0
    match = {'z': 'a', 'Z': 'A', '9': '0'}
    if a[-1] in match:
        temp += match[a[-1]]
        carry=1
    else:
        temp+=chr(ord(a[-1])+1)
    for i in range(len(a)-2,-1,-1):
        if carry:
            if a[i] in match:
                temp+=match[a[i]]
            else:
                temp += chr(ord(a[i])+1)
                carry=0
        else:
            temp += a[i]
    return temp[::-1]

def PreIncrement(name, local={}):
    #Equivalent to ++name
    if name in local:
        local[name]=increment(local[name])
        return local[name]
    globals()[name]=increment(globals()[name])
    return globals()[name]

def PostIncrement(name, local={}):
    #Equivalent to name++
    if name in local:
        temp=local[name]
        local[name] = increment(local[name])
        return temp-1
    temp=globals()[name]
    globals()[name] = increment(globals()[name])
    return temp-1
def PreDecrement(name, local={}):
    #Equivalent to --name
    if name in local:
        local[name]=str2int(local[name])-1
        return local[name]
    globals()[name]=str2int(globals()[name])-1
    return globals()[name]

def PostDecrement(name, local={}):
    #Equivalent to name--
    if name in local:
        local[name] = str2int(local[name])-1
        return local[name]+1
    globals()[name] = str2int(globals()[name])-1
    return globals()[name]+1

def cmp(a,b):
    return ((a > b) - (a < b)) 

def dor(a,b):
    if a in globals() or a in locals():
        return a
    else:
        return b
def str2int(a):
    try:
        return int(a)
    except:
        temp=""
        for i in a:
            if  48<=ord(i)<=57:
                temp+=i
            else:
                break
        if temp=="":
            return 0
        return int(temp)


def str2float(a):
    try:
        return float(a)
    except:
        temp = ""
        for i in a:
            if 48 <= ord(i) <= 57 or ord(i)==46:
                temp += i
            else:
                break
        if temp == "":
            return 0.0
        return float(temp)

def strbitwise(a,op,b):
    temp=""
    if op=='&':
        for i in range(0,min(len(a),len(b))):
            temp+=chr(ord(a[i]) & ord(b[i]))
        return temp
    elif op=='|':
        if len(a)>len(b):
            b+="0"*(len(a)-len(b))
            for i in range(0,len(a)):
                temp+=chr(ord(a[i]) | ord(b[i]))
        elif len(b) > len(a):
            a += "0"*(len(b)-len(a))
            for i in range(0, len(b)):
                temp += chr(ord(a[i]) | ord(b[i]))
        else:
            for i in range(0, len(b)):
                temp += chr(ord(a[i]) | ord(b[i]))
        return temp
    elif op == '^':
        if len(a) > len(b):
            b += "0"*(len(a)-len(b))
            for i in range(0, len(a)):
                temp += chr(ord(a[i]) ^ ord(b[i]))
        elif len(b) > len(a):
            a += "0"*(len(b)-len(a))
            for i in range(0, len(b)):
                temp += chr(ord(a[i]) ^ ord(b[i]))
        else:
            for i in range(0, len(b)):
                temp += chr(ord(a[i]) ^ ord(b[i]))
        return temp


def flatten(l):
    flat_list=[]
    for sublist in l:
        if type(sublist)!=list:
            flat_list.append(sublist)
        else:
            for item in sublist:
                flat_list.append(item)
    return flat_list

def insert_into(l,pos,item):
    length = len(l)
    if pos<length:
        l[pos]=item
    else:
        for i in range(pos-length):
            l.append(None)
        l.append(item)
