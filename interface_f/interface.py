from calculater.income_Infor import incomeInfor
class interface(incomeInfor):
    def __init__(self):
        super().__init__(basic_salary=0, dependent=0, allowance=0, bonus=0)
    def gui(self):
        print("----------------------------------------Net Salary System---------------------------------------")
        print("1.Check Net Salary")
        print("2.Check Insurance")
        print("3.Check Personal Income Tax")
        print("4.Check Overtime Income")
        print("5.Quit")
        print("------------------------------------------------------------------------------------------------")
    def displayMenu(self):
        while True:
            self.gui()
            choice = input('Please Input a value to use Function (Ex: 1) \n')
            if choice == "1":
                basic_sa = input("Please Input Your Basic Salary : \n")
                if basic_sa.isnumeric() == False:
                    print("-->You Have To Input Numeric Value !")
                    True
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                print('Bye!!!')
                break
            else:
                print('This function did not exist!')
