def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
    return primes

def main():
    n = int(input())
    m = int(input())

    primes = sieve_of_eratosthenes(n + 1)

    # بررسی اینکه آیا m یک عدد اول است
    if m in primes:
        print(1)
        return
    
    # اگر m عدد اول نیست، بررسی تعداد اعداد خط خورده
    # لیست تمام اعداد از 2 تا n
    non_primes = [i for i in range(2, n + 1) if i not in primes]
    
    # پیدا کردن موقعیت m در لیست اعداد غیر اول
    if m in non_primes:
        k = non_primes.index(m) + 1  # به خاطر اینکه ایندکس از صفر شروع می‌شود
        print(k)
    else:
        print("m is out of range")  # اگر m خارج از بازه باشد

if __name__ == "__main__":
    main()
