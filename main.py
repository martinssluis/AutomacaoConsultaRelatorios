import os
import shutil
import subprocess
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox

# Função para solicitar entrada do usuário e validar a data
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Solicita a data no formato DDMMYYYY e tenta converter para um objeto datetime
    data = simpledialog.askstring("Input", "Informe a data no formato DDMMYYYY:")
    if data is None:
        return None, None  # Se o usuário cancelar

    try:
        datetime.strptime(data, "%d%m%Y")
    except ValueError:
        messagebox.showerror("Erro", "Data inválida! Use o formato DDMMYYYY.")
        return get_user_input()

    # Lista de tipos de relatório válidos
    tipos_validos = ["FCBR15", "FCBR21", "FCBR30", "FCBR42", "FCBR423", "FCBRN31"]
    
    # Mostra as opções numeradas para o usuário escolher
    tipo_opcoes = "\n".join([f"{i + 1}. {tipo}" for i, tipo in enumerate(tipos_validos)])
    tipo_relatorio_input = simpledialog.askstring("Escolha", f"Escolha o tipo de relatório:\n{tipo_opcoes}")
    
    if tipo_relatorio_input is None:
        return None, None  # Se o usuário cancelar

    # Valida a entrada do usuário
    try:
        escolha = int(tipo_relatorio_input)
        if 1 <= escolha <= len(tipos_validos):
            tipo_relatorio = tipos_validos[escolha - 1]
        else:
            raise ValueError("Escolha inválida!")
    except ValueError:
        messagebox.showerror("Erro", "Escolha inválida! Digite um número entre 1 e 6.")
        return get_user_input()

    return data, tipo_relatorio

def copy_and_open_file(directory, date, report_type):
    # Formata o nome do arquivo baseado na entrada do usuário
    filename = f"AOM_{date}_013056_FCB_{report_type}"
    file_path = os.path.join(directory, filename)

    # Verifica se o arquivo existe
    if os.path.exists(file_path):
        print(f"Arquivo encontrado: {file_path}")

        # Converte a data fornecida pelo usuário para um objeto datetime
        user_date = datetime.strptime(date, "%d%m%Y")
        # Define os novos diretórios base onde serão salvos os arquivos
        base_directories = [r"Z:\Automatizacao\TratamentoRelatorios", r"Z:\AOM\TXT"]

        for base_directory in base_directories:
            # Define o diretório do tipo de relatório
            report_type_directory = os.path.join(base_directory, report_type)

            # Define o diretório do ano
            year_directory = os.path.join(report_type_directory, str(user_date.year))
            # Cria o diretório do ano se ele não existir
            os.makedirs(year_directory, exist_ok=True)

            # Define o diretório MesAno
            month_year_directory = os.path.join(year_directory, user_date.strftime('%m%Y'))
            # Cria o diretório MesAno se ele não existir
            os.makedirs(month_year_directory, exist_ok=True)

            # Define o novo nome do arquivo com extensão .txt
            new_filename = f"{report_type}_{date}.txt"
            # Define o caminho completo do novo arquivo
            new_file_path = os.path.join(month_year_directory, new_filename)

            # Copia o arquivo original para o novo diretório com o novo nome
            shutil.copy(file_path, new_file_path)
            print(f"Cópia do arquivo salva em: {new_file_path}")

        # Abre o arquivo copiado no primeiro caminho
        os.startfile(new_file_path)
    else:
        print(f"Arquivo não encontrado: {file_path}")
        # Abre o gerenciador de arquivos no diretório especificado se o arquivo não for encontrado
        subprocess.run(['explorer', directory])

def main():
    while True:
        # Diretório onde os arquivos originais estão localizados
        directory = r"\\sta340224\AOM\FCB"
        # Solicita a data e o tipo de relatório ao usuário
        date, report_type = get_user_input()
        
        if date is None:  # Se o usuário cancelar, saia do loop
            break
        
        # Copia e abre o arquivo baseado na entrada do usuário
        copy_and_open_file(directory, date, report_type)
        
        # Pergunta ao usuário se deseja processar outro relatório
        continuar = simpledialog.askstring("Continuar", "Deseja processar outro relatório? (s/n):")
        if continuar is None or continuar.strip().lower() != 's':
            break

# Ponto de entrada do script
if __name__ == "__main__":
    main()
