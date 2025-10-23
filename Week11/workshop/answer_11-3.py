"""
เฉลย Workshop 11-4: Tkinter - เครื่องคิดเลขง่ายๆ
"""
import tkinter as tk

def calculate(operation):
    """ฟังก์ชันสำหรับคำนวณตามการดำเนินการที่เลือก"""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                label_result.config(text="ข้อผิดพลาด! ไม่สามารถหารด้วย 0 ได้")
                return
            result = num1 / num2
        
        label_result.config(text=f"ผลลัพธ์: {result}")
        
    except ValueError:
        label_result.config(text="ข้อผิดพลาด! กรุณากรอกตัวเลข")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("เครื่องคิดเลข")
root.geometry("300x250")

# Label และ Entry สำหรับตัวเลขที่ 1
tk.Label(root, text="ตัวเลขที่ 1:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Label และ Entry สำหรับตัวเลขที่ 2
tk.Label(root, text="ตัวเลขที่ 2:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Frame สำหรับปุ่มต่างๆ
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# สร้างปุ่มทั้ง 4 ปุ่ม
tk.Button(button_frame, text="บวก (+)", command=lambda: calculate("add"), width=8).grid(row=0, column=0, padx=2)
tk.Button(button_frame, text="ลบ (-)", command=lambda: calculate("subtract"), width=8).grid(row=0, column=1, padx=2)
tk.Button(button_frame, text="คูณ (×)", command=lambda: calculate("multiply"), width=8).grid(row=1, column=0, padx=2, pady=5)
tk.Button(button_frame, text="หาร (÷)", command=lambda: calculate("divide"), width=8).grid(row=1, column=1, padx=2, pady=5)

# Label สำหรับแสดงผลลัพธ์
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()
