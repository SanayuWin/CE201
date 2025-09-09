# workshop_5.py
expenses = [550, 120, 300, 80, 250]

print("--- รายการค่าใช้จ่าย ---")
total_expenses = 0
for expense in expenses:
    print(f"ค่าใช้จ่าย: {expense} บาท")
    total_expenses += expense # บวกสะสมค่าใช้จ่าย

print(f"-----------------------")
print(f"ผลรวมค่าใช้จ่ายทั้งหมด: {total_expenses} บาท")