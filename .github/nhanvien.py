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
