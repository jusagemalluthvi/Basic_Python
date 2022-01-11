#!/usr/bin/env python
# coding: utf-8

# ## Boolean

# In[ ]:


print(10 > 9)
print(10 == 9)
print(10 < 9)


# ## Casting

# In[ ]:


# float to int
x = 1.9999999
print(x)
print(type(x))

y = int(x)
print(y)
print(type(y))


# In[ ]:


# int to float
a = 100
print(a)
print(type(a))

b = float(a)
print(b)
print(type(b))


# In[ ]:


# str to float
x = "4.5"
print(x)
print(type(x))

y = float(x)
print(y)
print(type(y))


# In[ ]:


# float to str
a = 9.9
print(a)
print(type(a))

b = str(a)
print(b)
print(type(b))


# ## Conditions

# In[1]:


a = 10
b = 11


# In[ ]:


if a > b:
    print("a lebih besar dari b")
elif a == b:
    print("a sama dengan b")
else:
    print("a lebih kecil dari b")

print(True and True)
print(True and False)
print(True or False)
print(not True)
print(not False)


# ## Datatypes

# In[ ]:


string = 'Ini ada string'
print(string)
print(type(string))


# In[ ]:


integer = 100
print(integer)
print(type(integer))


# In[ ]:


angka_desimal = 101.1
print(angka_desimal)
print(type(angka_desimal))


# In[ ]:


boolean = False
print(boolean)
print(type(boolean))


# ## Input

# In[ ]:


nama = input("Masukkan nama: ")
print(type(nama))
print("Your name is " + nama)


# ## List

# In[ ]:


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(100)

print(mylist)
print(len(mylist))
print(mylist[3])


# In[ ]:


mylist2 = []
mylist2.append("a")
mylist2.append("b")

print(mylist2)
print(len(mylist2))


# In[ ]:


for x in mylist:
    print("Value: " + str(x))


# ## Math

# In[ ]:


x = 5
y = 3


# In[ ]:


# Tambah
print(x + y)


# In[ ]:


# Kurang 
print(x - y)


# In[ ]:


# Kali
print(x * y)


# In[ ]:


# Bagi (float)
print(x / y)


# In[ ]:


# Bagi (int)
print(x // y)


# In[ ]:


# Modulo
print(x % y)


# In[ ]:


# Pangkat
print(x ** y)


# ## String

# In[ ]:


a = "Hello, World!"
print(a[4])


# In[ ]:


print(a[0:5])


# In[ ]:


print(a[1:])


# In[ ]:


print(a[-6:])


# In[ ]:


# Panjang string
print(len(a))


# In[ ]:


halo = "halo"
b = a + " " + halo
print(b) 


# ## String Formatting

# In[ ]:


nama = input("Masukkan nama: ")
age = 23
text = "Nama saya {}, dan saya {} tahun".format(nama, age)


# In[ ]:


print(text)


# ## Variabel

# In[ ]:


angka = 10
angka = 15
y = "Hello, Farhan!"


# In[ ]:


print(angka)
print(y)

