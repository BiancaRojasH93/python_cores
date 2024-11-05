class tarjetaCredito:

    def __init__(self, saldo_pagar, limite_credito, intereses):

        self.saldo_pagar= saldo_pagar
        self.limite_credito= limite_credito
        self.intereses= intereses

    def compra(self, monto):

        if self.saldo_pagar + monto < self.limite_credito:
            self.saldo_pagar += monto
            print(f"Se ha efectuado una compra de {monto}")
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de credito")
        return self


    def pago(self, monto):

        self.saldo_pagar -= monto
        print(f"Ha hecho un pago por {monto}")
        print(f"Su saldo actual es {self.saldo_pagar}")
        return self


    def mostrar_info_tarjeta(self):

        print(self.saldo_pagar)
        return self


    def cobrar_interes(self):

        self.saldo_pagar= (self.saldo_pagar * self.intereses) + self.saldo_pagar
        print(f"El saldo total con intereses es {self.saldo_pagar}")
        return self
    


pepito = tarjetaCredito(0, 500000, 0.03)
polilla = tarjetaCredito(0, 300000, 0.02)
figaro = tarjetaCredito(0, 400000, 0.025)

pepito.compra(50000).compra(150000).pago(100000).cobrar_interes().mostrar_info_tarjeta()

polilla.compra(25000).compra(50000).compra(100000).pago(25000).pago(100000).cobrar_interes().mostrar_info_tarjeta()

figaro.compra(50000).compra(80000).compra(75000).compra(150000).compra(50000).mostrar_info_tarjeta()
