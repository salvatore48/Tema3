a = ﬂoat(input('Valor de a: ')) 
b = ﬂoat(input('Valor de b: '))

try :
	x = (-b/a)
	print ('Solucion: ', x)
except:
	if (b != 0) :
          print ('La␣ecuacion␣no␣tiene␣solucion.')
          