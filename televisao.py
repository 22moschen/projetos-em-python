class Televisao:
    def __init__(self):
        self.ligada = false

        def power(self):
            if self.ligada:
                self.ligada = false
            else:
                self.ligada = true
televisao = Televisao()
print('televisão está ligada : {} '.format(televisao.ligada))
televisao.power()
print('televisão está ligada : {} '.format(televisao.ligada))
televisao.power()
print('televisão está ligada : {} '.format(televisao.ligada))