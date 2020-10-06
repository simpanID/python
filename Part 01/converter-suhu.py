########PROGRAM CONVERTER SUHU########
##########CONVERTER CELCIUS############
celcius = float(input('masukan suhu Celcius nya = '))
print ('kamu menginput',celcius,'C')

print('++++++++++++++++++++++++++++')
reamur = (4/5)*celcius
print ('Convert',celcius,'Celcius -> Reamur adalah',reamur,'R')

kelvin = celcius+273
print ('Convert',celcius,'Celcius -> Kelvin adalah',kelvin,'K')

fahrenheit = (9/5)*celcius+32
print ('Convert',celcius,'Celcius -> Fahrenheit adalah',fahrenheit,'F')
print('++++++++++++++++++++++++++++')

#######################################
##########CONVERTER REAMUR############
reamur = float(input('masukan suhu Reamur nya = '))
print ('kamu menginput',reamur,'R')

print('++++++++++++++++++++++++++++')
celcius = (5/4)*reamur
print('convert',reamur,'Reamur -> Celcius adalah',celcius,'C')

kelvin = celcius+273
print('convert',reamur,'Reamur -> Kelvin adalah',kelvin,'K')

fahrenheit = (9/4)*reamur+32
print('convert',reamur,'Reamur -> Fahrenheit adalah',fahrenheit,'F')

#######################################
##########CONVERTER FAHRENHEIT############
fahrenheit = float(input('masukan suhu Fahrenheit nya = '))
print ('kamu menginput',fahrenheit,'F')

print('++++++++++++++++++++++++++++')
celcius = 5/9*(fahrenheit-32)
print('convert',fahrenheit,'Fahrenheit -> Celcius adalah',celcius,'C')

reamur = 4/9*(fahrenheit-32)
print('convert',fahrenheit,'Fahrenheit -> Reamur adalah',reamur,'R')

kelvin = 5/9*(fahrenheit-32)+273
print('convert',fahrenheit,'Fahrenheit -> Kelvin adalah',kelvin,'K')

#######################################
##########CONVERTER KELVIN############
kelvin = float(input('masukan suhu Kelvin nya = '))
print('kamu menginput',kelvin,'K')

print('++++++++++++++++++++++++++++')
celcius = kelvin-273
print('convert',kelvin,'Kelvin -> Celcius adalah',celcius,'C')

reamur = 4/5*(kelvin-273)
print('convert',kelvin,'Kelvin -> Reamur adalah',reamur,'R')

fahrenheit = 9/5*(kelvin-273)+32
print('convert',kelvin,'Kelvin -> Fahrenheit adalah',fahrenheit,'F')


