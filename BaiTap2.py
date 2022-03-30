class Cau2:
    def FindMinMax(self):
        a = []
        n = int(input("Nhap so luong phan tu: "))
        if(n<=0):
            exit()
        for i in range(n):
            a.append(int(input("Nhap phan tu thu %d: " % (i+1))))
        print("Danh sach a: ")
        print(a)
        highest = max(a)
        lowest = min(a)
        if highest<0:
            print("So duong lon nhat: *")
        else:
            print("So duong lon nhat: ", highest)
        if lowest>0:
            print("So am be nhat: *")
        else:
            print("So am be nhat:",lowest )

testCau2 = Cau2();
testCau2.FindMinMax()
