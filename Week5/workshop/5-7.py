# workshop_7.py
numbers = [15, 22, 30, 41, 55, 60, 78]
even_numbers = []

for num in numbers:
    if num % 2 == 0: # ตรวจสอบว่าเป็นเลขคู่หรือไม่ (หาร 2 ลงตัว เศษเป็น 0)
        even_numbers.append(num)

print(f"List ตัวเลขทั้งหมด: {numbers}")
print(f"List เลขคู่: {even_numbers}")