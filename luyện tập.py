import csv
import os

filename = input("Nhập tên file .csv: ")

# Kiểm tra file có tồn tại chưa
file_exists = os.path.exists(filename)

# Dữ liệu mẫu
brands = ("Toyota", "Honda", "Mazda", "Hyundai", "KIA")
models = ("Vios", "City", "CX5", "Santafe", "Morning")
years = (2016, 2017, 2018, 2019, 2020)
colors = ("red", "orange", "yellow", "green", "blue")

# Mở file ở chế độ ghi nối thêm (append)
with open(filename, mode="a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    # Nếu file mới (chưa tồn tại) thì ghi header
    if not file_exists:
        writer.writerow(["Brand", "Model", "Year", "Color"])

    # Ghi từng dòng dữ liệu
    for x in range(5):
        writer.writerow([brands[x], models[x], years[x], colors[x]])

print(" Tạo file dữ liệu thành công!")
# xuát thông tin
with open(filename, "r", encoding="utf-8") as f2:
    print(f2.read())
    # đọc file csv
    with open(filename, "r", endording="utf-8")as f3:
        reader = csv.reader(f3)
        for row in reader:
            print(row)
           
    