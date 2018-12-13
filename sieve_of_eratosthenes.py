def prime(n):
    non_prime= []
    for i in range(2, n+1):
        if i not in non_prime:
            print (i)
            for j in range(i*i, n+1, i):
                non_prime.append(j)

x=int(input("Enter No."))
prime(x)







