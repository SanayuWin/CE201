# โค้ดที่ "ไม่ปลอดภัย" (อาจพังได้)
# age = int(input("กรุณากรอกอายุของคุณ: "))
# print(f"ปีหน้าคุณจะอายุ {age + 1} ปี")
# # ถ้าผู้ใช้พิมพ์ "ยี่สิบ" โปรแกรมจะ Crash!

# # โค้ดที่ "ปลอดภัย" ด้วย try...except
# try:
#     age_input = input("กรุณากรอกอายุของคุณ: ")
#     age = int(age_input)
#     print(f"ปีหน้าคุณจะอายุ {age + 1} ปี")
# except ValueError:
#     print("เกิดข้อผิดพลาด! กรุณาป้อนเป็นตัวเลขเท่านั้น")

# print("โปรแกรมยังคงทำงานต่อได้...")


filename = "my_important_data.txt"

try:
    # พยายามเปิดไฟล์เพื่ออ่าน
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print("--- เนื้อหาไฟล์ ---")
        print(content)

except FileNotFoundError:
    # ถ้าหาไฟล์ไม่เจอ (Error ที่พบบ่อยมาก)
    print(f"ไม่พบไฟล์ที่ชื่อ {filename}!")
    print("กำลังสร้างไฟล์ใหม่ให้แทน...")
    # สร้างไฟล์ใหม่ให้เลย
    with open(filename, "w", encoding="utf-8") as f:
        f.write("ไฟล์นี้ถูกสร้างขึ้นใหม่")
        
except Exception as e:
    # ดักจับ Error อื่นๆ ที่ไม่คาดคิด
    print(f"เกิดข้อผิดพลาดที่ไม่รู้จัก: {e}")


