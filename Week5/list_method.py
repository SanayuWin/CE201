# len(): หาจำนวนสมาชิกใน List
my_list = [10, 20, 30, 40]
print(f"จำนวนสมาชิกใน my_list: {len(my_list)}") # Output: 4

# append(): เพิ่มสมาชิกใหม่ที่ท้าย List
fruits = ["apple", "banana"]
fruits.append("orange")
print(f"List หลัง append: {fruits}") # Output: ['apple', 'banana', 'orange']

# insert(): เพิ่มสมาชิกที่ตำแหน่ง (Index) ที่ต้องการ
fruits = ["apple", "orange"]
fruits.insert(1, "grape") # เพิ่ม 'grape' ที่ Index 1
print(f"List หลัง insert: {fruits}") # Output: ['apple', 'grape', 'orange']

# remove(): ลบสมาชิกตัวแรกที่ตรงกับค่าที่ระบุ
my_numbers = [1, 2, 3, 2, 4]
my_numbers.remove(2) # ลบเลข 2 ตัวแรก
print(f"List หลัง remove 2: {my_numbers}") # Output: [1, 3, 2, 4]

# my_numbers.remove(5) # Uncomment เพื่อดู ValueError

# pop(): ลบสมาชิกที่ Index ที่ระบุ และส่งค่าสมาชิกนั้นกลับมา
fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop(1) # ลบ 'banana' (Index 1)
print(f"ผลไม้ที่ถูกลบออก: {removed_fruit}") # Output: banana
print(f"List หลัง pop Index 1: {fruits}") # Output: ['apple', 'cherry']

last_fruit = fruits.pop() # ลบตัวสุดท้าย ('cherry')
print(f"ผลไม้ตัวสุดท้ายที่ถูกลบ: {last_fruit}") # Output: cherry
print(f"List หลัง pop ตัวสุดท้าย: {fruits}") # Output: ['apple']

# del Statement: ลบสมาชิกด้วย Index หรือลบทั้ง List
my_list = [10, 20, 30, 40, 50]
del my_list[2] # ลบสมาชิกที่ Index 2 (ค่า 30)
print(f"List หลัง del index 2: {my_list}") # Output: [10, 20, 40, 50]

# del my_list # ลบตัวแปร my_list ทั้งหมดออกจาก memory
# print(my_list) # จะเกิด NameError เพราะ my_list ไม่มีอยู่แล้ว


# clear(): ลบสมาชิกทั้งหมดใน List แต่ยังคง List ว่างไว้
my_list = [1, 2, 3]
my_list.clear()
print(f"List หลัง clear: {my_list}") # Output: []


# count(): นับจำนวนสมาชิกที่มีค่าเท่ากับที่ระบุ
numbers = [1, 2, 2, 3, 2, 4, 5]
print(f"จำนวนเลข 2 ใน List: {numbers.count(2)}") # Output: 3


# index(): ค้นหา Index ของสมาชิกตัวแรกที่ตรงกับค่าที่ระบุ
fruits = ["apple", "banana", "cherry"]
print(f"Index ของ 'banana': {fruits.index('banana')}") # Output: 1

# print(fruits.index("grape")) # Uncomment เพื่อดู ValueError


# sort() / sorted(): จัดเรียงข้อมูลใน List
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(f"List ตัวเลขหลัง sort(): {numbers}") # Output: [1, 2, 5, 8, 9]

fruits = ["cherry", "apple", "banana"]
fruits.sort()
print(f"List ผลไม้หลัง sort(): {fruits}") # Output: ['apple', 'banana', 'cherry']

# เรียงจากมากไปน้อย (descending)
numbers.sort(reverse=True)
print(f"List ตัวเลขหลัง sort(reverse=True): {numbers}") # Output: [9, 8, 5, 2, 1]