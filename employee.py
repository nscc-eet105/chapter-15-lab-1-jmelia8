#Joe Melia EET-107

class Employee:
    
    def __init__(self, name, hours, rate):
        self.__name = name
        self.__hours = hours
        self.__rate = rate

    def get_name(self):
        return self.__name
    def get_hours(self):
        return self.__hours
    def get_rate(self):
        return self.__rate

    def set_name(self, name):
        self.__name = name
    def set_hours(self, hours):
        self.__hours = hours
    def set_rate(self, rate):
        self.__rate = rate

    def calc_pay(self):
        return self.__hours * self.__rate

class Salesperson(Employee):
    
    def __init__(self, name, hours, rate, weekly_sales, cms_rate):
        Employee.__init__(self, name, hours, rate)
        self.__weekly_sales = weekly_sales
        self.__cms_rate = cms_rate

    def get_weekly_sales(self):
        return self.__weekly_sales
    def get_cms_rate(self):
        return self.__cms_rate

    def set_weekly_sales(self, weekly_sales):
        self.__weekly_sales = weekly_sales
    def set_cms_rate(self, cms_rate):
        self.__cms_rate = cms_rate

    def calc_pay(self):
        hourly = Employee.calc_pay(self)
        cms = self.__weekly_sales * self.__cms_rate
        return hourly + cms
    
