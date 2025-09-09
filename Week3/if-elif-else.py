score = int(input("กรุณาป้อนคะแนน (0-100): "))

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print(f"คุณได้เกรด: {grade}")


if <เงื่อนไข 1>:
    # ทำเมื่อเงื่อนไข 1 เป็นจริง
elif <เงื่อนไข 2>:
    # ทำเมื่อเงื่อนไข 1 เป็นเท็จ และเงื่อนไข 2 เป็นจริง
elif <เงื่อนไข 3>:
    # ทำเมื่อเงื่อนไข 1 และ 2 เป็นเท็จ และเงื่อนไข 3 เป็นจริง
else:
    # ทำเมื่อไม่มีเงื่อนไขใดๆ ข้างบนเป็นจริงเลย


a = 2
if a == 2:
    a = 3
elif a == 3:
    a = 4
print(a)

a = 2
if a == 2:
    a = 3
if a == 3:
    a = 4
print(a)


