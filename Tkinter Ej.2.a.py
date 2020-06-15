from tkinter import *


# Define la ventana principal
main = Tk()
main.title('Calculadora de Financiación')

C = StringVar()
F = StringVar()
I = StringVar()

# Función convocada desde el boton de cálculo de la financiacón.
# Utiliza la formula de calculo de valor actual de una renta fija prepaga:
# Va=R * {[1-(1+tasa)^(-n)]/tasa} * (1+tasa) donde:
# tasa: es el valor de la tasa anual por año, de interés compuesto
# y es el informado por el enunciado
# n: Es el número de períodos seleccionados que no puede exceder de 18
# R: es la renta o cuota, que despejada de esta formula y
# nos permite encontrar el valor buscado)
def valor_cuota ():
    total = float(monto_Entry.get())
    num_cuotas = float(cuotas_Entry.get())
    int_dic = {'0-2': 0, '3-6': 0.1, '7-12': 0.2, '13-18': 0.3}
    if num_cuotas < 19:
        if num_cuotas > 2:
            if 3 <= num_cuotas < 7:
                int = int_dic['3-6']
            elif num_cuotas < 13:
                int = int_dic['7-12']
            else:
                int = int_dic['13-18']
            cuota = round((total / (1 - (1 + int) ** (-num_cuotas))) * int / (1 + int), 2)
        else:
            cuota = round(total / num_cuotas, 2)
        pagoTotal = round(cuota * num_cuotas, 2)
        intereses = round(pagoTotal-total, 2)
        C.set('$'+str(cuota))
        F.set('$'+str(pagoTotal))
        I.set('$'+str(intereses))
    else:
        C.set('18 cuotas màximo')

# Funcion ejecutada por el boton borrar
def borrar():
    monto_Entry.delete(first=0,last=22)
    monto_Entry.focus()
    cuotas_Entry.delete(first=0,last=22)
    ValorCuota_Entry.delete(first=0,last=22)
    ValorFinal_Entry.delete(first=0,last=22)
    ValorIntereses_Entry.delete(first=0,last=22)

# Funcion para salir del loop y cerrar la ventana
def salir():
    main.destroy()


#Ingreso del monto total del producto o total a financiar (texto y ventana de entrada)
monto_Lbl=Label(text='Pago Total').grid(row=0,column=0)
monto_Entry = Entry(main)
monto_Entry.grid(row=0,column=1, padx=20, pady=20)

# Ingreso de la acntidad de cuotas (texto y ventana de entrada)
cuotas_Lbl=Label(text='Cantidad de cuotas').grid(row=1,column=0)
cuotas_Entry = Entry(main)
cuotas_Entry.grid(row=1, column=1, padx=20, pady=20)

# Presentación del valor de la cuota
ValorCuotaTxt_Lbl = Label(main, text='Valor de la cuota:').grid(row=2 , column=0)
ValorCuota_Entry = Entry(main, textvariable=C)
ValorCuota_Entry.grid(row=2, column=1, padx=20, pady=20)

# Pago total o suma de todas las cuotas. No tiene significación financiera, ya que son
# pagos realizados en distintos  momentos.
# Para poder sumarlos habría que llevarlos al mismo momento.
ValorFinalTxt_Lbl= Label(main,text='Valor final pagado:')
ValorFinalTxt_Lbl.grid(row=3, column=0)
ValorFinal_Entry = Entry(main, textvariable=F)
ValorFinal_Entry.grid(row=3, column=1, padx=20, pady=20)

# Intereses Pagados.  Diferencia entre el monto por unica vez y la suma de todos los pagos
ValorInteresesTxt_Lbl= Label(main, text='Intereses:')
ValorInteresesTxt_Lbl.grid(row=4, column=0)
ValorIntereses_Entry = Entry(main, textvariable=I)
ValorIntereses_Entry.grid(row=4, column=1, padx=20, pady=20)

# Botón para ejecutar los cálculos de la función "valor_cuota"
monto_BTN = Button(main, text = 'calcule la Financiación', command = valor_cuota, width=50)
monto_BTN.grid(row=5, columnspan=2, pady=20)

# Boton para limpiar y reiniciar el cálculo
nuevo_BTN = Button(main, text='Borrar', command=borrar).grid(row=6, column=0)

# Boton para salir del loop y cerrar la ventana
Salir_BTN = Button(main, text='Cerrar la ventana', command=salir).grid(row=6, column=1)


mainloop()