from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Aluno:
	id: int
	nome: str
	curso: str

class NoAluno:
	def __init__(self, aluno: Aluno):
		self.aluno = aluno
		self.proximo: Optional['NoAluno'] = None

class ListaAlunos:
	def __init__(self):
		self.cabeca: Optional[NoAluno] = None

	def cadastrar_aluno(self, id: int, nome: str, curso: str) -> None:
		novo = NoAluno(Aluno(id, nome, curso))
		novo.proximo = self.cabeca
		self.cabeca = novo

	def remover_aluno_por_id(self, id: int) -> bool:
		prev = None
		cur = self.cabeca
		while cur:
			if cur.aluno.id == id:
				if prev:
					prev.proximo = cur.proximo
				else:
					self.cabeca = cur.proximo
				return True
			prev = cur
			cur = cur.proximo
		return False

	def buscar_por_id(self, id: int) -> Optional[Aluno]:
		cur = self.cabeca
		while cur:
			if cur.aluno.id == id:
				return cur.aluno
			cur = cur.proximo
		return None

	def listar_alunos(self) -> List[Aluno]:
		out: List[Aluno] = []
		cur = self.cabeca
		while cur:
			out.append(cur.aluno)
			cur = cur.proximo
		return out

if __name__ == '__main__':
	lista = ListaAlunos()
	lista.cadastrar_aluno(101, 'Ana', 'Engenharia')
	lista.cadastrar_aluno(102, 'Bruno', 'Matemática')
	lista.cadastrar_aluno(103, 'Carla', 'Física')
	print('Alunos cadastrados:', lista.listar_alunos())
	print('Buscar id=102:', lista.buscar_por_id(102))
	lista.remover_aluno_por_id(101)
	print('Após remoção id=101:', lista.listar_alunos())

