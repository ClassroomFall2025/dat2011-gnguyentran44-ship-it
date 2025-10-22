import os

# Nhập tên file CSV
filename = input("Nhập tên file .csv: ")

# Kiểm tra file có tồn tại không
file_exists = os.path.exists(filename)

# Mở file: nếu chưa có thì tạo mới ('w'), nếu có thì ghi thêm ('a')
mode = "a" if file_exists else "w"

with open(filename, mode, encoding="utf-8") as f:
    # Nếu file chưa tồn tại -> ghi tiêu đề (header)
    if not file_exists:
        f.write("MSSV,Họ tên,Lớp,Năm sinh,Điểm trung bình\n")

    # Nhập số lượng sinh viên mới
    n = int(input("Nhập số lượng sinh viên cần ghi thêm: "))

    # Ghi từng sinh viên vào file
    for i in range(n):
        print(f"\n--- Sinh viên thứ {i+1} ---")
        mssv = input("MSSV: ")
        hoten = input("Họ tên: ")
        lop = input("Lớp: ")
        namsinh = input("Năm sinh: ")
        diem = input("Điểm trung bình: ")

        # Ghi một dòng CSV bằng f-string
        line = f"{mssv},{hoten},{lop},{namsinh},{diem}\n"
        f.write(line)

print(f"\n Đã ghi {n} sinh viên vào file '{filename}' thành công!")

