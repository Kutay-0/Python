# MUTABLE & IMMUTABLE NEDİR ?

# MUTABLE (DEĞİŞTİRİLEBİLİR) NESNELER
# - Bellekteki adresleri aynı kalır, içeriği değişebilir.

listeler: list      # İçerisindekileri değiştirebiliriz.
dictler: dict       # Değişiklik aynı objede olur.
setler: set         # id() değişmez!

# IMMUTABLE (DEĞİŞTİRİLEMEZ) NESNELER
# - Bellekte oluşturulduktan sonra içeriği değiştirilemez.

intler: int
floatlar: float
strler: str                 # Değiştirilemezler. Onun yerine yeni bir obje oluşturulur.
tupleler: tuple             
frozensetler: frozenset

#--------------ÖRNEK-1---------------

a = [1, 2, 3]
print(id(a)) # Output: 1426478577472 -> Bu bizim bellekteki yerimizi gösterir.

a.append(4)
print(id(a)) # Output: 1426478577472 -> Çıktı yine aynıdır. Çünkü yeni obje oluşmadı sadece değişti.

# Bu yüzden list türü DEĞİŞEBİLİRDİR(MUTABLE).

#--------------ÖRNEK-2---------------

x = 10
print(id(x)) # Output: 140721513997720
                                            # Son iki haneleri farklı. Yani içerik değiştirilmedi.
x = x + 1                                   # Eski "x" değişkeni kaldırılıp yeni bir integer objesi oluştu.
print(id(x)) # Output: 140721513997752 

#--------------ÖRNEK-3---------------
                                    # SMALL INTEGER CACHING
a = 5       #           5           # -5 ile 256 arası integer'lar sadece 1 kere oluşturulur.
b = 5       #       /   |   \       # Hepsi aynı objeyi gösterir. Üç değişken -> tek obje
c = 5       #      a    b    c      # id(a) == id(b) == id(c)

#--------------ÖRNEK-4---------------

x = [1, 2]      # Liste objesi oluşturulur.
y = x           # Yeni obje üretilmez -> sadece referans kopyalandı.
x.append(3)     # Yani burada y'de değişti.

#--------------ÖRNEK-5---------------

a = (1,2,3)     # Burada 2 değerleri aynı olan iki farklı obje üretiliyor.
b = (1,2,3)     # Yani a'da olan bir değişiklikte b etkilenmez.

#--------------------STRING-INTERNING--------------------

# String Interning: Python'daki bazı belirli stringlerin RAM'de tek bir obje olarak saklanmasıdır.
a = "Kutay"
b = "Kutay"

# Bu durumda a ve b aynı RAM adresini işaret eder.
# Python bu stringi sadece 1 defa oluşturur.

#--------------------STRING-INTERNING-KURALLARI---------------------

# Intern Edilenler:
# 1 - Sadece ASCII harfler.
# 2 - Sadece rakamlar.
# 3 - Alt çizgi.
# 4 - Kısa string.
# 5 - Değişken adı gibi görünen stringler.
# 6 - Boşluk, tire, noktalama içermeyenler.

a = "kutay"
b = "Hello"
c = "python3"
d = "abc123"
e = "HelloWorld"
f = "variable_name"

# Intern Edilemeyenler:
# 1 - Boşluk, tire, noktalama içerenler.
# 2 - Unicode karakterler içerenler (ş,i,ğ,ü,ç....).
# 3 - Uzun stringler.
# 4 - Dosya yolları, URL'ler.

a = "kutay sahin"
b = "kutay-şahin"
c = "hello world!"
d = "email@example.com"
e = "Türkiye"
f = "python rocks!"

# Bu kuralları "is" anahtar kelimesiyle kontrol edebiliriz. Örnek

"a" is "a"  # True -> Çünkü string interning gerçekleşti. Stringler kurallara uyuyor.
"a" == "a"  # True -> Çünkü stringlerin DEĞERLERİ aynı.

"İslam Kutay-Şahin" is "İslam Kutay-Şahin" # False -> Çünkü string interning gerçekleşmedi. Stringler kurallara uymuyor.
"İslam Kutay-Şahin" == "İslam Kutay-Şahin" # True -> Çünkü stringlerin DEĞERLERİ aynı.

#-------------------MUTABLE-DEFAULT-ARGUMENT-BUG-------------------

def ekle(value, liste=[]):          # Burada her seferinde yeni bir liste oluşuyormuş gibi gözüküyor.
    liste.append(value)             # Ama Python'da default parametreler sadece 1 DEFA OLUŞUR. RAM'de hep aynı yerde durur.
    return liste                    # Her fonksiyon çağırıldığında aynı liste kullanılır.
                                    # Listeler mutable olduklarından her değişiklik aynı objeye olur.
print(ekle(1))  # Output: [1]
print(ekle(2))  # Output: [1,2]
print(ekle(3))  # Output: [1,2,3]


def ekle_dogru_cozum(value, liste = None):  # 
    if liste is None:                       #
        liste = []                          # Bu şekilde her seferinde yeni bir liste oluşturulur.
    liste.append(value)                     #
    return liste                            #

#------------------------------------------------------------------

#-------------------SHALLOW-COPY-vs-DEEP-COPY------------------

# Öncelikle Shallow ve Deep Copy işlemleri mutable yapılar için mantıklıdır.
# Çünkü immutable değişkenler tek bir objeye referans verecektir. Yapılabilir ama gerek yoktur.

# Shallow Copy:  Bir listenin veya dict yapısının kopyasını oluşturur. Ama içerisindekileri kopyalamaz.
# Sadece referanslarını taşır. Yani:

import copy

a = [[1,2], [3,4]]      # Burada b, a listesine referans verir. Ama içerisindekileri kopyalamaz. Sadece iç listeler etkilenir.
b = a.copy()            # Buradaki olay şu şekilde düşünülebilir: b listesiyle işlem yaparsanız a listesi üzerinden erişir.
                        # b listesine (b.append()) uygularsanız a içeriği değişmez ama b[0].append() yaparsanız a içeriğide değişir.

a[0] is b[0] # True -> Çünkü aynı objelere referans verilir.

# Deep Copy:    Dış liste kopyalanır. İçerisindeki her obje RAM'de yeni bir adreste oluşturulur.
# Yani tıpatıp aynı 2 bağımsız yapımız olmuş oldu.

c = copy.deepcopy(a)

a[0] is c[0] # False -> Çünkü yepyeni bağımsız bir liste oluşturulur.

#--------------------HASH()-NEDIR-HASHABLE-UNHASHABLE-MANTIĞI-----------------

# Hash: o objenin kimliğini belirleyen SABİT BİR SAYIDIR.

# Her hashlenebilir obje için Python, RAM'da sabit duran bir "kimlik" üretir.
# Bu da demek oluyor ki değişebilen yani MUTABLE yapılar HASHLENEMEZ.

# Hash Ne İşe Yarar: Python, hash sayesinde çok hızlı arama yapar. O(1)

# Hashable Ne Demektir:
# Bir obje, değişmezse ve hash'i sabit kalırsa -> Hashable kabul edilir. Yani

# 1 - İmmutable olacak.
# 2 - Hiç değişmeyecek.
# 3 - hash'i hep aynı kalacak.

# DİKKAT!!! Bir tuple'ın hashlenebilmesi için içindeki her elemanın da hashable (genelde immutable) olması gerekir.
# Frozenset de hashable'dır, bu yüzden içindeki elemanların da hashable olması gerekir.

#-----------------EŞİTLİK-(==)-ile-KİMLİK-(is)-FARKI----------------

# == -> Değerler eşit mi diye kontrol eder.
# is -> RAM'deki adresleri aynı mı diye kontrol eder.

# Hash ile Equality nasıl bağlıdır:
# KURAL: Eğer iki obje == ile eşitse, hash'leri de aynı olmalıdır. Yani

a == b              # True olduğunda 
hash(a) == hash(b)  # True olmalıdır. Çünkü işlemler şu şekilde çalışır:

# 1 - Anahtarın hash'ini hesapla.
# 2 - Hash tablosunda o bölgeyi bul.
# 3 - Aynı hash'te bir obje varsa == ile karşılaştır.
# 4 - Eşitse -> buldu.
# 5 - Eşit değilse -> aynı hash ama farklı değer. Collision.

#-------------CUSTOM-CLASSLARDA-eq-ve-hash-İLİŞKİSİ-------------

# Eğer bir sınıfın eşitlik kurallarını (==) değiştiriyorsan, hash kurallarınıda değiştirmen gerekir.

# Çünkü set ve dict anahtarları karşılaştırılırken hem hash hemde equality kullanır.

class User:
    def __init__(self, id):
        self.id = id
    
    def __eq__(self, other):            # Bu şekilde kullanılırsa sonuç şu şekilde olur:
        return self.id == other.id      
    
u1 = User(1)                            
u2 = User(1)

u1 == u2    # True -> Çünkü objeler aynı. Ama hash'leri yok. Sadece == metodunu override ettik. Yani python bunları UNHASHABLE yapar.
            # Bu şekilde kullanmak objelerini dict ve set içerisinde kullanamamanı sağlar. Bu sorunu çözmek içinse

def __hash__(self):         # Buradaki metodunda class içerisinde tanımlanmış olması gerekir.
    return hash(self.id)    # Çünkü bu tanımlanmazsa python güvenlik açısından sınıfları UNHASHABLE yapar.

#--------------------DICT-KEYLERİ-NEDEN-İMMUTABLE-OLMAK-ZORUNDA-------------------

# Eğer bir dict'in key'i mutable olsaydı.

a = [1,2,3]
dictt = {a: "kutay"}

a.append(4)     # Bu satır çalıştığı anda listeyi dict'teki "kutay" değerini kaybederdik.
                # Çünkü bu listeyi değiştirdi. Değişen liste hash değiştirdi. Ama "kutay" eski hash tablosundaki yerinde kaldı.
                # Bir daha "kutay" değerine erişemeyeceğiz.

# Bundan sebep dict key'leri immutable olmak zorundadır.

#-------------------GUN-1-TAMAMLANDI-------------------
#-----ISLAM-KUTAY-SAHIN-----------------24/11/2025-----