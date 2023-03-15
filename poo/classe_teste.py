class Filme:
    #construtor da classe
    def __init__(self, titulo, duracao_em_minutos):
        self.titulo = titulo
        self.duracao_em_minutos = duracao_em_minutos



    #atributos
    def exibir_duracao_em_horas(self):
        h = self.duracao_em_minutos // 60
        min = self.duracao_em_minutos % 60 
        print(f"O filme {self.titulo} possui {h} horas e {min} minutos de duração")







