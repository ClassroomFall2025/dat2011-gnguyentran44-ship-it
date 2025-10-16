from abc import ABC, abstractmethod

# Lớp trừu tượng SinhVien
class SinhVien(ABC):
    def __init__(self, ma_so, ho_ten, nganh):
        self.ma_so = ma_so
        self.ho_ten = ho_ten
        self.nganh = nganh

    @abstractmethod
    def get_diem(self):
        pass

    def xuat(self):
        print(f"MSSV: {self.ma_so}")
        print(f"Họ tên: {self.ho_ten}")
        print(f"Ngành học: {self.nganh}")
        print(f"Điểm: {self.get_diem()}")
        print(f"Học lực: {self.get_hoc_luc()}")

    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem >= 8:
            return "Giỏi"
        elif diem >= 6.5:
            return "Khá"
        elif diem >= 5:
            return "Trung bình"
        else:
            return "Yếu kém"

# Lớp con kế thừa SinhVien
class SinhVienCNTT(SinhVien):
    def __init__(self, ma_so, ho_ten, nganh, diem_lap_trinh, diem_csdl):
        super().__init__(ma_so, ho_ten, nganh)
        self.diem_lap_trinh = diem_lap_trinh
        self.diem_csdl = diem_csdl

    def get_diem(self):
        return (self.diem_lap_trinh + self.diem_csdl) / 2

# Ví dụ sử dụng
sv1 = SinhVienCNTT("SV001", "Nguyễn Văn A", "Công nghệ thông tin", 7.5, 8.0)
sv1.xuat()