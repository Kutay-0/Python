# pyright: reportUndefinedVariable=false
# pyright: reportMissingImports=false

#--------------------CLEAN-CODE-------------------
#-------------------İÇİNDEKİLER-------------------

# 22 - Clean Code Nedir ?
# 28 - Clean Code Neden Bu Kadar Önemli ?
# 47 - Clean Code'un Temel Kuralları
# 140 - Clean Code Standartı PEP8
# 174 - Code Teknikleri
# 176 - Guard Clause
# 201 - Pure/Impure Fonksiyonlar
# 263 - Early Return + Narrow Scope
# 283 - Small Modules, Big Systems
# 290 - Function Signature Netliği
# 304 - Refactoring Patterns
# 307 - Extract Method
# 357 - Extract Variable

#-------------------------------------------------
# Clean Code Nedir ?
# Clean code -> Okunması, anlaşılması ve değiştirilmesi kolay koddur.
# Amacımız sadece çalışır değil anlaşılır, esnek projeler geliştirmektir.

#-------

# Clean Code Neden Bu Kadar Önemli ?

# Kimse çalışan ama okunamayan kod istemez. Kodlarımız:

# - Okunabilir.
# - Sürdürmesi kolay.
# - Başkası rahat anlayacak.
# - Hatalar hızlı bulunacak.
# - Genişletilebilir olacak.

# Buna "Software Craftmanship" denir.

#-------

# EN ÖNEMLİ PRENSİP: "Okunabilirlik latent bir hata önleyicidir."
# Yani kod okunabilir olursa, daha yazarken hataların çoğunu otomatik olarak engellersin.

#-------

#-------------CLEAN-CODE'UN-TEMEL-KURALLARI--------------

# 1) ANLAMLI DEĞİŞKEN İSİMLERİ.

a = 5
b = "Kutay"         # KÖTÜ
c = a+b

#---

item_price = 10
tax = 20            # İYİ
total_price = item_price + tax

#-------

# 2) FONKSİYONLAR TEK BİR İŞ YAPMALI.

def process_user(data): 
    validate(data)      
    save_to_db(data)    # KÖTÜ    
    send_email(data)

#---

def validate_user(data):
    pass
def save_user(data):    # İYİ
    pass                
def notify_user(data):
    pass

#-------

# 3) KOD TEKRARLARINDAN KAÇIN (DRY)
age = 5

if age > 18:
    print("Adult")      # KÖTÜ
if age > 18:
    print("Can vote")

#---

is_adult = age > 18

if is_adult:            # İYİ
    print("Adult")
    print("Can vote")

#-------

# 4) MAGIC NUMBER KULLANMA
score = 100

# KÖTÜ:
if score > 70:
    print("Passed")

#---

# İYİ:
PASSING_SCORE = 70

if score > PASSING_SCORE:
    print("Passed")

#-------

# 5) FONKSİYONLAR KISA OLMALI

#   - 10-20 satırı geçmeyecek.
#   - Bir iş -> bir fonksiyon.
#   - Ne yaptığı ismiyle anlaşılmalı.

#-------

# 6) EXCEPTION HANDLING NET OLMALI

# KÖTÜ:
try:
    do_something()

except:
    pass

# İYİ:
try:
    do_something()

except ValueError:
    log("Invalid Value")

#-----------------CLEAN-CODE-STANDARDI-PEP-8-----------------

# İSİMLENDİRME KURALLARI:

# 1) DEĞİŞKEN VE FONKSİYONLAR -> snake_case
# Örnek:

user_name = "Kutay"

def get_user_name():
    pass

# 2) CLASS -> PascalCase
# Örnek:

class UserService:
    pass

# 3) SABİTLER -> UPPER_SNAKE_CASE
# Örnek:

MAX_RETRY = 3
DEFAULT_TIMEOUT = 5

# 4) BOOL DEĞİŞKENLER -> "is_" , "has_" , "can_" , "should_"
# Örnek:

is_admin = True
has_permission = False
can_edit = True
should_retry = False

# Bu pattern'ler okumayı inanılmaz kolaylaştırıyor.

#-------------CODE-TEKNİKLERİ-------------

# GUARD CLAUSE (ERKEN ÇIKIŞ) - İÇ İÇE IF YASAKTIR.
# KÖTÜ:

def process(user):
    if user:
        if user.is_active:
            if not user.is_banned:
                return calculate(user)
            
# İYİ:

def process(user):
    if not user:
        return
    
    if not user.is_active:
        return
    
    if user.is_banned:
        return
    
    return calculate(user)

#-------

# PURE FUNCTIONS (YAN ETKİSİZ FONKSİYONLAR)
# Bir fonksiyonun saf fonksiyon olabilmesi için 2 kural vardır:

# KURAL 1 - Aynı input -> Her zaman aynı output: Fonksiyonun çıktısı sadece parametrelere bağlıdır.
# KURAL 2 - Dış dünyayı değiştirmez: Dosya yazmaz, Database'e kaydetmez, Global değişken içermez, API çağırmaz, print bile etmez

#  PURE FONKSİYON ÖRNEĞİ:

def add(num1, num2):        # Değişken okumuyor -> Sadece parametre, Dosya yazmıyor, Databas'e kaydetmiyor,
    return num1 + num2      # Print etmiyor, Global değişkene dokunmuyor, Hep aynı input -> hep aynı output üretir.

#-------

# IMPURE FUNCTIONS (YAN ETKİLİ FONKSİYONLAR)
# Bir fonksiyon şu 3 şeyden birisini yapıyorsa impure fonksiyondur:

# KURAL 1 - Dış dünyayı değiştiriyorsa (Dosya,database,api)
# KURAL 2 - Aynı input -> Farklı output verebiliyorsa (Saat, tarih, random gibi şeyleri kullanıyorsa)
# KURAL 3 - Print, input vs. varsa

# IMPURE FONKSİYON ÖRNEKLERİ:

def save_user(data):
    db.save(data)       # DIŞ DÜNYA ETKİSİ -> IMPURE
    return True

#-

def show_result(a, b):
    print(a+b)          # IMPURE (I/O)

#-

counter = 0

def inc():
    global counter
    counter += 1        # GLOBAL DEĞİŞİYOR -> IMPURE

#-

def rool_dice():
    return random.randint(1,6)  # HER ÇAĞRIDA FARKLI -> IMPURE

# PURE/IMPURE FARKI NEDEN ÖNEMLİ ?

# PURE:
#   - Test etmesi kolaydır. (Sadece girdi-çıktı kontrol et.)
#   - Hata oranı düşüktür. (Dış dünya ile etkileşim yok.)
#   - Predictable (Girilen değere göre çıktı hesapla -> bitti)
#   - Paralel çalışmaya uygundur (Yan etki olmadığından aynı anda çalışabilirler.)

# IMPURE:
#   - Test etmesi zordur. (Dış etkenlerde sorun varsa önce onları çözmen gerekebilir.)
#   - Hatalar saklanabilir. (Global bir değişkeni değiştirmek, Yan etkiler vardır.)
#   - Debug etmesi zordur. (Bir yerde bir dış etki değişti. Ama nerede ?)
#   - Beklenmeyen sonuçlar üretebilir. (Aynı input - Farklı output çıkarabilir.)

# Yani olabildiğince PURE fonksiyonların sayısını arttırıp IMPURE fonksiyonların sayısını azaltmalıyız.

#-------

# EARLY RETURN + NARROW SCOPE (DEĞİŞKENLERİ MİNİMUM ALANDA TUTMA)

# KÖTÜ:
def something():
    result = 0
    if condition:
        result = calculate()
    return result

# İYİ:
def something():
    if not condition:
        return 0

    return calculate()

# Böylelikle gereksiz değişkenler yok

#--------

# SMALL MODULES, BİG SYSTEMS

# 200 satırlık tek bir dosya yerine -> 20 satırlık 10 modül daha temizdir.
# Kod kalabalığı ve kaostan kaçınılmış olunur.

#--------

# FUNCTION SIGNATURE NETLİĞİ

# Bir fonksiyonun ismine, aldığı parametrelerin adlarına bakan kişi fonksiyonun ne iş yaptığını anlamalıdır.

# KÖTÜ:
def process(data, x, y):
    pass

# İYİ: 
def create_invoice(customer_id: str, items: list, apply_discount: bool = True):
    pass

#-------

# REFACTORING PATTERNS

# EXTRACT METHOD -> Büyük fonksiyonu küçük parçalara böl

# KÖTÜ:
def process_order(order):
    # validate
    if not order.items:
        raise ValueError("Empty order")
    
    # calculate total
    total = sum(item.price for item in order.items)
    tax = total * 0.18
    total_with_tax = total + tax
    
    # save
    db.save(order)
    
    # send email
    email.send(order.user.email, f"Total: {total_with_tax}")

    return total_with_tax

#---

# İYİ:
def validate_order(order):
    if not order.items:
        raise ValueError("Empty order")


def calculate_total(order):
    total = sum(item.price for item in order.items)
    tax = total * 0.18
    return total + tax


def save_order(order):
    db.save(order)


def notify_user(order, total):
    email.send(order.user.email, f"Total: {total}")


def process_order(order):
    validate_order(order)
    total = calculate_total(order)
    save_order(order)
    notify_user(order, total)
    return total


# EXTRACT VARIABLE -> Uzun ifadeyi anlamlı değişkenlere ayır.

# KÖTÜ:
if (user.age >= 18 and user.country == "TR" and order.total > 1000) or (user.vip and order.total > 500):
    approve(order)

# İYİ:
is_adult_turkish = user.age >= 18 and user.country == "TR"
has_high_total = order.total > 1000
vip_large_order = user.vip and order.total > 500

if (is_adult_turkish and has_high_total) or vip_large_order:
    approve(order)

#---------------------GUN-1-TAMAMLANDI---------------------
#-----ISLAM-KUTAY-SAHIN---------------------26/11/2025-----