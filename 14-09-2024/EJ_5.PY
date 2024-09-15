print("Programa para poder aplicar descuentos a una tienda de Ropa")
print("El cliente es VIP? (1. SI / 2. NO)")
VIP = int(input())
print("Ingrese el total de la compra")
total = float(input())
if total >= 1000:
    descuento = .10
    if VIP == 1:
        descuento = descuento + .05
    total = total - (total * descuento)
    print("El total a pagar con descuento es: ", total)
elif total >= 500:
    descuento = .05
    if VIP == 1:
        descuento = descuento + .05
        print("DESCUENTO", descuento)
    total = total - (total * descuento)
    print("El total a pagar con descuento es: ", total)
else:
    print("No aplica descuento")
    print("El total a pagar es: ", total)