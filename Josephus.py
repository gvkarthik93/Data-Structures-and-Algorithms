def josephus(n, k):
    if n == 1:
        return 0
    else:
        #The position returned by josephus(n - 1, k) is adjusted because the
        #recursive call josephus(n - 1, k) considers the original position 
        #k%n + 1 as position 1
        return (josephus(n-1,k)+k)%n

n = 7;
k = 2;
print (josephus(n,k))