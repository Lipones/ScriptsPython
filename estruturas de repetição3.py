# -*- coding: utf-8 -*-
for i in range(10,20,2):#com o comand podemos determinar um limite inicial, um limite final e o passo em que será repetido
	print(i)

x = [1,2,3,4]
out = []
for item in x:
    out.append(item**2)
print(out)

[item**2 for item in x]