'''
Task Description: In this task, we develop a Body Mass Index (BMI) Calculator that can be used to calculate
your BMI value and weight status while taking your age into consideration. Use the "metric units" tab if
you are more comfortable with the international standard metric units. The referenced weight range and
calculation formula is listed below. The program requirement is as follows:
1. Allow users to run your program with three input arguments by passing three values to the
program: the choice of units, height, and weight.
2. Your program will read the three arguments and calculate BMI using the following two formulas:
BMI = weight(kg)/height2(m2) (Metric Units)
BMI = 703·weight(lb)/height2(in2) (Imperial (U.S.) Units)
NOTE: The formulas to calculate BMI are based on two of the most used unit systems.
3. After user inputs all the numbers, if the input numbers are invalid, you need to present an error
message “Your input is invalid!”. Otherwise, you need to print out BMI and category. The output
payment requires to have 2 precisions. For instance, if BMI is 23.456, it should print 23.46. If BMI
is 23, it should print 23.00.

BMI Table for Adults
This is the World Health Organization's (WHO) recommended body weight based on BMI values for adults.
It is used for both men and women, age 18 or older.
Category BMI range - kg/m2
Severe Thinness <= 16
Moderate Thinness >16 - 17
Mild Thinness >17 - 18.5
Normal >18.5 - 25
Overweight >25 - 30
Obese Class I >30 - 35
Obese Class II >35 - 40
Obese Class III >40

Example output is as follows. Note that '%0.2f\tSevere Thinness' should be used.
NOTE: You must strictly follow the input and output format.
Running example:
C:\ICT1002\Lab1\BMI Calculator>python BMICalculatorTest.py metric 1.80 78
24.07 Normal
C:\ICT1002\Lab1\BMI Calculator>python BMICalculatorTest.py metric 1.78 48
15.15 Severe Thinness
C:\ICT1002\Lab1\BMI Calculator>python BMICalculatorTest.py metric 1.60 126
49.22 Obese Class III
C:\ICT1002\Lab1\BMI Calculator>python BMICalculatorTest.py imperial 68.90 154.32
22.85 Normal
C:\ICT1002\Lab1\BMI Calculator>python BMICalculatorTest.py imperial 85.63 135.68
13.01 Severe Thinness
C:\ICT1002\Lab1\BMI Calculator>python BMICalculatorTest.py abc
Your input is invalid!
'''
import sys
# write your code here
import re

def is_decimal_string(s):
    decimal_pattern = re.compile(r'^[+-]?\d*\.\d+$')
    return bool(decimal_pattern.match(s))

def BMICalculator():
    pass



if __name__=='__main__':
    BMICalculator()
    
