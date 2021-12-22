import os,sys,wget,time,requests,re,urllib.request
from bs4 import BeautifulSoup
from googlesearch import search
print ("instalando recursos aguarde...")
os.system ("apt install poppler -y")
print ("instalando modulos...")
os.system ("pip install bs4 && pip install wget && pip install google && pip install requests")
os.system ("clear")
print ('''\033[91m
 :::=======  ::: :::= === :::===== :::==== 
 ::: === === ::: :::===== :::      :::  ===
 === === === === ======== ======   ======= 
 ===     === === === ==== ===      === === 
 ===     === === ===  === ======== ===  ===

\033[0;0m''')
time.sleep (1)
dhc = "BEM VINDO (A)!"
for i in list(dhc):
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.1)
print ('')
print ('')
print ('''
        |````````````````````````````````````|
        |    desenvolvido por D.H.C team     |
        |            beta: 0.0.1             |
        |  contato: dhcteamhacking@gmail.com |
        |____________________________________|
''')
while True:
    ir = input("quer ir para o menu da ferramenta?  sim/nao: ")
    if ir == "sim":
        time.sleep (1)
        break
    elif ir == "nao":
        exit ()
    else:
        print ('\033[93m'+'digite apenas sim ou nao!'+'\033[0;0m')
print ('''\033[32m
    |°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    |                 dhc miner                 |
    |                                           |
    |         [1]minerar dados                  |
    |         [2]converter .pdf para .txt       |
    |         [i]mais informações               |
    |         [x]sair                           |
    |___________________________________________|\033[0;0m''')
while True:
    opcao = input("digite a opção desejada: ")
    if opcao == "1":
        print('''recomendo pesquisar com dork's!
        
        exemplo: intext: cpf filetype: .pdf
        
        atenção este script suporta apenas download de arquivos com .pdf ou .txt no final! caso não coloque o (filetype: .pdf ou .txt) ele irá baixar o site completo. como arquivos java,css,html,xml,php entre outros.
        
        obs1: o script pode ser bloqueado por sites com sistema de agentes de navegador portanto pode não funcionar as vezes e retornar o codigo de erro 403 que e o codigo de permissão negada/recusada.
        
        obs2: eu tentei colocar a identidade de um agente de browser falso, porem sem sucesso. continuou retornando o codigo de erro 403.
      
    
        ''')
        query = input("pesquisar por dados: ")
        if query == query:
            while True:
                for j in search(query, tld="co.in", num=1,stop=1, pause=2):
                    print('\033[32m'+'|1|resultado encontrado!'+'\033[0;0m')
                    time.sleep (0.1)
                    print(j)
                    time.sleep (0.1)
                    #download
                    url = (j)
                    r = requests.get(url)
                    time.sleep (0.1)
                    filename = wget.download(j)
    elif opcao == "2":
        print ("aguarde...")
        pdf = input ("digite o nome do arquivo em .pdf: ")
        arq = input ("agora digite o nome para o arquivo em .txt: ")
        os.system ("pdftotext "+pdf)
        
    elif opcao == "i":
        print ('''
                |°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
                |        dhc team domina        |
                |_______________________________|
                |       para mais scripts:      |
                |  dhcteam.000webhostapp.com    |
                |_______________________________|
                |      ou entre em contato:     |
                |   dhcteamhacking@gmail.com    |
                |_______________________________|
                |     fazemos preços justos!    |
                |_______________________________|
                |    também vendemos exploits   |
                | malwares virus trojans etc    |
                |_______________________________|
                ''')
    elif opcao == "x":
        print ("saindo...")
        time.sleep (1)
        os.system ("clear")
        exit()
    break
else:
    print ('')
    print ('')
    print ('\033[31m'+'opção invalida'+'\033[0;0m')