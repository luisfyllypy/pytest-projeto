from pathlib import Path
from calculadora.operations import soma
from calculadora.history import History

# Caminho do arquivo JSON (na raiz do projeto)
caminho_arquivo = Path("historico.json")

# Cria o histórico (vai carregar se já existir ou criar do zero)
historico = History(caminho_arquivo)

# Realiza uma operação
resultado = soma(10, 5)
print(f"Resultado : {resultado}")

# Salva no histórico
historico.add_entry("soma(10, 5)", resultado)

# Mostra tudo que tem no histórico
print("Histórico de operações:")
for item in historico.get_all():
    print(f"{item['operacao']} = {item['resultado']}")