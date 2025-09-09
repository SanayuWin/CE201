# กำหนดค่าที่ถูกต้องไว้ในตัวแปร
correct_username = "admin"
correct_password = "pass1234"

# รับค่าจากผู้ใช้
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

# ใช้ 'and' เพื่อตรวจสอบว่าต้องเป็นจริงทั้งสองเงื่อนไข
if entered_username == correct_username and entered_password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password.")