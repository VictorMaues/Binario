def para_binario(simbolo):
    numero_tabela = ord(simbolo)
    codigo_binário = format(numero_tabela, '08b')
    return codigo_binário

def texto_para_binario(texto):
    resultado_final = []
    
    
    for letra in texto:
        binario = para_binario(letra)
        resultado_final.append(binario)
        
   
    return " ".join(resultado_final)

mensagem = input("Informe a frase: ")
print(f"'{mensagem}' em binário fica:")
print(texto_para_binario(mensagem))

#Função trasnformar uma imagem para binário

def imagem_binario(nome_do_arquivo):
    with open(nome_do_arquivo, 'rb') as arquivo:
        dados_da_imagem = arquivo.read()

        resultado = []

        for byte in dados_da_imagem[:20]:
            binario = format(byte, '08b')
            resultado.append(binario)

        return " ".join(resultado)

caminho = "Foto1.jpg"

try:
    resultado = imagem_binario(caminho)
    print(f"'Os primeito 20 bytes da imagem em binário são: \n{resultado}")
except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho}' não foi encontrado. Coloque uma imagem na mesma pasta!")
    