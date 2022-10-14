import calendar
import datetime


class Premiumdate():

    def __init__(self,paid_month):

        self.paid_month = paid_month
        self.currentDate = datetime.date.today()
        
        
    #store for use also 
    def get_Days_from_month(self):
        day_count = 0
        for i in range(0, self.paid_month):
            
         
            if (self.currentDate.month + i >= 13):
                day_count += calendar.monthrange(self.currentDate.year + 1, self.currentDate.month + i - 12)[1]
                
            else:
                day_count += calendar.monthrange(self.currentDate.year, self.currentDate.month + i)[1]
                
         
        return day_count 

    
    # important to user #store
    def get_expiring_date(self,day_count):

        return datetime.date.today() + datetime.timedelta(days=day_count)
        
    # important to user
    def days_left(self, year, month, day):

        daysLeft = datetime.date(year, month, day) - datetime.date(self.currentDate.year, self.currentDate.month, self.currentDate.day)
        return daysLeft


testClass = Premiumdate(1)

# days from month
#print(testClass.get_Days_from_month(), "day!!!!!!")


#expiring
expiring = testClass.get_expiring_date(testClass.get_Days_from_month())
#print(expiring, "expire at")


# days left
#print(testClass.days_left(expiring.year, expiring.month, expiring.day).days)
#print(testClass.days_left().days)
