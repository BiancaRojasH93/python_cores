from usuariosConTarjetaCredito.tarjetasUsuarios import tarjetaCredito

class Usuario:


    def __init__(self, nombre, apellido, email):

        self.nombre = nombre

        self.apellido = apellido

        self.email = email

        self.tarjetaCredito = tarjetaCredito (0, 20000, 0.015)



    def hacer_compra(self, monto):

        self.tarjetaCredito.compra(monto)
        return self

    def pagar_tarjeta(self, monto):

        self.tarjetaCredito.pago(monto)
        return self

    def mostrar_saldo_usuario(self):

        self.tarjetaCredito.mostrar_info_tarjeta()
        return self

miyagi = Usuario("Miyagi", "Nariyoshi", "miyagi@hotmail.cl")
daniel = Usuario("Daniel", "Lazaro", "daniloco@hotmail.cl")
fabrizio = Usuario("Fabrizio", "Madero", "pinocho@hotmail.cl")

miyagi.hacer_compra(50)
miyagi.hacer_compra(70)
miyagi.pagar_tarjeta(80)
miyagi.mostrar_saldo_usuario()

daniel.hacer_compra(100)
daniel.pagar_tarjeta(750)
daniel.pagar_tarjeta(250)
daniel.mostrar_saldo_usuario()

fabrizio.hacer_compra(200)
fabrizio.hacer_compra(200)
fabrizio.hacer_compra(200)
fabrizio.pagar_tarjeta(150)
fabrizio.pagar_tarjeta(150)
fabrizio.pagar_tarjeta(150)
fabrizio.pagar_tarjeta(150)
fabrizio.mostrar_saldo_usuario()