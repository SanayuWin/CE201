# รับค่าอาหารและเปอร์เซ็นต์ทิป
total_bill = float(input("ยอดรวมค่าอาหาร: "))
tip_percentage = float(input("ต้องการให้ทิปกี่เปอร์เซ็นต์: "))

# คำนวณจำนวนเงินทิป
tip_amount = total_bill * (tip_percentage / 100)

# คำนวณยอดรวมที่ต้องจ่าย
final_payment = total_bill + tip_amount

# แสดงผล
print(f"จำนวนเงินทิป: {tip_amount} บาท")
print(f"ยอดรวมที่ต้องจ่ายทั้งหมด: {final_payment} บาท")