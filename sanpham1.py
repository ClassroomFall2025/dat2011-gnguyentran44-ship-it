class SinhVienPoLy:
        def __init__(self, tensv, nganh):
                self.tensv = tensv
                self.nganh = nganh
                def get_diem(self):
                        pass
                def get_hoc_luc(self):
                        pass
                def xuat(self):
                        pass

class SinhVienIT(SinhVienPoLy):
        def __init__(self, tensv, nganh, java, html, css):
                super().__init__(tensv, nganh)
                self.java = java
                self.html = html
                self.css = css
        def get_diem(self):
                return (self.java + self.html + self.css) / 3
        
class SinhVienBiz(SinhVienPoLy):
        def __init__(self, tensinh, nganh, marketing, sales):
                super().__init__(tensinh, nganh)
                self.marketing = marketing
                self.sales = sales
        def get_diem(self):
                return (self.marketing * 2 + self.sales) / 3