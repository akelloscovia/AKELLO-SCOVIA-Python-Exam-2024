# answer (1i)

def circle_area():
    import math
    def circle_area(radius):
     pi =3.14
    return math.pi*(radius **2)
radius= 4
area=circle_area(radius)
print(f"area of a circle with radius{radius}is {area:.2f}")
    
# (ii)
list=[4,7,2,9,12,15]
numbers=[4,7,2,9,12,15]
odd_sum =0
for num in numbers:
    if num % 2 != 0:
        odd_sum += num
print("sum of odd numbers")


#(iii)
def calculate(a,b):
   return a + b, a - b, a * b, a / b

sum_, diff, prod, quot = calculate(10, 2)

print(f"Sum: {sum_}, Difference: {diff}, Product: {prod}, Quotient: {quot}")

#(iv)
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student_info['age'] = 26 
student_info['city'] = 'kampala'
print("The dictionary:",student_info )



        

    



