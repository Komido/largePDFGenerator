
# Large PDF Generator Script

Este projeto contém um script Python que gera um arquivo PDF grande para fins de teste de upload. O PDF é gerado com páginas que contêm uma imagem colorida aleatória e um texto de exemplo.

## Pré-requisitos

Certifique-se de que você tem os seguintes requisitos instalados:

- Python 3
- Virtualenv
- Bibliotecas Python: `fpdf`, `PyPDF2`, `Pillow`

Para instalar as bibliotecas necessárias, ative seu ambiente virtual e execute:

```bash
pip install fpdf PyPDF2 Pillow
```

## Passo a Passo para Configuração e Execução

1. **Clone o Repositório e Navegue até o Diretório:**
   ```bash
   cd /caminho/para/Projetos/Python/pdfGenerate
   ```

2. **Crie um Ambiente Virtual:**
   ```bash
   python3 -m venv venv
   ```

3. **Ative o Ambiente Virtual:**
   - No macOS ou Linux:
     ```bash
     source venv/bin/activate
     ```
   - Verifique se o ambiente virtual foi ativado corretamente, pois o nome do ambiente virtual aparecerá no início da linha de comando. Por exemplo:
     ```bash
     (venv) user@hostname:/caminho/para/Projetos/Python/pdfGenerate$
     ```
     ou ue o camando `which python3` e `which pip` para verificar se o Python e o pip estão apontando para o ambiente virtual.
     

4. **Instale as Dependências Necessárias:**
   ```bash
   pip install fpdf PyPDF2 Pillow
   ```

5. **Execute o Script para Gerar o PDF:**
   - Use o seguinte comando para executar o script Python, especificando o tamanho desejado do PDF em megabytes (MB):
   ```bash
   python generate_large_pdf.py --file_name nome_do_arquivo.pdf --size_mb 100 --image_path caminho_da_imagem.png
   ```

   - Parâmetros:
     - `--file_name`: Nome do arquivo PDF a ser gerado. (padrão: `default_large_file.pdf`)
     - `--size_mb`: Tamanho alvo do arquivo PDF em MB. (padrão: `10`)
     - `--image_path`: Caminho da imagem a ser adicionada ao PDF. (padrão: `sample_image.png`)

6. **Desative o Ambiente Virtual:**
   - Quando terminar de usar o script, você pode desativar o ambiente virtual:
     ```bash
     deactivate
     ```

## O que o Script Faz

O script `generate_large_pdf.py` utiliza a biblioteca `fpdf` para criar um PDF com várias páginas, cada uma contendo uma imagem gerada aleatoriamente. Ele cria partes do PDF e as mescla usando `PyPDF2` até atingir o tamanho especificado. Isso é útil para testes de upload em plataformas que exigem arquivos grandes.

## Contato

Para qualquer dúvida ou sugestão, entre em contato com Daniel Tsuneo através de tsuneokomido@gmail.com.
