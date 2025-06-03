import json
from pathlib import Path
from typing import List, Dict

class History:
    """
    Permite gerenciar um histórico de operações:
    - armazena cada cálculo como um dicionário {"operacao": ..., "resultado": ...}
    - salva/recupera de um arquivo JSON
    """

    def __init__(self, path: Path):
        self._path = path
        # Se o arquivo existir, carrega o histórico; senão, inicializa lista vazia
        if self._path.exists():
            with open(self._path, "r", encoding="utf-8") as f:
                self._data: List[Dict] = json.load(f)
        else:
            self._data: List[Dict] = []

    def add_entry(self, operacao: str, resultado):
        """Adiciona uma nova entrada ao histórico e persiste no arquivo."""
        entry = {"operacao": operacao, "resultado": resultado}
        self._data.append(entry)
        self._save()

    def get_all(self) -> List[Dict]:
        """Retorna todas as entradas (lista de dicionários)."""
        return list(self._data)  # retorna cópia para não expor internamente

    def clear(self):
        """Limpa o histórico (lista vazia e reseta o arquivo)."""
        self._data = []
        self._save()

    def _save(self):
        """Grava o conteúdo atual de _data no arquivo JSON."""
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2)
