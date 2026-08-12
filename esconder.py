import builtins

# 1. Truque para importar o Converter.py sem disparar o prompt de input dele
input_original = builtins.input
builtins.input = lambda *args: ""  # Desativa o input temporariamente
import Converter
builtins.input = input_original  # Restaura o input original


def ocultar_mensagem(caminho_imagem_original, caminho_imagem_saida, texto_mensagem):
    # 2. Chama a função texto_para_binario importada do seu Converter.py
    dados_binarios = Converter.texto_para_binario(texto_mensagem)
    print(f"\n[Converter.py] Binário gerado: {dados_binarios}")
    
    # Marcador para identificar onde começa o texto oculto nos bytes do arquivo
    marcador = b"##START_SECRET##"
    
    # 3. Lê os bytes da imagem original (ex: Foto1.jpg)
    with open(caminho_imagem_original, 'rb') as arquivo:
        bytes_imagem = arquivo.read()
        
    # 4. Junta os bytes da imagem + marcador + a mensagem em formato binário
    dados_finais = bytes_imagem + marcador + dados_binarios.encode('utf-8')
    
    # 5. Grava a nova imagem esteganografada (ex: Foto_Secreta.jpg)
    with open(caminho_imagem_saida, 'wb') as arquivo:
        arquivo.write(dados_finais)
        
    print(f"[Sucesso] Mensagem escondida em: {caminho_imagem_saida}")


def revelar_mensagem(caminho_imagem):
    marcador = b"##START_SECRET##"
    
    # 1. Lê a imagem esteganografada
    with open(caminho_imagem, 'rb') as arquivo:
        bytes_imagem = arquivo.read()
        
    # 2. Encontra a posição do marcador nos bytes
    posicao = bytes_imagem.find(marcador)
    
    if posicao == -1:
        return "Nenhuma mensagem secreta encontrada."
        
    # 3. Pega a mensagem binária e decodifica para string
    dados_binarios = bytes_imagem[posicao + len(marcador):].decode('utf-8')
    print(f"\n[Bytes extraídos] Binário recuperado da imagem: {dados_binarios}")
    
    # 4. Converte a string de binários ("01001111...") de volta para caracteres usando ord/chr
    lista_binaria = dados_binarios.split(" ")
    caracteres = [chr(int(b, 2)) for b in lista_binaria if b]
    
    return "".join(caracteres)


# --- Menu Principal ---
if __name__ == "__main__":
    print("--- SISTEMA DE ESTEGANOGRAFIA ---")
    print("1. Esconder mensagem em Foto1.jpg")
    print("2. Revelar mensagem de Foto_Secreta.jpg")
    opcao = input("Escolha a opção (1 ou 2): ").strip()
    
    if opcao == "1":
        texto = input("Digite a mensagem secreta: ")
        ocultar_mensagem("Foto1.jpg", "Foto_Secreta.jpg", texto)
    elif opcao == "2":
        mensagem_revelada = revelar_mensagem("Foto_Secreta.jpg")
        print(f"Mensagem final traduzida: '{mensagem_revelada}'")
    else:
        print("Opção inválida.")