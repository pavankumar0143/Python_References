x,y,z,n= (int(input()) for _ in range(4))
lc=[[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if (c+b+a) !=n]
print lc
