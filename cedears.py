# TICKER || CANT || FECHA || PRECIO INICIAL || PRECIO ACTUAL || DOLAR INICIAL || DOLAR ACTUAL
# BABA   ||  3   || 00/00 ||                || 29628.99      ||               ||
# GOOGL  ||  19  || 00/00 ||                || 62232.98      ||               ||
# AMNZ   ||  20  || 00/00 ||                || 27732.40      ||               ||
# INTC   ||  4   || 00/00 ||                || 49792.28      ||               ||
# NVDA   ||  1   || 00/00 ||                || 32257.29      ||               ||
# SHOP   ||  2   || 00/00 ||                || 1941.54       ||               ||
#
# 203585.48
# 1240
#
# COMPRA || CANT || PRECIO ||   PDD   || TOTAL || FECHA
# GOOGL1 =  10      807.01    433.87    8070.1    20/04
# AMZN1 =   1       319.16    433.87    319.16    20/04
# GOOGL2 =  4       830.01    448.55    3320.04   21/04
# AMZN2 =   5       342.83    448.55    1714.15   21/04
# AMZN3 =   12      349.98    471.66    4199.76   25/04
# GOOGL3 =  5       879.02    471.66    4395.1    25/04
# BABA =    3       4380.82   483.5     13142.46  31/05
# INTC =    4       3700.29   533       14801.16  25/07
# AMNZ4 =   2       706.55    740.8     1413.1    24/08
# NVDA =    1       13966.63  726.5     13966.63  11/09


def menu():
        print("1) Calcular precio de los CEDEARS en dolares en su momento.")
        print("2) Calcular rendimiento de un CEDEAR en particular.")
        print("3) Sumar CEDEARS en pesos.")
        print("4) Sumar el total de los CEDEARS")
        print("6) Salir.")

def cedears():
    print("1) GOOGL")
    print("2) AMZN")
    print("3) INTC")
    print("4) NVDA")
    print("5) BABA")
    print("6) SHOP")


def incremento_porcentual(periodo1, periodo2):
    incremento = ((periodo2 - periodo1) / periodo1) * 100
    return round(incremento, 2)

def calcular_promedio_total_dolar(v):
    promedio_total = v[4] / v[3]
    return promedio_total

def calcular_promedio_unitario_dolar(v):
    promedio_unitario = v[2] / v[3]
    return promedio_unitario


def compras_a_dolar(wallet):
    dolar_blue_hoy = 1240
    cont = 0
    total_dolares = 0
    for compra in wallet:
        cont += 1
        prom = calcular_promedio_total_dolar(compra)
        total_dolares += prom
        print("la compra", cont, "de", compra[1], "fue de $", round(prom, 2), " dolares")
    print("-----------------------------------------------------------------")
    print("el total de dolares fue de: $", round(total_dolares, 2))
    print("Hoy en dia serian:", round(round(total_dolares, 2) * dolar_blue_hoy, ), "pesos")
    return total_dolares


def suma_en_pesos(wallet):
    total = 0
    for precio in wallet:
        total += precio[4]
    return total

def promedio_de_compra(wallet, cedear):
    acum = 0
    cont = 0
    for c in wallet:
        if c[1] == cedear:
            acum += c[2]
            cont += 1
    if cont == 0:
        return None
    else:
        return round(acum / cont, 2)

def precio_actual(wallet):
    total_GOOGL = 0
    total_AMZN = 0
    total_NVDA = 0
    total_SHOP = 0
    total_BABA = 0
    total_INTC = 0

    GOOGL_hoy = 3359.69
    GOOGL_cont = 0
    AMZN_hoy = 1424.18
    AMZN_cont = 0
    NVDA_hoy = 33128.15
    NVDA_cont = 0
    SHOP_hoy = 1000.47
    SHOP_cont = 0
    BABA_hoy = 10140.90
    BABA_cont = 0
    INTC_hoy = 12783.44
    INTC_cont = 0

    for ticker in wallet:
        if ticker[1] == "GOOGL":
            total_GOOGL += ticker[0] * GOOGL_hoy
            GOOGL_cont += ticker[0]
        if ticker[1] == "AMZN":
            total_AMZN += ticker[0] * AMZN_hoy
            AMZN_cont += ticker[0]
        if ticker[1] == "NVDA":
            total_NVDA += ticker[0] * NVDA_hoy
            NVDA_cont += ticker[0]
        if ticker[1] == "SHOP":
            total_SHOP += ticker[0] * SHOP_hoy
            SHOP_cont += ticker[0]
        if ticker[1] == "BABA":
            total_BABA += ticker[0] * BABA_hoy
            BABA_cont += ticker[0]
        if ticker[1] == "INTC":
            total_INTC += ticker[0] * INTC_hoy
            INTC_cont += ticker[0]

    suma_total = total_GOOGL + total_INTC + total_BABA + total_NVDA + total_SHOP + total_AMZN
    print("Tus", GOOGL_cont, "CEDEARS de GOOGL hoy cuestan: $",round(total_GOOGL,2) )
    print("Tus", AMZN_cont, "CEDEARS de AMZN hoy cuestan: $",round(total_AMZN,2) )
    print("Tus", NVDA_cont, "CEDEARS de NVDA hoy cuestan: $",round(total_NVDA,2) )
    print("Tus", SHOP_cont, "CEDEARS de SHOP hoy cuestan: $",round(total_SHOP,2))
    print("Tus", BABA_cont, "CEDEARS de BABA hoy cuestan: $",round(total_BABA,2) )
    print("Tus", INTC_cont, "CEDEARS de INTC hoy cuestan: $",round(total_INTC,2) )
    print("----------------------------------------------------------")
    print("El total es de: $", round(suma_total,2))
    return suma_total


def main():

    compra0 = [2, "SHOP", 132.01, 367.49, 264.02, "20/01"]
    compra1 = [10, "GOOGL", 807.01, 433.87, 8070.1, "20/04"]
    compra2 = [1, "AMZN", 319.16, 433.87, 319.16, "20/04"]
    compra3 = [4, "GOOGL", 830.01, 448.55, 3320.04, "21/04"]
    compra4 = [5, "AMZN", 342.83, 448.55, 1714.15, "21/04"]
    compra5 = [12, "AMZN", 349.98, 471.66, 4199.76, "25/04"]
    compra6 = [5, "GOOGL", 879.02, 471.66, 4395.1, "25/04"]
    compra7 = [3, "BABA", 4380.82, 483.5, 13142.46, "31/05"]
    compra8 = [4, "INTC", 3700.29, 533, 14801.16, "25/07"]
    compra9 = [2, "AMNZ", 706.55, 740.8, 1413.1, "24/08"]
    compra10 = [1, "NVDA", 13966.63, 726.5, 13966.63, "11/09"]

    wallet = [compra0, compra1, compra2, compra3, compra4, compra5, compra6, compra7, compra8, compra9, compra10]
    suma_total_cedears = 0
    suma_total_dolares = 0
    compras_dolar = 0
    dolar_blue_hoy = 1240
    op = 0
    while op != "10":
        menu()
        op = input("Seleccione su opcion: ")
        if op == "1":
            compras_dolar = compras_a_dolar(wallet)

        if op == "2":
            cedears()
            cedear = input("Elige el CEDEAR: ")
            op_2 = promedio_de_compra(wallet,cedear)
            if op_2 == None:
                print("No tienes ese CEDEAR.")
            else:
                print("El CEDEAR", cedear, "tiene un promedio de compra de: ", op_2)
            promedio_de_compra(wallet,cedear)

        if op == "3":
            op_3 = suma_en_pesos(wallet)
            print("La suma de los cedears es de", op_3)

        if op == "4":
            suma_total_cedears = precio_actual(wallet)

        if op == "5":
            if suma_total_cedears == 0:
                print("Tienes que cargar la suma total")
            else:
                print("El precio de tus cedears en dolares es de: $", round(suma_total_cedears / dolar_blue_hoy, 2), "Dolares" )
                suma_total_dolares = round(suma_total_cedears / dolar_blue_hoy, 2)

        if op == "6":
            if suma_total_cedears == 0 or suma_total_dolares == 0 or compras_dolar == 0:
                print("ERROR!! tienes que cargar la cantidad de los cedears en su momento")
            else:
                print("Obtuviste una ganancia de: $", round(suma_total_dolares - compras_dolar, 2)   ,"Dolares")
                print("Que es un: %", incremento_porcentual(compras_dolar, suma_total_dolares) , "Más")



if __name__ == '__main__':
    main()