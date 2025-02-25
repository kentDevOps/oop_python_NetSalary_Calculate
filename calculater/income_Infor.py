class incomeInfor:
    def __init__(self,basic_salary,dependent,allowance,bonus):
        self.basic_s = basic_salary
        self.dependent_s = dependent
        self.allowance_s = allowance
        self.bonus_s = bonus
    def printInfor(self):
        print("----------------Basic Information---------------")
        print(f"Your Basic Salary Per Month is : {int(self.basic_s):,} VND")
        print(f"Your Number of Dependent is : {self.dependent_s} Member")
        print(f"Your Monthly Allowance is : {int(self.allowance_s):,} VND")
        print(f"Your Bonus Money is : {int(self.bonus_s):,} VND")