#ada beberapa data di python yaitu, INT, STR, FLOAT, BOOL
#merubah type data ke  data lain disebut casting

print('====INTEGER====')
data_int = 0
data_str = str(data_int) # merubah int ke str
data_float = float(data_int) # merubah int ke float
data_bool = bool(data_int) # merubah int ke boolean
print ('datanya adalah = ',data_str,type(data_str))
print ('datanya adalah = ',data_float,type(data_float))
print ('datanya adalah = ',data_bool,type(data_bool))

print('===FLOAT====')
data_floot  = 21.5
data_integer = int(data_floot) # merubah float ke int
data_string = str(data_floot) # merubah float ke string
data_boolean = bool(data_floot) # merubah float ke bool
print ('datanya adalah = ',data_integer,type(data_integer))
print ('datanya adalah = ',data_string,type(data_string))
print ('datanya adalah = ',data_boolean,type(data_boolean))

print('===BOOLEAN====')
data_bol = True # jika TRUE maka semua data akan menjadi 1, Jika False maka akan 0
data_in = int(data_bol) 
data_fl = float(data_bol)
data_st = str(data_bol)
print ('datanya adalah = ',data_in,type(data_in))
print ('datanya adalah = ',data_fl,type(data_fl))
print ('datanya adalah = ',data_st,type(data_st))


print('===STRING====')
data_strings = '1'
data_boole = bool(int(data_strings))
print ('datanya adalah = ',data_boole,type(data_boole))




