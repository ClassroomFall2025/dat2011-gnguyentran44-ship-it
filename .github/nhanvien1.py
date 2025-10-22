class NhanVien:
    def __init__(self, ho_ten_nv, luong_cb, so_gio_lam):
        self.ho_ten_nv = ho_ten_nv
        self.luong_cb = luong_cb
        self.so_gio_lam = so_gio_lam

        class TiepThi(NhanVien):
            def __init__(self, ho_ten_nv, luong_cb, so_gio_lam, doanh_so, hoa_hong):
                super().__init__(ho_ten_nv, luong_cb, so_gio_lam)
                self.doanh_so = doanh_so
                self.hoa_hong = hoa_hong
            def tinh_luong(self):
                return self.luong_cb + (self.doanh_so * self.hoa_hong)
            def hien_thi_thong_tin(self):
                return f"ho_ten_sv la {self.ho_ten_nv}", f"luong_cb la {self.luong_cb}", f"so_gio_lam la {self.so_gio_lam}"
            class Truongphong(NhanVien):
                def __init__(self, ho_ten_nv, luong_cb, so_gio_lam, phu_cap):
                    super().__init__(ho_ten_nv=ho_ten_nv, luong_cb=luong_cb, so_gio_lam=so_gio_lam)
                    self.phu_cap =phu_cap
                    def tinh_luong(self):
                        return self.luong_cb + self.phu_cap
                    def hien_thi_thong_tin(self):
                        return f"ho_ten_sv la {self.ho_ten_nv}", f"luong_cb la {self.luong_cb}", f"so_gio_lam la {self.so_gio_lam}", f"phu_cap la {self.phu_cap}"
            tp1=Truongphong("Nguyễn Trần Gia Bảo",2000000.24,160,500000)
            print(tp1.hien_thi_thong_tin())
            print("Luong cua truong phong la:", tp1.tinh_luong())
        tt1=TiepThi("Nguyễn Trần Gia Bảo",2000000.24,160,5000000,0.03)
        print(tt1.hien_thi_thong_tin())
        print("Luong cua tiep thi la:", tt1.tinh_luong())
        # Danh sách nhân viên
danh_sach_nv = []

def cn1():
    print("Chức năng 1: Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file.")
    so_luong_nv = int(input("Nhập số lượng nhân viên cần lưu:"))
    for i in range(so_luong_nv):
        print(f"Nhập thông tin nhân viên thứ {i+1}:")
        vitri = input("Vị trí nhân viên (NV/TT/TP):").upper()
        ma = input("Mã nhân viên:")
        ho_ten = input("Họ tên nhân viên:")
        luong_co_ban = float(input("Lương cơ bản:"))

        if vitri == "NV":
            nv = NV(ma, ho_ten, luong_co_ban)
        elif vitri == "TT":
            doanh_so = float(input("Doanh số bán hàng: "))
            hoa_hong = float(input("Tỉ lệ hoa hồng (%): ")) / 100
            nv = TT(ma, ho_ten, luong_co_ban, hoa_hong, doanh_so)
        elif vitri == "TP":
            luong_trach_nhiem = float(input("Phụ cấp trách nhiệm: "))
            nv = TP(ma, ho_ten, luong_co_ban, luong_trach_nhiem)
        else:
            print("Vị trí nhân viên không hợp lệ. Vui lòng nhập lại.")
            continue
        danh_sach_nv.append(nv)
    print("Đã nhập xong danh sách nhân viên:")
        
    # file_name = input("Nhập tên file .csv: ")
    # Kiểm tra file có tồn tại không
    # file_exists = os.path.exists(file_name)
    # Mở file: nếu chưa có thì tạo mới ('w'), nếu có thì ghi thêm ('a')
    # mode = "a" if file_exists else "w"
    # with open(file_name, mode, encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     for nv in danh_sach_nv:
    #         writer.writerow(nv)
    # print(f"Đã lưu {so_luong_nv} nhân viên vào file {file_name}.")

def cn2():
    print("Chức năng 2: Đọc thông tin nhân viên từ file và xuất danh sách nhân viên")
    pass
def cn3():
    print("Chức năng 3: Tìm và hiển thị nhân viên theo mã nhập từ bàn phím.")
    ma = input("Nhập mã nhân viên cần tìm:")
    for nv in danh_sach_nv:
        if nv.get_ma_nv() == ma:
            print("Thông tin nhân viên:")
            nv.xuat()
            return
    print("Không tìm thấy nhân viên với mã đã nhập.")

def cn4():
    print("Chức năng 4: Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu.")
    pass
def cn5():
    print("Chức năng 5: Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file.")
    pass
def cn6():
    print("Chức năng 6: Tìm các nhân viên theo khoảng lương nhập từ bàn phím.")
    luong_min = float(input("Nhập mức lương tối thiểu: "))
    luong_max = float(input("Nhập mức lương tối đa: "))
    print(f"Các nhân viên có khoảng lương: {luong_min} - {luong_max}")
    for nv in danh_sach_nv:
        if luong_min <= nv.get_thu_nhap() <= luong_max:
            nv.xuat()

def cn7():
    print("Chức năng 7: Sắp xếp nhân viên theo họ và tên.")
    danh_sach_nv.sort(key=lambda nv: nv.get_ho_ten())
    for nv in danh_sach_nv:
        nv.xuat()

def cn8():
    print("Chức năng 8: Sắp xếp nhân viên theo thu nhập.")
    danh_sach_nv.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
    for nv in danh_sach_nv:
        nv.xuat()

def cn9():
    print("Chức năng 9: Xuất 5 nhân viên có thu nhập cao nhất.")
    danh_sach_nv.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
    so_luong = min(5, len(danh_sach_nv))
    for nv in range(so_luong):
        danh_sach_nv[nv].xuat()

def cn10():
    print("Chức năng 10: Thoát chương trình.")
    print("Kết thúc chương trình.")      