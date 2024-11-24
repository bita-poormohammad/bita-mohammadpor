def sort_string(input_string):
    # حذف اسپیس‌ها و تپ‌ها
    input_string = ''.join(input_string.split())
    
    # تقسیم کاراکترها به سه دسته: حروف، اعداد و علامت‌های خاص
    letters = []
    numbers = []
    special_chars = []

    for char in input_string:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            numbers.append(char)
        else:
            special_chars.append(char)

    # مرتب‌سازی حروف بر اساس حروف الفبایی
    letters.sort()

    # ترکیب نتایج
    sorted_string = ''.join(special_chars) + ''.join(numbers) + ''.join(letters)
    
    return sorted_string

# دریافت ورودی از کاربر
input_string = input("لطفا رشته ورودی را وارد کنید: ")
output_string = sort_string(input_string)

# چاپ خروجی
print("رشته مرتب شده:", output_string)
