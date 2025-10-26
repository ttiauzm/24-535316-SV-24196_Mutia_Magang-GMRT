import math

servo1_deg = 40   #sudut coxa ke femur
servo2_deg = 30   #sudut femur ke tibia

femur = 16  #panjang femur
tibia = 94  #panjang tibia

servo1_rad = math.radians(servo1_deg)
servo2_rad = math.radians(servo2_deg)

x1 = femur * math.cos(servo1_rad)
y1 = femur * math.sin(servo1_rad)

x2 = x1 + tibia * math.cos(servo1_rad + servo2_rad)
y2 = y1 + tibia * math.sin(servo1_rad + servo2_rad)

print(f"({x2:.2f}, {y2:.2f})")
