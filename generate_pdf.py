import os
from io import BytesIO
import argparse
from fpdf import FPDF
from PyPDF2 import PdfMerger, PdfReader
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random

# Função para gerar uma imagem PNG com cor e número da página
def create_sample_png(image_path):
    # Gera uma cor aleatória
    color = tuple(random.randint(0, 255) for _ in range(3))
    # Cria uma imagem com a cor gerada
    img = Image.new('RGB', (200, 200), color=color)
    d = ImageDraw.Draw(img)
    try:
        # Tenta carregar uma fonte de sistema
        font = ImageFont.truetype("arial", 20)
    except IOError:
        # Usa uma fonte padrão se a fonte de sistema não estiver disponível
        font = ImageFont.load_default()
    d.text((50, 90), "Sample", fill=(255, 255, 255), font=font)
    img.save(image_path)

# Função para gerar uma parte do PDF com imagens
def generate_pdf_part_with_images(image_path, num_pages):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=False, margin=0)
    for _ in range(num_pages):
        pdf.add_page()
        pdf.image(image_path, x=10, y=10, w=190)  # Adiciona a imagem na página
    buffer = BytesIO()
    pdf.output(buffer)
    return buffer.getvalue()

# Função para gerar um PDF grande
def create_large_pdf(file_name="default_large_file.pdf", size_mb=10, image_path="sample_image.png"):
    target_size_bytes = size_mb * 1024 * 1024

    # Inicializa o PDF Merger
    merger = PdfMerger()

    # Gera a imagem uma vez no início
    create_sample_png(image_path)

    # Adiciona timestamp ao nome do arquivo
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    base_name, ext = os.path.splitext(file_name)
    file_name_with_timestamp = f"{base_name}_{timestamp}{ext}"

    # Define o caminho para a pasta downloads dentro do projeto
    downloads_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(downloads_dir, exist_ok=True)
    downloads_path = os.path.join(downloads_dir, file_name_with_timestamp)

    # Abre o arquivo final para escrita
    with open(downloads_path, "wb") as f:
        page_count = 0
        start_time = datetime.now()
        while True:
            part = generate_pdf_part_with_images(image_path, 10)  # Gerar uma parte com 10 páginas
            part_buffer = BytesIO(part)
            merger.append(part_buffer)
            page_count += 10

            # Escreve a parte no arquivo final
            merger.write(f)
            temp_size = f.tell()
            progress = (temp_size / target_size_bytes) * 100
            print(f"Progresso: {progress:.2f}% concluído.")
            if temp_size >= target_size_bytes:
                break

        merger.close()

    # Verifica o número real de páginas no PDF gerado
    with open(downloads_path, "rb") as f:
        reader = PdfReader(f)
        actual_page_count = len(reader.pages)
    
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"{downloads_path} criado com sucesso!")
    print(f"Tempo total do processo: {total_time}")
    print(f"Total de páginas no arquivo gerado: {actual_page_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerar um PDF grande com tamanho especificado.")
    parser.add_argument("--file_name", type=str, default="default_large_file.pdf", help="Nome do arquivo PDF a ser criado.")
    parser.add_argument("--size_mb", type=int, default=10, help="Tamanho alvo do arquivo PDF em MB.")
    parser.add_argument("--image_path", type=str, default="sample_image.png", help="Caminho da imagem a ser adicionada ao PDF.")
    
    args = parser.parse_args()
    
    create_large_pdf(args.file_name, args.size_mb, args.image_path)