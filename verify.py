from math import isqrt

N=50000
pmax=[0]*(N+1)
for p in range(2,N+1):
    if pmax[p]==0:
        for n in range(p,N+1,p):
            pmax[n]=p
for n in range(2,N+1):
    d=next(t for t in range(isqrt(n),0,-1) if n%t==0)
    p=pmax[n]
    a=n//d-d
    assert abs(a-p)**3<=n*n
    if p*p>n:
        assert d==n//p and n//d==p
    else:
        assert d**3>=n
    if n==p**3:
        assert a-p==p*p-2*p
print("Verified exact divisor comparison for 2..50000 and the prime-cube witnesses.")
