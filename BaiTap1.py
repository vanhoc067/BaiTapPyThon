class Cau1:
    def InHinhChuNhat(self,n):
        for i in range(0,n):
            print("*" * n)


    def InHinhTamGiacVuongTrai(self,n):
        for i in range(1,n+1):
            print("*" * i)


    def InHinhTamGiacVuongPhai(self,n):
        for i in range(1,n+1):
            print(" " * (n - i) + "*" * i)


    def InHinhTamGiacCan(self,n):
        for i in range (1, n+1,2):
            print(("*"*i).center(n))



n = int(input(" Nhap vao mot so nguyen N: "))
testCau1 = Cau1()
testCau1.InHinhChuNhat(n)
print("------")
testCau1.InHinhTamGiacVuongPhai(n)
print("------")
testCau1.InHinhTamGiacVuongTrai(n)
print("------")
testCau1.InHinhTamGiacCan(n)
