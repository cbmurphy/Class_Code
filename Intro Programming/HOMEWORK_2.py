'''
def main():
  radius, length = eval(input('Enter the radius and length of a cylinder: '))
  area = radius ** 2 * 3.14159
  volume = area * length
  print("The area is", area)
  print("The volume is", volume)
       

main()
'''
'''
def main():
  pounds = eval(input("Enter a value in pounds: "))
  kilos = pounds * 0.0454
  print(pounds, "pounds is", kilos, "kilos")

main()
'''
'''
def main():
  water = eval(input('Enter the amount of water in kilograms: '))
  tempIn = eval(input('Enter the initial temperature: '))
  tempFin = eval(input('Enter the final temperature: '))
  Q = water * (tempFin - tempIn) * 4184
  print('The energy needed is', Q)

main()
'''
'''
def main():
  speed, accel = eval(input('Enter speed and acceleration: '))
  length = speed ** 2 / (2 * accel)
  print('The minimum runway length for this airplane is', length)

main()
'''
'''
def main():
  print('a \t b \t a ** b')
  for x in range(5):
    a = x + 1
    b = x + 2
    c = a ** b
    print('%d \t %d \t %d' % (a, b, c))
main()
'''
'''
def main():
  ax, ay, bx, by, cx, cy = eval(input('Enter three points for a triangle: '))
  side1 = (abs(ax - bx) **2 + abs(ay - by) ** 2) ** 0.5
  side2 = (abs(bx - cx) ** 2 + abs(by - cy) ** 2) ** 0.5
  side3 = (abs(cx - ax) ** 2 + abs(cy - ay) ** 2) ** 0.5
  print(side1, side2, side3)
  s = (side1 + side2 + side3) / 2
  print(s)
  area = (s * abs(s - side1) * abs(s - side2) * abs(s - side3)) ** 0.5
  print(area)
  print('The area of the triangle is %f' % area)

main()
'''
'''
def main():
  v0, v1, t = eval(input('Enter v0, v1, and t: '))
  accel = (v1 - v0) / t
  print('The average acceleration is %f' %accel)

main()
'''
'''
import time

def main():
  offset = eval(input('Enter the time zone offset to GMT: '))
  currentTime = time.time()
  currentTime += offset * 60 * 60
  totalSeconds = int(currentTime)
  currentSecond = totalSeconds % 60
  totalMinutes = totalSeconds // 60
  currentMinute = totalMinutes % 60
  totalHours = totalMinutes // 60
  currentHour = totalHours % 24
  
  print('Current time is', currentHour, ':', currentMinute, ':', currentSecond, 'GMT')

main()
'''
'''
def main():
  balance, rate = eval(input('Enter balance and interest rate (e.g., 3 for 3%): '))
  interest = balance * (rate / 1200)
  print('The interest is %g' % interest)

main()
'''
def main():
  #get number of years
  years = eval(input('Enter the number of years: '))
  
  #calculate seconds per year
  secondsPerYear = 60 * 60 * 24 * 365
  #print(secondsPerYear)

  #calculate population
  currentPopulation = 312032486
  seconds = secondsPerYear * years
  population = currentPopulation + (seconds // 7) - (seconds // 13) + (seconds // 45)
  print('The population in %d years is %d' % (years, population))

main()
