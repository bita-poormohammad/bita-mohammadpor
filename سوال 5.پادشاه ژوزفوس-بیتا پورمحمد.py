def josephus(n, k):
    if n == 1:
        return 0  # اگر فقط یک نفر باشد، او آزاد می‌شود
    else:
        return (josephus(n - 1, k) + k) % n

def main():
    x = int(input("تعداد آزمایش‌ها را وارد کنید: "))
    
    for _ in range(x):
        line = input("مقدار n و k را وارد کنید (با فاصله جدا کنید): ")
        if line == "*":
            break
        
        # تجزیه ورودی
        parts = list(map(int, line.split()))
        
        # مقدار پیش‌فرض n و k
        n = parts[0] if len(parts) > 0 else 100
        k = parts[1] if len(parts) > 1 else 2
        
        # محاسبه شخص آزاد شده
        result = josephus(n, k) + 1  # به خاطر اینکه شمارش از 0 شروع می‌شود
        print(result)

if __name__ == "__main__":
    main()
