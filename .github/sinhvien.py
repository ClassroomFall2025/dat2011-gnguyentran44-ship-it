def them_sinh_vien():
    print(">>> Chức năng: Thêm sinh viên")

def xoa_sinh_vien():
    print(">>> Chức năng: Xóa sinh viên")

def cap_nhat_sinh_vien():
    print(">>> Chức năng: Cập nhật sinh viên")

def xem_danh_sach():
    print(">>> Chức năng: Xem danh sách sinh viên")

def thoat():
    print(">>> Thoát chương trình")

# Menu chính
def menu():
    while True:
        print("\n====== HỆ THỐNG QUẢN LÝ SINH VIÊN ======")
        print("1. Thêm sinh viên")
        print("2. Xóa sinh viên")
        print("3. Cập nhật sinh viên")
        print("4. Xem danh sách sinh viên")
        print("5. Thoát")
        
        chon = input("Nhập lựa chọn (1-5): ")
        
        if chon == "1":
            them_sinh_vien()
        elif chon == "2":
            xoa_sinh_vien()
        elif chon == "3":
            cap_nhat_sinh_vien()
        elif chon == "4":
            xem_danh_sach()
        elif chon == "5":
            thoat()
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại!")

# Chạy menu
menu()
