from sinhvienpoly import SinhVienPoLy


class SinhVien:
    # khởi tạo các thuộc tính
    def __init__(self, masv, tensv, diem):
        self.masv = masv
        self.tensv = tensv
        self.diem = diem
        self.__nganh_hoc = None

    def get_diem(self):
        return self.diem
        pass
    def get_hoc_luc(self):
        if self.get_diem() >= 9 and self.get_diem() <= 10:
            return "Xuat sac"
        elif self.get_diem() >= 8:
            return "Gioi"
        elif self.get_diem() >= 7:
            return "Kha"
        elif self.get_diem() >= 5:
            return "Trung bình"
        else:
            return "Yeu"

    def hien_thi_thong_tin(self):
        return (
            f"masv la {self.masv}, tensv la {self.tensv}",
            f"diem la {self.diem}",
            f"nganh_hoc la {self.__nganh_hoc}",
            f"hoc luc la {self.get_hoc_luc()}",
        )


class SinhVienIT(SinhVienPoLy):
    def __init__(self, masv, tensv, diem, diemJava, diemHtml, diemCss):
        super().__init__(masv, tensv, diem)
        self.diemJava = diemJava
        self.diemHtml = diemHtml
        self.diemCss = diemCss
        self.__nganh_hoc = "IT"

    def get_diem(self):
        # override: compute average of technical scores (adjust as you need)
        return (self.diemJava + self.diemHtml + self.diemCss) / 3
# ...existing code...

