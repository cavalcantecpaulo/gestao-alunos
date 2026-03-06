from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    rm: int
    curso: str
    mensalidade: float

    def exibir_informacoes(self):
        print(f"\n    RM{self.rm} | {self.nome}")
        print(f"    Curso: {self.curso} | Mensalidade: R${self.mensalidade}")