class sinhvien:
    def __init__(self, ho_ten_sv, nganh_hoc, diem_java, diem_html, diem_css):
        self.ho_ten_sv = ho_ten_sv
        self.nganh_hoc = nganh_hoc
        self.diem_java = diem_java
        self.diem_html = diem_html
        self.diem_css = diem_css

    def __getattr__(self, name):
        raise NotImplementedError

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

class quanlysinhvien:
    #khởi tạo danh sách sinh viên
    def __init__(self):
        self.sinhvien = []
    #nhập danh sách sinh viên
    def nhap_sinh_vien(self):
        pass

    def in_danh_sach(self):
        pass

    def sap_xep_hoc_luc_gioi(self):
        pass

    def sap_xep_theo_diem(self):
        pass
    def ket_thuc(self):
        while True:
            ho_ten_sv=input("Mời bạn nhập họ tên sinh viên:")
            nganh_hoc=input("Mời bạn nhập ngành hoc:")
            if nganh_hoc=="IT":
                diem_java=float(input("Mời bạn nhập điểm java:"))
                diem_html=float(input("Mời bạn nhập điểm html:"))
                diem_css=float(input("Mời bạn nhập điểm css:"))
                sv=sinhvien(ho_ten_sv,nganh_hoc,diem_java,diem_html,diem_css)
                self.sinhvien.append(sv)
            else:
                print("Ngành học không hợp lệ!")
                if nganh_hoc=="Biz":
                    diem_marketing = float(input("Mời bạn nhập điểm marketing:"))
                    diem_sales=float(input("Mời bạn nhập điểm sales:"))
                    sv=sinhvien(ho_ten_sv ,nganh_hoc ,diem_marketing ,diem_sales)
                    self.sinhvien.append(sv)
                else:
                    print("Ngành học không hợp lệ!")
                    
                
