import keyboard
from math import sqrt
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

ascii_art = """
 _______  _______  ______    __   __    _______  _______  _______  __   __ 
|       ||   _   ||    _ |  |  |_|  |  |       ||       ||       ||  | |  |
|    ___||  |_|  ||   | ||  |       |  |_     _||    ___||       ||  |_|  |
|   |___ |       ||   |_||_ |       |    |   |  |   |___ |       ||       |
|    ___||       ||    __  ||       |    |   |  |    ___||      _||       |
|   |    |   _   ||   |  | || ||_|| |    |   |  |   |___ |     |_ |   _   |
|___|    |__| |__||___|  |_||_|   |_|    |___|  |_______||_______||__| |__|
"""

"""
EXECUTE O PROGRAMA UTILIZANDO O SEGUINTE COMANDO NO TERMINAL:

pyinstaller --onefile --clean --name=FarmTechSolutions --icon=farm.ico farmtech_app.py

"""

dadosPlantio = []

def inputOrEscape(promptMessage):
    while True:
        valor = Prompt.ask(promptMessage)
        if keyboard.is_pressed("esc"):
            return None
        return valor

def digitarCultura():
    culturasValidas = ["soja", "milho", "café", "trigo", "algodao", "amendoim", "feijao"]
    while True:
        cultura = Prompt.ask("Digite o tipo de cultura (soja/milho/café/trigo/etc):").lower()
        if cultura in culturasValidas:
            return cultura
        else:
            console.print("[bold red]Cultura inválida![/bold red]")

def calcularArea(forma):
    if forma == "1":
        comprimento = Prompt.ask("Digite o comprimento (em metros):")
        largura = Prompt.ask("Digite a largura (em metros):")
        return float(comprimento) * float(largura)
    elif forma == "2":
        diametro = Prompt.ask("Digite o diâmetro (em metros):")
        return 3.14 * (float(diametro) / 2) ** 2
    else:
        console.print("[bold red]Forma geométrica inválida![/bold red]")
        return None

def entradaDeDados():
    cultura = digitarCultura()
    if cultura is None:
        return

    console.print("[bold green]Escolha a forma geométrica da área plantada:[/bold green]")
    console.print("[1] Quadrilátero")
    console.print("[2] Círculo")
    forma = Prompt.ask("Escolha a forma (1 ou 2)")

    area = calcularArea(forma)
    if area is not None:
        dadosPlantio.append({"cultura": cultura, "area": area})
        console.print(f"Área calculada para {cultura}: {area} m²")
        Prompt.ask("Pressione Enter para continuar...")

def exibirDados():
    if len(dadosPlantio) == 0:
        console.print("[bold red]Nenhum dado registrado![/bold red]")
        return False
    console.print("[bold green]Dados atuais:[/bold green]")
    for idx, dado in enumerate(dadosPlantio, start=1):
        console.print(f"[{idx}] Cultura: {dado['cultura'].capitalize()}, Área: {dado['area']} m²")
    return True

def atualizarDados():
    if not exibirDados():
        return

    escolha = Prompt.ask("Digite o número da entrada que deseja atualizar")
    if not escolha.isdigit() or not (1 <= int(escolha) <= len(dadosPlantio)):
        console.print("[bold red]Escolha inválida![/bold red]")
        return

    posicao = int(escolha) - 1
    novaCultura = digitarCultura()

    console.print("[bold green]Escolha a nova forma geométrica da área plantada:[/bold green]")
    console.print("[1] Quadrilátero")
    console.print("[2] Círculo")
    novaForma = Prompt.ask("Escolha a forma (1 ou 2)")

    novaArea = calcularArea(novaForma)
    if novaArea is not None:
        dadosPlantio[posicao] = {"cultura": novaCultura, "area": novaArea}
        console.print(f"[bold green]Dados atualizados para posição {posicao + 1}.[/bold green]")
        Prompt.ask("Pressione Enter para continuar...")

def deletarDados():
    if not exibirDados():
        return

    escolha = Prompt.ask("Digite o número da entrada que deseja deletar")
    if not escolha.isdigit() or not (1 <= int(escolha) <= len(dadosPlantio)):
        console.print("[bold red]Escolha inválida![/bold red]")
        return

    posicao = int(escolha) - 1
    deletado = dadosPlantio.pop(posicao)
    console.print(f"[bold red]Dados da cultura {deletado['cultura'].capitalize()} foram deletados com sucesso![/bold red]")
    Prompt.ask("Pressione Enter para continuar...")

def menu():
    while True:
        console.clear()
        console.print(ascii_art, style="green")

        console.print("[bold white]Menu:[/bold white]")
        console.print("[bold white][1] Inserir nova cultura e calcular área[/bold white]")
        console.print("[bold white][2] Atualizar dados[/bold white]")
        console.print("[bold white][3] Deletar dados[/bold white]")
        console.print("[bold white][4] Exibir todos os dados[/bold white]")
        console.print("[bold white][0] Sair do programa[/bold white]")

        escolha = Prompt.ask("[bold white]Escolha uma opção[/bold white]")

        if escolha == "1":
            entradaDeDados()
        elif escolha == "2":
            atualizarDados()
        elif escolha == "3":
            deletarDados()
        elif escolha == "4":
            exibirDados()
            Prompt.ask("[bold white]Pressione Enter para voltar ao menu...[/bold white]")
        elif escolha == "0":
            console.print("[bold red]Saindo do programa...[/bold red]")
            break
        else:
            console.print("[bold red]Opção inválida![/bold red]")
            Prompt.ask("[bold white]Pressione Enter para continuar...[/bold white]")

if __name__ == "__main__":
    menu()
