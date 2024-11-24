def main():
    # خواندن n و m
    n, m = map(int, input().split())
    
    # خواندن نام شهرها
    cities = [input().strip() for _ in range(n)]
    
    # ایجاد دیکشنری برای نگهداری پروازها
    flights = {city: [] for city in cities}
    
    # خواندن خطوط هوایی
    for _ in range(m):
        origin, destination = input().strip().split()
        flights[origin].append(destination)
    
    # تولید خروجی
    for city in cities:
        destinations = flights[city]
        print(len(destinations))  # تعداد شهرهایی که پرواز مستقیم دارد
        if destinations:
            print("\n".join(destinations))  # نام شهرها

if __name__ == "__main__":
    main()
