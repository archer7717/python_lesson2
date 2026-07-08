
def f(x, A):
    return (x%A==0) or ((x%23==0) <= (not( 50 <= x <= 70)))


for A in range(1, 10000):
    if all(f(x,A)==1 for x in range(1, 10000)):
        print(A)