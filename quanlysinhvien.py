import sinhvienpoly as sv
class QuanLySinhVien:
    def __int__ (self):
        self.ds_sinh_vien =[]
        def nhap_dssv(self):
            n = int(input("Nhập số lượng sinh viên: "))
            for i in range(n):
                print(f"Nhập thông tin sinh viên thứ {i + 1}:")
                tensv = input("Tên sinh viên: ")
                nganh = input("Ngành học: ")
                loai = input("Loại sinh viên (IT/Biz): ")
                if loai == "IT":
                    java = float(input("Điểm Java: "))
                    html = float(input("Điểm HTML: "))
                    css = float(input("Điểm CSS: "))
                    sv_it = sv.SinhVienIT(tensv, nganh, java, html, css)
                    self.ds_sinh_vien.append(sv_it)
                elif loai == "Biz":
                    marketing = float(input("Điểm Marketing: "))
                    sales = float(input("Điểm Sales: "))
                    sv_biz = sv.SinhVienBiz(tensv, nganh, marketing, sales)
                    self.ds_sinh_vien.append(sv_biz)

    def xuat_dssv(self):
        for sinh_vien in self.ds_sinh_vien:
            print("Thông tin sinh viên:")
            print(f"Tên: {sinh_vien.tensv}")
            print(f"Ngành: {sinh_vien.nganh}")
            print(f"Điểm: {sinh_vien.get_diem()}")
            print(f"Học lực: {sinh_vien.get_hoc_luc()}")