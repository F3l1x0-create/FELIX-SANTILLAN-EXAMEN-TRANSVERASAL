import csv 
opc=0
sueldos=0
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]



while True:
    print("==menu principal==")
    print("[1]- asignar sueldos aleatorios")
    print("[2]- clasificar sueldos")
    print("[3]- ver estadisticas")
    print("[4]- reporte de sueldos ")
    print("[5]- salir ")
    opc=int(input("seleccione una opcion : "))
    

    if opc==1:
        print("asignale un sueldo base a cada uno de los trabajadores : ")
        
        sueldos=juan_perez=int(input("juan perez, sueldo : "))
        maria_garcia=int(input("maria garcia, sueldo : "))
        carlos_lopez=int(input("carlos lopez, sueldo : "))
        ana_martinez=int(input("ana martinez, sueldo : "))
        pedro_rodriguez=int(input("pedro rodriguez, sueldo : "))
        laura_hernandez=int(input("laura hernandez, sueldo : "))
        miguel_sanchez=int(input("miguel sanchez, sueldo : "))
        isabel_gomez=int(input("isabel gomez, sueldo : "))
        fabricio_diaz=int(input("fabricio diaz, sueldo : "))
        elena_hernandez=int(input("elena hernandez, sueldo : "))

        
        print("==SUELDOS ASIGNADOS==")


    if opc==2:
        print("sueldos menor a $800.000")
        print("total : ",  )

        print("sueldos entre los $800.000 y 1.200.000")
        print("total : ", )

        print("sueldos superior a 2.200.000")
        print("total : ", )




    if opc==3:
        print("sueldo mas alto : ")

        print("sueldo mas bajo : ")

        print("promedio de sueldos : ")

        print("media geometrica : ")






    if opc==4:
        print("decuento salud : 7%")
        print("descuento AFP : 12% ")
        print("sueldo liquido : ")




    if opc==5:
        print("Finalizando programa""\n""Desarrolado por Felix Santillan ""\n" "RUT : 25423586-5")


    















