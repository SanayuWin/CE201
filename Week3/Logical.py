age = 25
money = 100

# and: ต้องเป็นจริงทั้งคู่
can_watch_movie = (age >= 18) and (money >= 150)
print(f"อายุ 25, เงิน 100, ดูหนังได้ไหม? : {can_watch_movie}") # ผลลัพธ์: False (เพราะเงินไม่พอ)

# or: เป็นจริงอย่างใดอย่างหนึ่ง
can_get_discount = (age < 12) or (age > 60)
print(f"อายุ 25, ได้รับส่วนลดไหม? : {can_get_discount}") # ผลลัพธ์: False (เพราะไม่อยู่ในเงื่อนไข)

# not: กลับค่า
is_active = True
is_banned = not is_active
print(f"สถานะ Active คือ {is_active}, โดนแบนไหม? : {is_banned}") # ผลลัพธ์: False

