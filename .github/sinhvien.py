class sinhvien:

    #Các thuộc tính
    def __init__(self,ten,tuoi,diem):
        self.ten=ten
        self.tuoi=tuoi
        self.diem=diem
    #Các phương thức
    def hoc_luc(self):
        if self.diem < 5:
            return "Yếu"
        elif self.diem <7:
            return "Trung bình"
        elif self.diem <8:
            return "Khá"
        else:
            return "Giỏi"
    def __str__(self):
        return f"sinh viên {self.ten} {self.tuoi} tuổi có điểm {self.diem} học lực {self.hoc_luc()}"
    # sv1=sinhvien("Nguyễn Trần Gia Bảo",20,8)
    #print(sv1)
    # sv2=sinhvien("Lê Thị Thu Hà",19.5)
   #print(sv2)
   # sv3=sinhvien("Trần Bích Ngọc",18,9)
   #print(sv3)

   