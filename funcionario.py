
def primos_ate(n):
    e = eratosteles(n)
    return [e[i] for i in range(n) if e[i]!=False]

def maior_fator_primo_de(n):
    ps = primos_ate(n)
    for p in ps[::-1]:
        if n % p==0:
            return p
    return n

def eratosteles(n):
    flags = list(range(n+1))
    flags[0]=False
    flags[1]=False
    for k in flags:
        if k==False:
            continue
        else:
            for idx in range(2*k,n+1,k):
                flags[idx] = False
    return flags