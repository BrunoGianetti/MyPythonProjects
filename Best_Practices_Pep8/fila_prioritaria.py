from typing import Union

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO
from estatística_resumida import EstatisticaResumida
from estatística_detalhada import EstatisticaDetalhada

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}'

    def estatistica(self, retorna_estatística: Classes) -> dict:

        return retorna_estatística.roda_estatistica(self.clientes_atendidos)
