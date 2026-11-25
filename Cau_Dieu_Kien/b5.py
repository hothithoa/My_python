nam_sinh = int(input("Nhập năm sinh: "))
if 1946 <= nam_sinh <= 1964:
    print("Gen baby boomers")
elif 1965 <= nam_sinh <= 1980:
    print("Gen X")
elif 1981 <= nam_sinh <= 1996:
    print("Gen Y")
elif 1997 <= nam_sinh <= 2012:
    print("Gen Z")
elif 2010 <= nam_sinh <= 2024:
    print("Gen Alpha")  
else:
    print("Gen Beta")          