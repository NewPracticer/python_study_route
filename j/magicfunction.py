# 魔法函数
# python自带 已提前定义好
class Company(object):

    def __init__(self,employee_list):
        self.employee = employee_list
    
    def __getitem__(self,item):
        return self.employee[item]

    def __str__(self):
        return ','.join(self.employee)

company = Company(["tom","bob","jane"])
employee = company.employee

for em in employee:
    print(em)

for em in company:
    print(em)

print(company)

    