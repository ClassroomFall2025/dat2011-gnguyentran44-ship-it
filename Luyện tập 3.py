import csv

students = []
n = int(input("Nhập số lượng sinh viên: "))

for i in range(n):
    print(f"\n--- Sinh viên {i+1} ---")
    mssv = input("MSSV: ")
    name = input("Họ tên: ")
    cls = input("Lớp: ")
    score = float(input("Điểm trung bình: "))
    students.append({"MSSV": mssv, "Họ tên": name, "Lớp": cls, "Điểm": score})

# Sau khi nhập xong mới ghi ra file
with open("sinhvien.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["MSSV", "Họ tên", "Lớp", "Điểm"])
    writer.writeheader()
    writer.writerows(students)

print(" Đã lưu danh sách sinh viên vào file CSV thành công!")