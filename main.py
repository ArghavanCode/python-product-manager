import os

# نام فایلی که اطلاعات محصولات در آن ذخیره می‌شود
FILE_NAME = "products.txt"

def load_products():
    """این تابع محصولات را از فایل متنی می‌خواند و به صورت لیست برمی‌گرداند"""
    products = []
    if not os.path.exists(FILE_NAME):
        return products
    
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            # حذف فاصله‌های اضافی و شکستن متن با علامت کاما
            data = line.strip().split(",")
            if len(data) == 3:
                name, price, quantity = data
                products.append({
                    "name": name,
                    "price": float(price),
                    "quantity": int(quantity)
                })
    return products

def save_products(products):
    """این تابع لیست محصولات را می‌گیرد و داخل فایل txt ذخیره می‌کند"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for prod in products:
            file.write(f"{prod['name']},{prod['price']},{prod['quantity']}\n")

def add_product():
    """تابع اضافه کردن محصول جدید"""
    print("\n--- اضافه کردن محصول جدید ---")
    name = input("نام محصول را وارد کنید: ").strip()
    
    try:
        price = float(input("قیمت محصول: "))
        quantity = int(input("تعداد یا موجودی محصول: "))
    except ValueError:
        print("خطا! قیمت و تعداد باید به صورت عدد وارد شوند.")
        return

    products = load_products()
    products.append({"name": name, "price": price, "quantity": quantity})
    save_products(products)
    print(f"محصول '{name}' با موفقیت ذخیره شد!")

def show_products():
    """تابع نمایش همه محصولات موجود"""
    print("\n--- لیست محصولات موجود ---")
    products = load_products()
    
    if not products:
        print("هیچ محصولی ثبت نشده است.")
        return
        
    for index, prod in enumerate(products, 1):
        print(f"{index}. نام: {prod['name']} | قیمت: {prod['price']} | موجودی: {prod['quantity']}")

def search_product():
    """تابع جستجوی محصول بر اساس نام"""
    print("\n--- جستجوی محصول ---")
    search_name = input("نام محصول مورد نظر را وارد کنید: ").strip().lower()
    products = load_products()
    found = False
    
    for prod in products:
        if search_name in prod['name'].lower():
            print(f"پیدا شد! -> نام: {prod['name']} | قیمت: {prod['price']} | موجودی: {prod['quantity']}")
            found = True
            
    if not found:
        print("محصولی با این نام پیدا نشد.")

def main_menu():
    """منوی اصلی برنامه که تا زمان خروج کاربر اجرا می‌شود"""
    while True:
        print("\n===== سیستم مدیریت محصولات SianTech =====")
        print("1. اضافه کردن محصول")
        print("2. نمایش همه محصولات")
        print("3. جستجوی محصول")
        print("4. خروج از برنامه")
        
        choice = input("لطفاً یک گزینه را انتخاب کنید (1-4): ").strip()
        
        if choice == "1":
            add_product()
        elif choice == "2":
            show_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            print("خروج از برنامه. موفق باشید ارغوان عزیز!")
            break
        else:
            print("گزینه نامعتبر! لطفاً عددی بین 1 تا 4 وارد کنید.")

# اجرای منوی اصلی برنامه
if __name__ == "__main__":
    main_menu()
  
