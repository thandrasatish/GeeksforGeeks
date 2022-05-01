# A prime number is Super Prime if it is a sum of two primes. Find all the Super Primes upto N

def superPrimes(n):
    ans = 0
    primes = [True for i in range(n+1)]
    def prime(n):
        i = 2
        primes[0] = False
        primes[1] = False
        while(i*i <= n):
            if primes[i] == True:
                for k in range(i+i,n+1,i):
                    primes[k] = False
            i+=1
    prime(n)
    arr = []
    for each in range(len(primes)):
        if primes[each]:
            arr.append(each)
    for num in arr:
        if primes[num]:
            if primes[num-2]:
                ans += 1
    #print(primes)
    return ans
	# code here
n=int(input())
print(superPrimes(n))
