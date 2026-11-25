#Thông tin của bạn
name = "Thuy"
age = 20
city = "Da Nang"
#In thông tin của bạn bằng

#C1: Định dạng f-string
print(f"Xin chao, toi ten la {name}, nam nay toi {age} tuoi va song o {city}.")

#C2: Định dạng format
print("Xin chao, ten toi la {}, nam nay toi {} tuoi va song o {}.".format(name,age,city))

#Bài 2
#Chiều dài và chiều rộng hình chữ nhật
chieu_dai = 10.8
chieu_rong = 5.7
#Tính chu vi và diện tích
chu_vi = (chieu_dai + chieu_rong)*2
dien_tich = chieu_dai*chieu_rong
#In kết quả chu vi và diện tích

print(f"Chu vi hinh chu nhat:{chu_vi}")
print(f"Dien tich hinh chu nhat:{dien_tich}")

print(f"Chu vi hinh chu nhat:{chu_vi:.2f}")
print(f"Dien tich hinh chu nhat:{dien_tich:.2f}")