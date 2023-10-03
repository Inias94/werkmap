def ruweschatter(getal):
    i =0
    vermenigvuldiger = 1
    while vermenigvuldiger * vermenigvuldiger <= getal:
        i+=1
    return vermenigvuldiger-1, i

def vierkantswortel(getal, factor=0.001):
    start, i = ruweschatter(getal)
    vermenigvuldiger = start + factor

    while factor < getal - vermenigvuldiger * vermenigvuldiger and vermenigvuldiger * vermenigvuldiger < getal:
        vermenigvuldiger += 1
        i+= 1
    return vermenigvuldiger, i

vierkantswortel(54000)