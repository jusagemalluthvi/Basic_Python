#!/usr/bin/env python
# coding: utf-8

# ## Break

# In[ ]:


# for i in range(5):
#     if i == 3:
#         break
#     print(i)

text = input()

while True:
    if text == "stop" or text == "end":
        print("Program has stopped.")
        break
    print("text: {}".format(text))
    text = input()


# ## Continue

# In[ ]:


# for i in range(5):
#     if i == 1:
#         continue
#     print(i)

for i in range(10):
    if i % 2 == 1:
        continue
    print(i) 


# ## foor_loop

# In[ ]:


nama_buah = ["apel", "jeruk", "mangga", "lemon", "salak"]

# print(nama_buah[0])
# print(nama_buah[1])
# print(nama_buah[2])
# print(nama_buah[3])
# print(nama_buah[4])
# print(len(nama_buah))
# print(nama_buah)

for buah in nama_buah:
    print(buah)

# print("done")


# ## List

# In[ ]:


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(100)
# mylist = []
# mylist.append(1)
# mylist.append(2)
# mylist.append(3)
# mylist.append(100)


# In[ ]:


print(mylist)
print(len(mylist))
print(mylist[3])
# print(mylist)
# print(len(mylist))
# print(mylist[3])


# In[ ]:


mylist2 = []
@@ -16,5 +16,11 @@
print(mylist2)
print(len(mylist2))

for x in mylist:
mylist2.remove("a")
mylist2.remove("b")

print(mylist2)
print(len(mylist2))


# In[ ]:


for x in mylist2:
    print("Value: " + str(x))


# ## Nested loop

# In[ ]:


# for i in range(3):
#     print("i: {}".format(i))
#     for j in range(3):
#         print("j: {}".format(j))

# for baris in range(5):
#     for kolom in range(5):
#         print("{}.{}".format(baris+1,kolom+1), end=" ")
#     print()

count = 1
for baris in range(5):
    for kolom in range(5):
        print(count, end=" ")
        count = count + 1
    print() 


# ## program_for_loop

# In[ ]:


count = int(input("Berapa data: "))

nama_pelanggan = []
umur_pelanggan = []


# In[ ]:


for i in range(count):
    print("Data ke {}".format(i+1))
    nama = input("Nama : ")
    umur = int(input("Umur : "))

    nama_pelanggan.append(nama)
    umur_pelanggan.append(umur)


# In[ ]:


for i in range(len(nama_pelanggan)):
    print("Pelanggan {} berumur {}".format(nama_pelanggan[i], umur_pelanggan[i])) 


# ## Range

# In[ ]:


# for i in range(3):
#     print(i)

# print("----")

# for i in range(1,3):
#     print(i)

# for i in range(2, 20, 3):
#     print(i)

for i in range(1,11):
    print(i)


# ## While

# In[ ]:


i = 1
while i < 6:
    print(i)
    i += 2

print("done")

