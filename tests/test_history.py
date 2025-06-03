# tests/test_history.py

import json
import pytest
from pathlib import Path
from calculadora.history import History

@pytest.fixture
def history_path(tmp_path):
    """
    Cria um arquivo JSON vazio em um diretório temporário.
    Retorna o caminho do arquivo para usar nos testes.
    """
    path = tmp_path / "historico_test.json"
    return path

def test_history_inicial_esta_vazio(history_path):
    # Ao instanciar pela primeira vez, o arquivo ainda não existe.
    h = History(history_path)
    assert h.get_all() == []  # Histórico vazio

    # O arquivo ainda não foi criado, porque ainda não chamamos add_entry
    assert not history_path.exists()

def test_add_entry_persiste_no_arquivo(history_path):
    h = History(history_path)
    # Adiciona duas entradas
    h.add_entry("soma(2,3)", 5)
    h.add_entry("divide(10,2)", 5.0)

    # Agora o arquivo deve existir
    assert history_path.exists()

    # Lendo diretamente do arquivo, deve haver exatamente 2 registros
    content = json.loads(history_path.read_text(encoding="utf-8"))
    assert isinstance(content, list)
    assert len(content) == 2
    assert content[0] == {"operacao": "soma(2,3)", "resultado": 5}
    assert content[1] == {"operacao": "divide(10,2)", "resultado": 5.0}

    # get_all() deve refletir o mesmo conteúdo
    all_entries = h.get_all()
    assert all_entries == content

def test_clear_reseta_historico(history_path):
    h = History(history_path)
    # Preenche com 1 entrada
    h.add_entry("multiplica(3,4)", 12)
    assert len(h.get_all()) == 1

    # Agora limpa
    h.clear()
    assert h.get_all() == []

    # E o arquivo JSON deve existir, mas com lista vazia
    content = json.loads(history_path.read_text(encoding="utf-8"))
    assert content == []

def test_history_carrega_dados_existentes(history_path):
    # Escreve manualmente um JSON de duas entradas para simular histórico pré-existente
    sample_data = [
        {"operacao": "soma(1,2)", "resultado": 3},
        {"operacao": "subtrai(5,1)", "resultado": 4},
    ]
    history_path.write_text(json.dumps(sample_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # Ao instanciar, a lista interna deve conter esses dois registros
    h = History(history_path)
    all_entries = h.get_all()
    assert all_entries == sample_data

    # Se adicionarmos mais um, a lista final terá 3
    h.add_entry("divide(8,2)", 4)
    assert len(h.get_all()) == 3
