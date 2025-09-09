# workshop_6.py
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

search_name = input("กรอกชื่อนักเรียนที่ต้องการค้นหา: ")

if search_name in students:
    print(f"พบนักเรียนชื่อ '{search_name}' ในระบบ")
    # โจทย์เสริม: หากพบ ให้พิมพ์ Index
    student_index = students.index(search_name)
    print(f"อยู่ในลำดับที่ (Index): {student_index}")
else:
    print(f"ไม่พบนักเรียนชื่อ '{search_name}' ในระบบ")