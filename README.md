# Automação de Consulta e Salvamento de Relatórios Diários

Este projeto visa automatizar o processo de consulta e salvamento de relatórios diários. O código facilita a busca e o armazenamento de relatórios frequentemente utilizados, organizando-os em diretórios específicos por tipo, ano e mês, simplificando o acesso futuro.

## Descrição do Projeto

Este script em Python solicita ao usuário uma data e o tipo de relatório desejado, busca o arquivo correspondente em um diretório padrão e, se encontrado, cria cópias organizadas em subdiretórios específicos. Caso o arquivo não seja localizado, o gerenciador de arquivos é aberto no diretório padrão, permitindo ao usuário procurar o arquivo manualmente.

### Objetivo

A automação visa:

- Reduzir o tempo necessário para encontrar e salvar relatórios diários.
- Organizar os relatórios de forma estruturada, facilitando consultas e referências.
- Manter uma estrutura de armazenamento clara, organizada por ano e mês.

## Tecnologias e Bibliotecas Utilizadas

O script utiliza as seguintes bibliotecas e módulos:

- **os**: Permite operações de sistema, como verificar a existência de arquivos e manipular diretórios.
- **shutil**: Facilita a cópia de arquivos para diferentes diretórios.
- **subprocess**: Utilizado para abrir o gerenciador de arquivos quando um relatório não é encontrado.
- **datetime**: Manipula e valida as datas fornecidas pelo usuário.
- **tkinter**: Cria uma interface gráfica simplificada para entrada de dados do usuário.

## Estrutura e Funcionamento do Código

1. **Entrada do Usuário**:
   - A função `get_user_input()` solicita a data e o tipo de relatório via interface gráfica usando `tkinter`.
   - A data é inserida no formato `DDMMYYYY` e validada para garantir que seja uma data válida.
   - O usuário escolhe o tipo de relatório de uma lista predefinida.

2. **Cópia e Organização do Arquivo**:
   - A função `copy_and_open_file()` verifica se o arquivo existe no diretório padrão (`\\sta340224\AOM\FCB`).
   - Se o arquivo é encontrado, ele é copiado para os diretórios de destino organizados por tipo de relatório, ano e mês (ex.: `Z:\Automatizacao\TratamentoRelatorios\Tipo\Ano\Mês`).
   - O novo arquivo é renomeado com base no tipo e na data fornecidos pelo usuário.

3. **Processamento Contínuo**:
   - Após processar um relatório, o usuário é questionado se deseja processar outro.
   - O script permanece em um loop até que o usuário escolha encerrar.

## Uso do Script

1. Certifique-se de que todas as dependências do Python estão instaladas.
2. Execute o script e insira a data e o tipo de relatório quando solicitado.
3. O arquivo será buscado, copiado e organizado nos diretórios especificados.
4. Se o arquivo não for encontrado, o gerenciador de arquivos será aberto no diretório padrão.


