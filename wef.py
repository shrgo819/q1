import pandas as pd
def search(st,l):
    for i in range(len(l)):
        if l[i]==st:
            return i
def noooo(path1,path2):
    df=pd.read_csv(p1)#'/home/sunbeam/PycharmProjects/Ml/file1.csv')
    dm=pd.read_json(p2)#'/home/sunbeam/Downloads/students.json')
    l=[]
    l=df['name']
    r=[]
    for i in range(len(l)):
        t=1
        j=0
        k=0
        st=l[i]
        for c in st:
            if (c>'z' or c<'A' or (c>'Z' and c<'a'))and c != ' ':
                t=0
            if c==' ':
                j=1
            if c >='A' and c<='Z':
                k=1
        if t==0 or j==0 or k==0:
            print(st)
            r.append(st)
    for i in range(len(l)):
        if l[i] not in r and l[i] in dm['n']:
            w=search(l[i],dm['n'])
            print(l[i],dm['i'][w],dm['d'][w],df['organisation'][i],df['program'][i])

p1=input()
p2=input()
noooo(p1,p2)






























