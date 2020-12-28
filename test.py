class Carro:
    def __init__(self):
        self.componentes = {
            "rodas": 4,
            "material": "carbono",
            "combustivel": {
                "tipo": "gasolina",
                "quantidade": 100
            },
            "volante": 1,
            "retrovisor": 2,
            "step": False,
        }

    def andar(self):
        self.componentes["combustivel"]["quantidade"] -= 10
    

ok = Carro()
ok.andar()
print(ok.componentes)