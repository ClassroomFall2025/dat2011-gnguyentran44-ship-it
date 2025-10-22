class sanpham:
    def __init__(self,ten_san_pham,gia,giam_gia):
        self.ten_san_pham =ten_san_pham
        self.gia=gia
        self.giam_gia=giam_gia

    def doc_giam_gia(self):
        return self.giam_gia
    def ghi_giam_gia(self,giam_gia_moi):
        self.giam_gia=giam_gia_moi
    def thue_nhap_khau(self):
        return self.gia*0.1
    

    def nhap_thong_tin(self):
        self.ten_san_pham = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập giá sản phẩm: "))
        self.giam_gia = float(input("Nhập giá giảm: "))

    def xuat_thong_tin(self):
        return(f"san pham {self.ten_san_pham} có giá {self.gia} được giảm giá {self.giam_gia} và thuế nhập khẩu là {self.thue_nhap_khau()}")
    def __str__(self):
        return f"Sản phẩm {self. ten_san_pham} có giá {self.gia}được giảm giá {self.giam_gia} và thuế nhập khẩu là {self.thue_nhap_khau()}"
    


# sp1=sanpham("beer",2000000,100000)
# print(sp1.doc_giam_gia)
# print(sp1.giam_gia)
# sp1.xuat_thong_tin()
# print(sp1)

# sp1.ghi_giam_gia(20000)
# print(sp1)