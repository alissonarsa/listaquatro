from typing import Optional, List

class NoJogador:
	def __init__(self, nome: str):
		self.nome = nome
		self.proximo: Optional['NoJogador'] = None

	def __repr__(self):
		return self.nome

class RodizioCircular:
	def __init__(self):
		# 'atual' aponta para um nó do círculo; nó.proximo forma o círculo
		self.atual: Optional[NoJogador] = None

	def adicionar_jogador(self, nome: str) -> None:
		novo = NoJogador(nome)
		if not self.atual:
			novo.proximo = novo
			self.atual = novo
			return
		# inserir após atual
		novo.proximo = self.atual.proximo
		self.atual.proximo = novo

	def remover_jogador_por_nome(self, nome: str) -> bool:
		if not self.atual:
			return False
		prev = self.atual
		cur = self.atual.proximo
		# caso único
		if cur is prev and cur.nome == nome:
			self.atual = None
			return True
		start = prev
		while True:
			if cur.nome == nome:
				prev.proximo = cur.proximo
				if cur is self.atual:
					# mover ponteiro atual para prev (ou outro) para manter consistência
					self.atual = prev
				return True
			prev = cur
			cur = cur.proximo
			if prev is start:
				break
		return False

	def proximo(self) -> Optional[str]:
		if not self.atual:
			return None
		self.atual = self.atual.proximo
		return self.atual.nome

	def jogador_atual(self) -> Optional[str]:
		return self.atual.nome if self.atual else None

	def listar_membros(self) -> List[str]:
		out: List[str] = []
		if not self.atual:
			return out
		out.append(self.atual.nome)
		cur = self.atual.proximo
		while cur is not self.atual:
			out.append(cur.nome)
			cur = cur.proximo
		return out

if __name__ == '__main__':
	r = RodizioCircular()
	r.adicionar_jogador('Player1')
	r.adicionar_jogador('Player2')
	r.adicionar_jogador('Player3')
	print('Membros:', r.listar_membros())
	print('Atual:', r.jogador_atual())
	print('Avança para:', r.proximo())
	r.remover_jogador_por_nome('Player2')
	print('Após remover Player2:', r.listar_membros())

