class SinhVien:
    # Các thuộc tinh
    ten_sinh_Vien = ""
    nam_sinh = ""
    diem = ""

    # Các phương thức
    def them_sinh_vien(self, ten_sv, namsinh_sv, diem_mon):
        self.ten_sinh_Vien = ten_sv
        self.nam_sinh = namsinh_sv
        self.diem = diem_mon
    
    def xuat_thong_tin_sv(self):
        print(f"Sinh viên {self.ten_sinh_Vien}, sinh năm {self.nam_sinh} có điểm môn {self.diem}")


sv1 = SinhVien()
sv1.them_sinh_vien("Gia Bao",2006,7)
sv1.xuat_thong_tin_sv()