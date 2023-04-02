class Sinhvien:
    countsv = 0
    def __init__(self, masv, tensv, ngsinh, lop, diemtichluy,sdt):
        self.masv = masv
        self.tensv = tensv
        self.ngsinh = ngsinh
        self.lop = lop
        self.diemtichluy = diemtichluy
        self.sdt = sdt
        Sinhvien.countsv += 1

    def InThongTinSV(self):
        print('\nMã SV         :', self.masv)
        print('Tên SV        :', self.tensv)
        print('Ngày Sinh     :', self.ngsinh)
        print('Lớp           :', self.lop)
        print('Điểm tích lũy :', self.diemtichluy)
        print('Số điện thoại :', self.sdt)

    def XepLoai(self):
        if self.diemtichluy >= 3.5:
            print('\nXuất sắc')
        elif 3.2 <= self.diemtichluy < 3.5:
            print('\nGiỏi')
        elif 2.5 <= self.diemtichluy < 3.2:
            print('\nKhá')
        elif 2 <= self.diemtichluy < 2.5:
            print('\nTrung bình')
        else:
            print('\nKém')

    def SuaThongTinSv(self):
        sdt_m = int(input('\nNhập số điện thoại mới:'))
        self.sdt = sdt_m
        print('Cập nhật thành công')

#•	Tạo 3 đối tượng sinh viên, có thông tin như bảng dưới đây:
sv1 = Sinhvien('201112345','Nguyễn Tiến Thanh','12/10/2002','45k14',3.4,'')
sv2 = Sinhvien('201112346','Phùng Lê Na','05/06/2002','45k14',1.9,'')
sv3 = Sinhvien('201112347','Trần Văn Hùng','07/11/2002','45k21.1',2.3,'')

#•	Sử dụng phương thức XepLoai để kiểm tra xếp loại học lực của sinh viên Nguyễn Tiến Thành
sv1.XepLoai()

#•	Sử dụng phương thức SuaThongTinSV để đổi số điện thoại của Phùng Lê Na thành 091234567
sv3.SuaThongTinSv()

# •	In thông tin của 3 sinh viên ra màn hình
sv1.InThongTinSV()
sv2.InThongTinSV()
sv3.InThongTinSV()