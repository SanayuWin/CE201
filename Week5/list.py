# สร้าง List ว่าง (Empty List):
my_empty_list = []
print(f"List ว่าง: {my_empty_list}") # Output: List ว่าง: []
print(f"ชนิดข้อมูลของ my_empty_list: {type(my_empty_list)}") 
# Output: ชนิดข้อมูลของ my_empty_list: <class 'list'>


# สร้าง List ที่มีข้อมูลเริ่มต้น:
# List ที่เก็บตัวเลขจำนวนเต็ม
numbers = [10, 20, 30, 40, 50]
print(f"List ตัวเลข: {numbers}") # Output: List ตัวเลข: [10, 20, 30, 40, 50]

# List ที่เก็บข้อความ (Strings)
fruits = ["apple", "banana", "cherry", "date"]
print(f"List ผลไม้: {fruits}") # Output: List ผลไม้: ['apple', 'banana', 'cherry', 'date']

# List ที่เก็บข้อมูลหลากหลายชนิด (mixed data types)
mixed_data = ["Alice", 25, 175.5, True]
print(f"List ข้อมูลผสม: {mixed_data}") # Output: List ข้อมูลผสม: ['Alice', 25, 175.5, True]


# fruits = ["apple", "banana", "cherry", "date"]

fruits = ["apple", "banana", "cherry", "date"]

print(f"ผลไม้ที่ Index 0: {fruits[0]}")  # Output: apple (สมาชิกตัวแรก)
print(f"ผลไม้ที่ Index 2: {fruits[2]}")  # Output: cherry (สมาชิกตัวที่สาม)
print(f"ผลไม้ที่ Index -1: {fruits[-1]}") # Output: date (สมาชิกตัวสุดท้าย)
print(f"ผลไม้ที่ Index -3: {fruits[-3]}") # Output: banana (สมาชิกตัวที่สองนับจากท้าย)

# ถ้าพยายามเข้าถึง Index ที่ไม่มีอยู่ จะเกิดข้อผิดพลาด (IndexError)
# print(fruits[4]) # Uncomment เพื่อดู IndexError: list index out of range



fruits = ["apple", "banana", "cherry", "date"]
print(f"List ก่อนแก้ไข: {fruits}") # Output: ['apple', 'banana', 'cherry', 'date']

# เปลี่ยน 'banana' (Index 1) เป็น 'blueberry'
fruits[1] = "blueberry"
print(f"List หลังแก้ไข Index 1: {fruits}") # Output: ['apple', 'blueberry', 'cherry', 'date']

# เปลี่ยน 'date' (Index 3 หรือ -1) เป็น 'dragonfruit'
fruits[-1] = "dragonfruit"
print(f"List หลังแก้ไข Index -1: {fruits}") # Output: ['apple', 'blueberry', 'cherry', 'dragonfruit']



fruits = ["apple", "banana", "cherry"]
print("รายการผลไม้:")
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


fruits = ["apple", "banana", "cherry"]
print("\nรายการผลไม้พร้อม Index:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry


fruits = ["apple", "banana", "cherry"]
print("\nรายการผลไม้โดยใช้ Index:")
for i in range(len(fruits)): 
# len(fruits) คือ 3 ดังนั้น range(3) จะให้ 0, 1, 2
    print(f"ผลไม้ที่ Index {i}: {fruits[i]}")
# Output:
# ผลไม้ที่ Index 0: apple
# ผลไม้ที่ Index 1: banana
# ผลไม้ที่ Index 2: cherry

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"List เดิม: {my_list}")

# เลือกตั้งแต่ Index 2 (30) จนถึงก่อน Index 5 (ไม่รวม 50)
print(f"my_list[2:5]: {my_list[2:5]}") # Output: [30, 40, 50]

# เลือกตั้งแต่ต้นจนถึงก่อน Index 4 (ไม่รวม 50)
print(f"my_list[:4]: {my_list[:4]}") # Output: [10, 20, 30, 40]

# เลือกตั้งแต่ Index 5 (60) จนถึงท้าย List
print(f"my_list[5:]: {my_list[5:]}") # Output: [60, 70, 80, 90]

# คัดลอกทั้ง List (เป็นการสร้างสำเนาใหม่ ไม่ใช่การอ้างอิงเดิม)
copied_list = my_list[:]
print(f"สำเนาของ List: {copied_list}") # Output: [10, 20, 30, 40, 50, 60, 70, 80, 90]

# เลือกสมาชิกแบบกระโดด (step)
print(f"my_list[::2]: {my_list[::2]}") # Output: [10, 30, 50, 70, 90] (ทุกๆ 2 ตัว)

# เลือกย้อนกลับ (step เป็น -1)
print(f"my_list[::-1]: {my_list[::-1]}") # Output: [90, 80, 70, 60, 50, 40, 30, 20, 10] (ย้อนกลับทั้ง List)


fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("มีกล้วยอยู่ใน List ผลไม้")

if "grape" not in fruits:
    print("ไม่มีองุ่นใน List ผลไม้")
