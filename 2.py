from typing import Optional, List

class NoMusica:
	def __init__(self, titulo: str, artista: str):
		self.titulo = titulo
		self.artista = artista
		self.proximo: Optional['NoMusica'] = None

	def __repr__(self):
		return f"{self.titulo} - {self.artista}"


class PlaylistComNavegacao:
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

	def avancar(self) -> Optional[NoMusica]:
		if not self.atual:
			return None
		if self.atual.proximo:
			self.atual = self.atual.proximo
		# se não há próximo, mantém no final
		return self.atual

	def retroceder(self) -> Optional[NoMusica]:
		if not self.cabeca or not self.atual or self.atual is self.cabeca:
			return self.atual
		prev = None
		cur = self.cabeca
		while cur and cur is not self.atual:
			prev = cur
			cur = cur.proximo
		if prev:
			self.atual = prev
		return self.atual

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
	p = PlaylistComNavegacao()
	p.adicionar_musica('Blinding Lights', 'The Weeknd')
	p.adicionar_musica('Levitating', 'Dua Lipa')
	p.adicionar_musica('Bad Guy', 'Billie Eilish')
	print('Playlist:', p.listar_musicas())
	print('Atual:', p.musica_atual())
	p.avancar()
	print('Após avançar:', p.musica_atual())
	p.retroceder()
	print('Após retroceder:', p.musica_atual())

