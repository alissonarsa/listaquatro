from typing import Optional, List

class NoMusica:
	def __init__(self, titulo: str, artista: str):
		self.titulo = titulo
		self.artista = artista
		self.proximo: Optional['NoMusica'] = None

	def __repr__(self):
		return f"{self.titulo} - {self.artista}"


class PlaylistEncadeada:
	def __init__(self):
		self.cabeca: Optional[NoMusica] = None
		self.atual: Optional[NoMusica] = None

	def adicionar_musica(self, titulo: str, artista: str) -> None:
		novo = NoMusica(titulo, artista)
		if not self.cabeca:
			self.cabeca = novo
			self.atual = novo
			return
		cur = self.cabeca
		while cur.proximo:
			cur = cur.proximo
		cur.proximo = novo

	def remover_musica_por_titulo(self, titulo: str) -> bool:
		prev = None
		cur = self.cabeca
		while cur:
			if cur.titulo == titulo:
				if prev:
					prev.proximo = cur.proximo
				else:
					self.cabeca = cur.proximo
				if self.atual is cur:
					self.atual = cur.proximo if cur.proximo else self.cabeca
				return True
			prev = cur
			cur = cur.proximo
		return False

	def musica_atual(self) -> Optional[NoMusica]:
		return self.atual

	def listar_musicas(self) -> List[str]:
		out = []
		cur = self.cabeca
		while cur:
			out.append(repr(cur))
			cur = cur.proximo
		return out


if __name__ == '__main__':
	p = PlaylistEncadeada()
	p.adicionar_musica('Imagine', 'John Lennon')
	p.adicionar_musica('Heroes', 'David Bowie')
	p.adicionar_musica('No Surprises', 'Radiohead')
	print('Lista de músicas:', p.listar_musicas())
	print('Atual:', p.musica_atual())
	p.remover_musica_por_titulo('Heroes')
	print('Após remover "Heroes":', p.listar_musicas())

