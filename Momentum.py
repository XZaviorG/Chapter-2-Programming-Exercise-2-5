GP_01_PE_2-5 (Chapter 2: Programming Exercise 2-5)

Task 1: Write a program in the file momentum.py that accepts an object’s mass (in kilograms) and velocity (in meters per second) as inputs and then outputs its momentum. (LO: 2.3, 2.4)

print("This program calculates an object's momentum.")
mass = float(input("Enter mass in Kg:"))
velocity = int(input("Enter velocity in m/s:"))
momentum = (mass * velocity)
print("The objects Momentum is", momentum, "kg m/s")
