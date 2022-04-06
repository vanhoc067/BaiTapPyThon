class Cau3:
    dict = {
        "Information Technology": "Cong nghe thong tin",
        "Software Testing": "Kiem thu phan mem",
        "Data Mining": "Khai pha du lieu",
        "Computer Vision": "Thi giac may tinh"
    }

    def Add(self, key, value):
        if (key not in self.dict.keys()):
            self.dict[key] = value

    def ShowAll(self):
        print(self.dict.items())
        print("So tu: ", len(self.dict))

    def Search(self, keyword, co):
        for k in self.dict.keys():
            if (k == keyword):
                print("key: ", str(keyword), " co gia tri: ", str(self.dict[keyword]))
                co = True
        if co == False:
            print("Khong tim thay!!")

    def DeleteItem(self, keyword, co):
        for k in self.dict.keys():
            if (k == keyword):
                del self.dict[keyword]
                co = True
            else:
                co = False
        if co == True:
            print("Xoa thanh cong!!")
        else:
            print("Khong tim thay tu can xoa!!")


testCau3 = Cau3()
co = False
#
# key = str(input('Nhap tu tieng Anh can them: '))
# value = str(input('Nhap y nghia: '))
# testCau3.Add(key=key, value=value)
#
# testCau3.ShowAll()


# keyword = str(input('Nhap tu tieng Anh can tim: '))
# testCau3.Search(keyword=keyword, co=co)

keyword = str(input('Nhap tu can xoa: '))
testCau3.DeleteItem(keyword=keyword, co=co)