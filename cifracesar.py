#coding: utf-8
def crypt(msg):
    print('César CRIPT\nCRYPT\n---------------')
    temp = (input('Digite a chave para criptografar a mensagem: '))
    chave = sum(ord(x) for x in temp)    
    msgcrpt = [ord(x)+chave for x in msg]
    msg = ''.join(chr(x) for x in msgcrpt)
    print(msg)
    
def decrypt(msg):
    print('César CRIPT\nDECRYPT\n---------------')
    temp=(input('Digite a chave para descriptografar a mensagem: '))
    chave=sum(ord(x) for x in temp)
    msgcrpt=[ord(x)-chave for x in msg]
    msg=''.join(chr(x) for x in msgcrpt)

# teste
'''arquivo = open(input('Digite o caminho do arquivo: '))
crypt(arquivo.read())
'''
while True:
    print("""
    1.Criptografar Mensagem a partir do prompt
    2.Criptografar Mensagem a partir de um arquivo de texto
    3.Desriptografar Mensagem a partir do prompt
    4.Desriptografar Mensagem a partir de um arquivo de texto
    5. Sair
    """)
    op=input("Selecione uma opção ")
    if op=="1":
        mensagem =  input('Digite a Mensagem a ser critpgrafada: ')
        crypt(mensagem)
        while True:
            print('''
    1. Salvar Mensagem Criptografada para um arquivo
    2. Exibir mensagem na tela
    ''')
            op=(input('Escolha uma opção'))
            if op=='1':
                local=input('Digite o nome do arquivo que sera salvo: ')
                arquivo = open(local, 'w', encoding = 'utf-8')
                arquivo.write(msg)
                arquivo.close()
    elif op=="2":
      print("\n Student Deleted")
    elif op=="3":
      print("\n Student Record Found")
    elif op=="5":
        break
    else:
       print("\n Oção inválida, tente novamente")

