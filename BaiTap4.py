class Cau4:
    allEmployee = [{"maNV":"1", "tenNV":"Nguyen Van A"},
    {"maNV":"2", "tenNV":"Tran Van B"},
    {"maNV":"3", "tenNV":"Nguyen Thi C"}]

    n = len(allEmployee)
    def GetAllEmployee(self):
        for i in range (0, self.n):
            print("Ma nhan vien: {0}".format(self.allEmployee[i]["maNV"]))
            print("Ten nhan vien: {0}".format(self.allEmployee[i]["tenNV"]))

    def FindEmployee(self,name_word, co):
        for i  in range(0,self.n):
            if self.allEmployee[i]["tenNV"].find(name_word) != -1:
                print("Ma nhan vien: {0}".format(self.allEmployee[i]["maNV"]))
                print("Ten nhan vien: {0}".format(self.allEmployee[i]["tenNV"]))
                co = True
        if co == False:
            print("Khong tim thay!!")

    def AddEmployee(self, id, name):
        newemp = {"maNV":id, "tenNV":name}
        self.allEmployee.append(newemp)
        self.n = len(self.allEmployee)
        self.GetAllEmployee()

    def DeleteEmployee(self,id):
        for i in range(0,self.n):
            if(self.allEmployee[i]["maNV"] == str(id)):
                del self.allEmployee[i]
                self.n = len(self.allEmployee)
                print(self.n)
                self.GetAllEmployee()
                return
        print("Not found id")


testcau4 = Cau4()
co = False

# testcau4.GetAllEmployee()

# name_word = str(input("Nhap tu khoa tim kiem: "))
# print("========== KET QUA ==========")
# testcau4.FindEmployee(name_word=name_word, co=co)

# id = str(input("Nhap ma NV can xoa: "))
# print("========== KET QUA ==========")
# testcau4.DeleteEmployee(id=id)


id = str(input("Nhap ma NV: "))
name = str(input("Nhap ten NV: "))
testcau4.AddEmployee(name=name, id=id)