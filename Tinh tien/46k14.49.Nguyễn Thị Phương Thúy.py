class Hanghoa:
    countsv = 0
    def __init__(self, mahang, tenhanghoa, soluonghh, gianhap, giaban, khuyenmai):
        self.mahang = mahang
        self.tenhanghoa = tenhanghoa
        self.soluonghh = soluonghh
        self.gianhap = gianhap
        self.giaban = giaban
        self.khuyenmai = khuyenmai
        Hanghoa.countsv += 1
    def Tinhgiaban(self):
        if self.soluonghh > 100:
            self.giaban = self.gianhap * 0.1
        if 50 < self.soluonghh <= 100:
             self.giaban = self.gianhap * 0.1
        if self.soluonghh < 50:
            self.giaban = self.gianhap * 0.2


sp1=Hanghoa('M01','Mì tôm hảo hảo',100,3000,'',0)
sp2=Hanghoa('D01','Dầu ăn Trường An(1 lít) 10',20,40000,'',0)

sp1.Tinhgiaban()
print('giá bán:',sp1.giaban)