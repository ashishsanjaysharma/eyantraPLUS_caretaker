def getrange(o,p,q):
    o=int(o/2);
    p=int(p*2+25);
    q=int(q*2+25);
    if((o-20)<0):
        ol=0
        ou=o+20
    if ((o+20)>179):
        ol=o-20
        ou=179
    if((o-20)>0 and (o+20)<179):
        ol=o-20
        ou=o+20
            
    return (ou,p+20,q+20,ol,p-20,q-20)

a,b,c,d,e,f=getrange(352,23,89)#pnk
print a,b,c,d,e,f

a,b,c,d,e,f=getrange(221,67,84)#pnk
print a,b,c,d,e,f

a,b,c,d,e,f=getrange(356,73,80)#pnk
print a,b,c,d,e,f

a,b,c,d,e,f=getrange(189,89,48)#pnk
print a,b,c,d,e,f
