def p(a, b, c):
    if a > 18:
        if b == "TR":
            if c > 1000:
                print("OK")
            else:
                print("Not OK")
        else:
            print("Not OK")
    else:
        print("Not OK")

"""

Görev:
Bu fonksiyonu:
İsimleri düzelt
Guard clause kullan
Magic number kaldır
Extract variable uygula
Pure function olacak şekilde düzenle (print yerine return)

"""

# ÇÖZÜM:

MIN_AGE = 18
TARGET_COUNTRY = "TR"
MIN_SALARY = 1000

def user_check(age: int, country: str, salary: int) -> str:
    is_adult = age > MIN_AGE
    is_in_target_country = country == TARGET_COUNTRY
    has_enough_salary = salary > MIN_SALARY

    if not is_adult or not is_in_target_country or not has_enough_salary:
        return "Not OK"
    
    return "OK"

#----------------------------------------------------------------------------------

def order(o):
    if len(o["items"]) == 0:
        print("Empty")

    total = 0
    for i in o["items"]:
        total += i["p"]

    tax = total * 0.18
    total += tax
    print("Total:", total)

    with open("orderlog.txt", "a") as f:
        f.write(str(total))

"""

Görev:
Bu fonksiyonu:
“Tek bir iş yapma” prensibine göre böl
Pure/impure fonksiyonları ayır
Extract method uygula
“Magic number 0.18” sabitle

"""

# ÇÖZÜM:

TAX_RATE = 0.18

# Pure
def is_empty(order: dict) -> bool:    
    if len(order["items"]) == 0:
        return True
    return False

# Pure
def sum_order(order: dict) -> float:
    return sum(item["p"] for item in order["items"])

# Pure
def calculate_tax(total: float) -> float:
    total += TAX_RATE * total
    return total

# Impure
def write_to_document(data: float, file_path: str):
    try:
        with open(file_path, "a") as file:
            file.write(str(data))
    
    except FileNotFoundError:
        raise FileNotFoundError("File Not Found.")

def enter_order(order: dict):
    if is_empty(order):
        return "Orders is empty!"
    
    file_path = "orderlog.txt"

    write_to_document(calculate_tax(sum_order(order)), file_path)

#------------------------------------------------------------------------------
def c(u):
    # check if active
    if u["a"] == 1:
        # check ban
        if u["b"] == 0:
            print("welcome", u["n"])

"""

Görev:
İsimlendirmeleri düzelt
Magic number kaldır
Guard clause yap
Pure hale getir

"""

# ÇÖZÜM:

def get_welcome_message(user: dict) -> str:
    is_active = user["active"]
    is_ban = user["banned"]

    if not is_active or is_ban:
        return None
    
    return f"Welcome, {user['name']}"

#------------------------------------------------------------------------------------

def f(x, y, z):
    if x == 1:
        if y > 10:
            if z < 5:
                return (y*2) + (z*3)
            else:
                return (y*3) + (z*2)
    else:
        return y + z

"""

Görev:
Tüm nested yapıyı guard clause ile düzelt
Extract variable
İsimleri anlamlandır
Daha test edilebilir hale getir

"""

# ÇÖZÜM:

def calculate_numbers(number_x: int, number_y: int, number_z: int) -> int:

    is_x_equal_one = number_x == 1
    is_y_greater_ten = number_y > 10
    is_z_smaller_five = number_z < 5

    if (is_x_equal_one and is_y_greater_ten) and is_z_smaller_five:
        return (number_y * 2) + (number_z * 3)
    
    if (is_x_equal_one and is_y_greater_ten) and not is_z_smaller_five:
        return (number_y * 3) + (number_z * 2)

    return number_y + number_z