# score = input ("")
# mystery = 0

# for chara in score : 
#     if int(chara) == 9 :
#         break
#     if int(chara) % 2 > 0 :
#         continue
#     else: 
#         mystery += int(chara)

# print(mystery)

# n = 5
# output = ""

# for i in range (0, n) :
#     output += str(n)
#     n += 1
# print(output)

# b = "abcd"

# for i in range (0,len(b)) :
#     print(len(b))
#     b = b[i:len(b)]
#     print(b)

# result = 1
# lst = [1,3,5,7]
# for element in lst:
#     print (element)
#     result = result*element
# print (result)

# mylist = ["you", "I", "We"]

# for word in mylist :
#     print("{:>10}".format(word))

# word = "pemrograman"
# word = word.replace ("r","")
# print (word)

# kata = "terang"
# kata = kata[0:1]
# print (kata)


# list = [1,2,3]
# for i in range (0,10) :
#     list[i] = i
# print(list)

# res = [[x,y] for x in range(0,5,2) for y in range(0,5,2)]
# print(res)

# n = int(input('Masukkan nilai N: '))
# index = 0
# while index < n and n > 2 and n < 10:
#     empty_space_list = [' '] * n
#     empty_space_list[index] = 'x'
#     empty_space_list[-(index + 1)] = 'x'
#     index += 1
#     print(''.join(empty_space_list))

# def maks_ganjil(lst):
#     m = None
#     for e in lst:
#         if e % 2 and m == None :
#             m = e
#         elif e % 2 and e > m :
#             m = e
#     print (m)
#     return m

# print (maks_ganjil([5,8]))

# def berstemmer(kalimat):
#     stem_kalimat = ''
#     for word in kalimat.split(" "):
#         if word[:3].lower() == 'ber':
#             word = word[3:]
#         elif word[:2].lower() == 'be':
#             word = word[2:]
#         stem_kalimat = stem_kalimat + word + ' '
#     return stem_kalimat
# kalimat = "ayah pergi bekerja"
# print (f"{berstemmer(kalimat):>40}")

# def input_integer() :
#     global x
#     global y
#     y = input("Masukkan nilai:")
#     x = True
#     while x == True:
#         try:
#             y = int(y)
#             print(y)
#             x = False
#         except :
#             y = input("Masukkan nilai:")
# input_integer()

# for i,ch in enumerate("hello world") :
#     print (i,ch)

# def gabung(lst, delimiter) :
#     str_result = ""
#     for element in lst:
#         str_result = str_result + str(element) + str(delimiter)
#     print (str_result)

# gabung([1,2,3], 5)

# input = input ("kalimat")

# line = input.split(" ")
# for i in range (len(line)) :
#     x = line[i]
#     if "," in x :
#         x = x.replace(",","")
#     if "mu" in x[-2:] :
#         print (x)
#     elif "ku" in x[-2:] :
#         print (x)
#     elif "nya" in x[-3:] :
#         print (x)
#     else :
#         pass

# x = [1,2,3]
# y = [1,2,3]
# y.append (x)
# z = []
# z = x + y
# x.insert (0,5)
# y.insert (0,5)
# print(z)

# for i in range(9) :
#     if i == 3 :
#         continue
#     print(i)

# set = {'a','b','c'}
# set.update (set)
# set.add (5)
# set.discard (10)
# print (set)

# set_a = {1,2}
# set_b = set_a.copy()
# set_b.add (3)
# print(set_a, set_b)

# set = {ch for ch in "to be or not to be"}
# print(sorted(set))

# dict = {'satu':1, 'dua':2}
# dict_2 = {}
# dict_2 = dict.copy()
# print(dict['satu'])
# dict['satu'] = 10
# print(dict['satu'])
# for key in dict:
#     print(key, dict[key])
# print(dict, dict_2)
# #bisa dictionary dalam dictionary
 
# list =[1,2,3]
# def panjang_list (list):
#     if list == []:
#         return 0
#     return 1 + panjang_list [1:]

# x = 55
# y = 25
# for i in range (x,1,-1):
#     if x % i == 0 and y % i == 0 :
#         print (i)

# def rvs (str) :
#     print (str[::-1])
# rvs("abcd")

# def max (x,y):
#     if x > y:
#         return x
#     return y
# def find (a):
#     if len(a) == 1:
#         return a[0]
#     return max (a[0],find(a[1:]))
# a = [1,2,3,4,5]
# print(find(a))

# def tower(disk, awal, akhir, perantara):
#     if disk == 1 :
#         print(f"Pindahkan dari {awal} ke {akhir}")
#     else:
#         tower(disk-1, awal, perantara, akhir)
#         print(f"Pindahkan dari {awal} ke {akhir}")
#         tower(disk-1, perantara, akhir, awal)

# tower(3,"A","B","C")

# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n-1) + fibonacci (n-2)
# print(fibonacci(36))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# S = {-13,-7,0,7,13}
# def f(x):
#     print(x)
#     x = x**3//13
#     print(x)
# for element in S:
#     f(element)

# class customer () :
#     def __init__ (entry, email = "", phone = ""):
#         entry.email = email
#         entry.phone = phone
#     def email (entry, email = "") :
#         entry.email = email
#     def phone (entry, phone = "") :
#         entry.phone = phone
#     def order (entry, place = "", cancel = ""):
#         entry.place = place
#         entry.cancel = cancel
#     def place (entry, place = ""):
#         entry.place = place
#     def cancel (entry, cancel = ""):
#         entry.cancel = cancel
#     def __str__(entry) :
#         return f"{entry.email}@company.com {entry.phone}"
# customer1 = customer("Lara", "12345" )
# customer2 = customer("Tess", "67890")
# customer3 = customer("Dave", "151011")

# print (customer1)
# print (customer2)
# print (customer3)

# total =0
# for number in range (1,10) :
#     if number%2  and not number%3 :
#         print(number)
#         total += number
#     else : 
#         pass
# print (total)

# class Book(object): 
#     def __init__(self, title, price):
#         self.__title = title
#         self.__price = price
        
#     def get_title(self):
#         return ______________ # 1 point
        
#     def get_price(self):
#         return ______________ # 1 point

# class Cart(object):
#     def __init__(self):
#         self.__shopping_cart = []
        
#     def add_item(self, item):
#         """ menambahkan sebuah item di posisi akhir list shopping cart """
#         _________________________ # 3 point

#     def total_price(self):
#         """ melakukan loop terhadap shopping cart, dan menghitung total harga """
#         _________________________ # 5 point

# if __name__ == '__main__':
        
#     my_cart = Cart()
    
#     my_cart.add_item(Book("Python", 50000))
#     my_cart.add_item(Book("Java", 30000))
#     my_cart.add_item(Book("Data Mining", 45000))
#     my_cart.add_item(Book("Clean Code", 70000))
#     my_cart.add_item(Book("Effective Programming", 70000))
        
#     print("total price = {}".format(my_cart.total_price()))

# class Nama:
#     def __init__(self, nama, NPM):
#         self.nama = nama
#         self.NPM = NPM
# nama = Nama("C", 123)
# print (nama.__class__)

# circle.py

# class Mobil :
#     roda = 4
#     def __init__(self, merk, seri, warna) :
#         self.merk = merk
#         self.seri = seri
#         self.warna = warna
#     def __str__(self) :
#         return "merk: "  + self.merk + " seri :" + self.seri + "warna : " + self.warna
#     def __del__(self) :
#         print("merk: "  + self.merk + " seri :" + self.seri + "warna : " + self.warna + "dihapus")
# m1 = Mobil("Toyota", "Avanza", "hitam")
# m2 = Mobil("Honda", "Jazz", "kuning")

# print (m1)
# print (m2)
# del m1

# class Myclass :
#     def __init__(self) :
#         self.my_public_attr = "Public"
#         self.__my_private_attr = "private"
#     def print_private(self) :
#         print (self.__my_private_attr)
# obj = Myclass()
# print (obj.my_public_attr)
# obj.print_private()

# class Newclass(object):
#     def __init__(self, param_int=1) :
#         self.the_int = param_int
#         if param_int%2 == 0:
#             self.parity = 'even'
#         else : 
#             self.parity = 'odd'
#     def process(self,instance ) :
#         sum_int = self.the_int + instance.the_int
#         if sum_int < 0 :
#             return "negative"
#         elif sum_int % 2 ==0 :
#             return 'even'
#         else : 
#             return 'odd'
#     def __str__(self) :
#         return 'Value {} is {}'.format(self.the_int, self.parity)

# inst1 = Newclass (4)
# inst2 = Newclass (-5)
# inst3 = Newclass ()
# print (inst3.process(inst1))

# class Animal():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(self.name ," is eating...")

# class Cat(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed
#     def meow(self):
#         print(self.name, " is meowing...")

# class Bird(Animal):
#     def __init__(self, name, age, feather_color):
#         super().__init__(name, age)
#         self.feather_color = feather_color
#     def flies(self):
#         print(self.name, " is flying...")
#     def flight(self):
#         print("Most of the birds can fly but some cannot.") 
# class Sparrow (Bird) :
#     def flight(self):
#         print ("Sparrows can fly")
# class Ostrich (Bird) :
#     def flight(self):
#         print ("Ostrich cannot fly")
# burung = Ostrich("Peacock", 10, "Rainbow")
# cat = Cat("Kucing oren", 10, "Husky")
# cat.meow()
# burung.flies()
# burung.flight()

# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return "({},{})".format(self.x, self.y)
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)
# p1 = Point(1, 2)
# p2 = Point(2, 3)
# print(p1 + p2)

# class Parent(object) :
#     atr_b = "world"
#     atr_c = "Mundo"
#     def __init__(self, atr_a) :
#         self.atr_a = atr_a
#     def __str__(self):
#         return self.atr_a + " " + self.atr_b
# class Child (Parent) :
#     atr_a = "dunia"
#     def set_atr_b (self, atr_b) :
#         self.atr_b = atr_b
        

# c = Child ("monde")
# c.set_atr_b ("wereld")
# print(c)

# class Person (object) :
#     def __get_info (self) :
#         return "person"
#     def print_person (self) :
#         print(self.__get_info())

# class Student(Person) :
#     def __get_info(self):
#         return "student"
# person = Person()
# person.print_person()
# student = Student()
# student.print_person()

# list_check = []
# def is_exist (nomor, list1):
#     for element in list1 :
#         if nomor == element :
#             list_check.append(1)
#         elif isinstance (element, list) :
#             is_exist (nomor, element)
#         else : 
#             list_check.append(0)
# is_exist (4, [3,[2],[[],[]],[1,[5]]])
# jumlah = list_check.count(1)
# if jumlah == 0 :
#     print("False")
# else :
#     print("True")

# list1 = ([('rudi', 'elmo'), ('elmo', 'hakimi'), ('elmo', 'rudi'), ('hakimi', 'elmo')])
# dict_nama = {}
# def saling_follow (list1) :
#     total = 0
#     for element in list1 :
#         nama,nama_1 = element
#         if nama in dict_nama :
#             dict_nama[nama].append(nama_1)
#         else :
#             dict_nama[nama] = [nama_1]
#         try :
#             for element in dict_nama[nama_1] :
#                 if nama == element :
#                     total += 1
#         except KeyError:
#             pass
#     print(total)
# saling_follow(list1)

# class Book(object):
#     def __init__(self, title, price):
#         self.__title = title
#         self.__price = price
#     def get_title(self):
#         return self.__title # 1 point
#     def get_price(self):
#         return self.__price # 1 point

# class Cart(object):
#     def __init__(self):
#         self.__shopping_cart = []
#     def add_item(self, item):
#         self.__shopping_cart.append(item)
#     def total_price(self):
#         total = 0
#         for barang in self.__shopping_cart :
#             total += barang.get_price()
#         return total
# if __name__ == '__main__':
#     my_cart = Cart()
#     my_cart.add_item(Book("Python", 50000))
#     my_cart.add_item(Book("Java", 30000))
#     my_cart.add_item(Book("Data Mining", 45000))
#     my_cart.add_item(Book("Clean Code", 70000))
#     my_cart.add_item(Book("Effective Programming", 70000))
#     print("total price = {}".format(my_cart.total_price()))

# num_sinonim = int(input("banyaknya pasangan sinonim: "))
# dict_sinonim = {}
# for i in range(num_sinonim):
#     first, second = input().split()
#     dict_sinonim[first] = second
#     dict_sinonim[second] = first
# print()
# word = input("kata yang ingin dicari sinonimnya: ")
# print (dict_sinonim[word])

# import math
# class Vector5(list):
#     jumlah_vector = 0 # a class variable
#     def __init__(self, data = 5*[0]):
#         super().__init__(data)
#         Vector5.jumlah_vector += 1
#     def __str__(self):
#         return f"<{self[0]},{self[1]},{self[2]},{self[3]},{self[4]}>"
#     def __add__(self, param):
#         data = 5*[0]
#         if type(param) == Vector5:
#             for i in range(5):
#                 data[i] = self[i] + param[i]
#             return Vector5(data)
#         else:
#             raise(TypeError)
#     def __sub__(self, param):
#         data = 5*[0]
#         if type(param) == Vector5:
#             for i in range(5):
#                 data[i] = self[i] - param[i]
#             return Vector5(data)
#         else:
#             raise(TypeError)
#     def __mul__(self, param ):
#         data = 5*[0]
#         total = 0
#         if type(param) == Vector5 :
#             for i in range (5) :
#                 data[i] = self[i] * param[i]
#             for element in data :
#                 total += element
#             return total
#         else:
#             raise(TypeError)
    
#     def norm(self):
#         return math.sqrt(self * self)

# def main():
#     v1 = Vector5([1,1,3,2,7])
#     v2 = Vector5([1,0,1,0,-1])
#     v3 = v1 + v2
#     v4 = v1 - v2
#     print(len(v1)) # 5, len() bisa diterapkan karena "Vector5 is a list"
#     print(v1[2]) # 3, indexing bisa diterapkan karena "Vector5 is a list"
#     print(v3) # <2,1,4,2,6>
#     print(v4) # <0,1,2,2,8>
#     print(v1 * v2) # -3
#     print(v1.norm()) # 8.0
#     print(Vector5.jumlah_vector) # 4
# if __name__ == '__main__':
#     main()

# class BankAccount(object):
#     def __init__(self, balance):
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#     def deposit(self, amount):
#         self.__balance += amount
        
#     def withdraw(self, amount):
#         self.__balance -= amount
        
#     def transfer(self, other_account, amount):
#         self.withdraw(amount)
#         other_account.deposit(amount)

#     def __str__(self):
#         return "amount of money = {}".format(self.get_balance())
    
# if __name__ == '__main__':
#     my_account = BankAccount(50000)
#     your_account = BankAccount(100000)
#     print(my_account) # amount of money = 50000
#     print(your_account.get_balance()) # 100000
#     your_account.deposit(4000)
#     print(your_account) # amount of money = 104000
#     my_account.transfer(your_account, 20000)
#     print(my_account) # amount of money = 30000
#     print(your_account) # amount of money = 124000

# def f_rec(s) :
#     if not s :
#         return s
#     elif len(s) == 1:
#         return s
#     else:
#         if s[0] == s[-1] :
#             return s[0] + f_rec(s[1:-1]) + s[-1]
#         else :
#             return f_rec(s[1:-1])

# print (f_rec("aba"))