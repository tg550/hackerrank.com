
d = ['2015-01-01','2016-05-01','2015-07-01','2015-10-01','2015-04-01']
df = pd.DataFrame({ 'Date': pd.to_datetime(d)})
a = df['Date'].dt.to_period('Q')
print(a.values)

import datetime as dt
import pandas as pd










##############2
numbers = [1, 6, 10]


def count(numbers):
    total_number = 0
    for num in numbers:
        for i in range(1,num+1,2):
            if num % i == 0:
                total_number = total_number + i
    return total_number

count(numbers) 

##############3
SELECT
    Departments.DEPT_NAME,
    COUNT(Students.STUDENT_ID)
FROM
    Departments LEFT JOIN Students ON Departments.DEPT_ID = Students.DEPT_ID
GROUP by
    Departments.DEPT_ID
ORDER by
    COUNT(Students.STUDENT_ID) DESC, 
    Departments.DEPT_NAME ASC






##############4
def root(n, tolerance):
   if n == '1':
      return 1
   elif n <= 0:
      print('this computes square root for positive numbers only' )
   else:
      pass
   prev_estimate = n/2
   while True: 
       new_estimate = (prev_estimate + n/prev_estimate)/2
       if abs(new_estimate * new_estimate - n) < tolerance:
         return prev_estimate

root(4,0.0001)
