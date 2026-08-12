import builtins

# 1. Truque para importar o Converter.py sem ativar o prompt de input dele
input_original = builtins.input
builtins.input = lambda *args: ""  # Desativa o input temporariamente
import Converter
builtins.input = input_original  # Restaura o input original


def obter_dados_binarios(texto):
    """
    Usa a função do Converter.py para gerar os dados binários do texto.
    """
    return Converter.texto_para_binario(texto)


def ocultar_mensagem_na_imagem(caminho_original, caminho_saida, texto_mensagem):
    # 2. Obter a mensagem convertida em binário (0s e 1s)
    dados_binarios = obter_dados_binarios(texto_mensagem)
    print(f"Dados binários gerados para esconder: {dados_binarios}")
    
    # Marcador para identificar onde começa a mensagem na leitura binária
    marcador = b"##INICIO##"
    
    # 3. Ler os bytes da imagem original (Foto1.jpg)
    with open(caminho_original, 'rb') as f:
        bytes_imagem = f.read()
        
    # 4. Juntar os bytes da imagem + marcador + os bytes da mensagem binária
    dados_finais = bytes_imagem + marcador + dados_binarios.encode('utf-8')
    
    # 5. Salvar a nova imagem (Foto_Secreta.jpg)
    with open(caminho_saida, 'wb') as f:
        f.write(dados_finais)
        
    print(f"Sucesso! Nova imagem gerada em: {caminho_saida}")


# --- Executa o processo ---
if __name__ == "__main__":
    mensagem = input("Digite a frase para ocultar na imagem: ")
    ocultar_mensagem_na_imagem("Foto1.jpg", "Foto_Secreta.jpg", mensagem)