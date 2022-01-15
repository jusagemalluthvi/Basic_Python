# # #FOR
# # fruits = ["apple", "banana", "cherry"]
# # for fruit in fruits:
# #     print(fruit)

# # x = range(6)
# # for i in x:
# #     print(i)

# # y = range(2,50,3)
# # for a in y:
# #     print(a)


# #WHILE
# # while 2 < 3:
# #     print("Hello, World!")

# i = int(input("mulai dari angka :"))
# while i < 6:
#     print(i)
#     i += 1

# while True:
#     pass -->tidak mengeksekusi apapun

for i in range(5):
    if i == 2 or i == 3 :
        continue
    print(i)

for i in range(5):
    if i == 3 :
        break
    print(i)

#NESTED LOOP
adj_list = ["M                            urah", "Enak", "Bagus"]
fruit_list = ["Mangga", "Salak", "Sawo"]

for i in fruit_list:
    for j in adj_list:
        print(i + " " + j)
