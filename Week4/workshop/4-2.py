import random # เรียกใช้โมดูลสำหรับสุ่มตัวเลข

# 1. สุ่มตัวเลข 1-100 แล้วเก็บในตัวแปร
secret_number = random.randint(1, 100)
print("ฉันสุ่มตัวเลขระหว่าง 1-100 ไว้แล้ว ทายให้ถูกสิ!")

# 2. ใช้ while True สร้างลูปที่ไม่รู้จบไปก่อน
while True:
    # รับการทายจากผู้ใช้ (แปลงเป็น int)
    guess = int(input("ทายตัวเลข: "))

    # 3. ตรวจสอบเงื่อนไข
    if guess > secret_number:
        print("น้อยกว่านี้")
    elif guess < secret_number:
        print("มากกว่านี้")
    else: # เงื่อนไขเดียวที่เหลือคือ guess == secret_number
        print(f"ถูกต้อง! เลขปริศนาคือ {secret_number} คุณสุดยอดมาก!")
        break # 5. เมื่อทายถูก ให้ออกจากลูปทันที