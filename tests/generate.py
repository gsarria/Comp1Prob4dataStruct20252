#!/usr/bin/env python3
import os, math
def first_primes(n):
    if n==1: return [2]
    ub = int(n*(math.log(n)+math.log(math.log(n))))+10 if n>=6 else 20
    sieve=[True]*(ub+1); sieve[0]=sieve[1]=False
    for p in range(2,int(ub**0.5)+1):
        if sieve[p]:
            step=p; start=p*p
            sieve[start:ub+1:step]=[False]*(((ub-start)//step)+1)
    return [i for i,v in enumerate(sieve) if v][:n]
def w(name, n):
    os.makedirs("tests", exist_ok=True)
    open(f"tests/input_{name}.txt","w").write(str(n)+"\n")
    arr=first_primes(n)
    open(f"tests/output_{name}.txt","w").write(" ".join(map(str,arr))+"\\n")
def main():
    w("min",1); w("max",10**5); w("rnd",1234)
if __name__=="__main__": main()
