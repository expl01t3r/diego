import os, sys


def progress():
    sys.stdout.write("\r")
    sys.stdout.write('{senha}'
                     .format(senha = str(x).rstrip()))
try:
    global dic
    dic = open(input('Caminho do dicionário (Ex.: C:\Wordist.txt): '))
except:
    print('Wordlist não encontrada')
    exit(1)

arquivo = input('Arquivo a ser quebrado (Ex.: C:\Arquivo.rar): ')
if os.path.isfile(arquivo) == False:
    print('Arquivo não encontrado')
    exit(1)
    
contador = 0

def crack(x):
    global com, extract
    com = '@"C:\Program Files\WinRAR\Rar.exe" t -y -p{senha} {arquivo} > nul 2>&1' .format(senha =  x.rstrip(), arquivo = arquivo)
    extract = os.system(com)
try:
    for x in dic:
        progress()
        crack(x)
        if extract == 0:
            os.system('cls')
            print('\n\n[+]Senha encontrada: {text}\nNumero de tentativas executadas: {cnt}'
                  .format( text = x, cnt = contador))
            opcode = 1
            break
        contador += 1
        
except KeyboardInterrupt:
    os.system('cls')
    print('\n\n[-]Procedimento cancelado pelo usuário\nNumero de tentativas executadas: {cnt}' .format(cnt = contador))
    dic.close()
    exit(1)
    
dic.close()
if opcode == 0:
    os.system('cls')
    print('\n\n[-]Valor não encontrado, tente com uma wordlist mais completa ;)\nNumero de tentativas executadas: {cnt}' .format(cnt = contador))
