#!/usr/bin/env python

class SplitDateStr():

    def __init__(self, datestr):

        self.datestr = datestr
        self.a = ' '

    def datelist(self):
        for i in self.datestr:
            if i == '-':
                i = " "

            self.a += i

        splite_date= self.a.split()

        date_list = [ int(i) for i in splite_date ]

        return date_list

# Test
c='2023-02-14'
Test = SplitDateStr(c)
print(Test.datelist())
