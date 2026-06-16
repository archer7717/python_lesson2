

def p(x):
     for i in range(2, int(x**0.5)+1):
         if x%i==0:
             return [i]+p(x//i)
     return [x]

for i in range(0, 1_475_000):
    d = sorted(set(p(i)))
    if len(d) > 0:
        S = sum(d)
        if S!=0 and S <= 42000 and S%6==0:
            print(i, S)