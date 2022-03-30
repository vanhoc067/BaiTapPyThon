class Cau4:
    allEmployee = [{"maNV":"1", "tenNV":"Nguyen Van A"},
    {"maNV":"2", "tenNV":"Tran Van B"},
    {"maNV":"3", "tenNV":"Nguyen Thi C"}]

    n = len(allEmployee)
    def GetAllEmployee(self):
        for i in range (0,self):
            print("Ma nhan vien: {0}".format(self.allEmployee[i]["maNV"]))
            print("Ten nhan vien: {0}".format(self.allEmployee[i]["tenNV"]))

    def FindEmployee(self,name_word):
        for i  in range(0,self.n):
            if self.allEmployee[i]["tenNV"].find(name_word) != -1:
                print("Ma nhan vien: {0}".format(self.allEmployee["maNV"]))
                print("Ten nhan vien: {0}".format(self.allEmployee["tenNV"]))

    def AddEmployee(self):
        print("Nhap ma nhan vien")
        id = str(input())
        name = str(input())
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

