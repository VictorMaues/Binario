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

