# workshop_2.py
fruits = ["apple", "banana", "cherry"]
print(f"List ผลไม้เริ่มต้น: {fruits}")

fruits.append("orange")
print(f"หลังเพิ่ม 'orange': {fruits}")

fruits.insert(1, "grape") # เพิ่ม 'grape' ที่ Index 1
print(f"หลังเพิ่ม 'grape' ที่ Index 1: {fruits}")

fruits.remove("banana")
print(f"หลังลบ 'banana': {fruits}")