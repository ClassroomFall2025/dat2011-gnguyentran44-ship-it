from sinhvienpoly import SinhVienPoLy


class SinhVien:
   #khởi tạo các thuộc tính
    def __init__(self, masv, tensv, diem):
        self.masv = masv
        self.tensv = tensv

        def get_diem(self):
            pass

        def get_hoc_luc(self):
            pass
        if self.get_diem() >=9 and self.get_diem() <=10:
            hoc_luc="Xuat sac"
        elif self.get_diem() >=8:
            hoc_luc="Gioi"
        elif self.get_diem() >=7:
            hoc_luc="kha"
        elif self.get_diem()>=5:
            hoc_luc="trung bình"
        elif self.get_diem()<5:
            hoc_luc="yeu"
            return hoc_luc
        def hien_thi_thong_tin(self):
            return f"masv la {self.masv},tensv la {self.tensv}", f"diem la {self.diem}", f"nganh_hoc la {self.__nganh_hoc}",f"hoc luc la {self.get_hoc_luc()}"
        
class sinhvienIT(SinhVienPoLy):
    def __init__(self, masv, tensv, diem, diemJava, diemHtml, diemCss):
        super().__init__(masv, tensv, diem)
        self.diemJava = diemJava
        self.diemHtml = diemHtml
        self.diemCss = diemCss
        self.__nganh_hoc = "IT"
        def get_diem(self):
            return (self.diemJava*2 + self.diemHtml + self.diemCss)/4
        class sinhvienBiz(SinhVienPoLy):
            def __init__(self, masv, tensv, diem, diemMarketing, diemSales):
                super().__init__(masv, tensv, diem)
                self.diemMarketing = diemMarketing
                self.diemSales =diemSales
                self.__nganh_hoc = "Biz"
                def get_diem(self):
                    return (self.diemMarketing*2+self.diemSales)/3

