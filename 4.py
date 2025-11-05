from typing import Optional, List, Tuple

class NoHistorico:
	def __init__(self, url: str):
		self.url = url
		self.anterior: Optional['NoHistorico'] = None
		self.proximo: Optional['NoHistorico'] = None

	def __repr__(self):
		return f"{self.url}"


class HistoricoNavegacao:
	def __init__(self):
		self.cabeca: Optional[NoHistorico] = None
		self.cauda: Optional[NoHistorico] = None
		self.atual: Optional[NoHistorico] = None

	def visitar(self, url: str) -> None:
		novo = NoHistorico(url)
		if not self.cabeca:
			self.cabeca = self.cauda = self.atual = novo
			return
		# se houver forward (próximos) a partir do atual, removemos esses nós
		if self.atual and self.atual.proximo:
			self.atual.proximo.anterior = None
			self.atual.proximo = None
			self.cauda = self.atual
		# anexar novo
		if self.cauda:
			self.cauda.proximo = novo
			novo.anterior = self.cauda
			self.cauda = novo
		else:
			self.cabeca = self.cauda = novo
		self.atual = novo

	def voltar(self) -> Optional[str]:
		if self.atual and self.atual.anterior:
			self.atual = self.atual.anterior
		return self.atual.url if self.atual else None

	def avancar(self) -> Optional[str]:
		if self.atual and self.atual.proximo:
			self.atual = self.atual.proximo
		return self.atual.url if self.atual else None

	def url_atual(self) -> Optional[str]:
		return self.atual.url if self.atual else None

	def listar_historico(self) -> List[Tuple[str, bool]]:
		out: List[Tuple[str, bool]] = []
		cur = self.cabeca
		while cur:
			out.append((cur.url, cur is self.atual))
			cur = cur.proximo
		return out


if __name__ == '__main__':
	h = HistoricoNavegacao()
	h.visitar('https://exemplo.com')
	h.visitar('https://openai.com')
	h.visitar('https://python.org')
	print('Histórico:', h.listar_historico())
	h.voltar()
	print('Após voltar, atual:', h.url_atual())
	h.avancar()
	print('Após avançar, atual:', h.url_atual())

