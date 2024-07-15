from bs4 import BeautifulSoup
import requests
import warnings
import csv
warnings.filterwarnings("ignore")
codigo_tce = []
n_instrumento = []
ano = []
situacao = []
objeto = []
tipo_pessoa = []
meus_links = []
cpf_cnpj = []
nome_fornecedor = []
Razão_social = []

for i in range(0, 1):
    print(f"Página: {i + 1}\n")

    url = f"https://transparencia.tcerr.tc.br/contratacoes/contratos?instrumentoContratual=&ano=&objeto=&dataAssinaturaInicial=&dataAssinaturaFinal=&valorContratadoInicial=&valorContratadoFinal=&vigenciaInicial=&vigenciaFinal=&prazoFinalDaVigenciaInicial=&prazoFinalDaVigenciaFinal=&tipoDeInstrumentoContratualId=&situacaoId=&cpfCnpj=&nomeDoFornecedor=&tipoDeOrigemDoContratoId=&page={i + 1}"

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "cookiesession1=678A8C4C233A593D5AF5ECD170F6E886; JSESSIONID=3F206B4C6E21EF17BF46B8E900544DA0",
        "Host": "transparencia.tcerr.tc.br",
        "Referer": "https://transparencia.tcerr.tc.br/contratacoes/contratos",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    response = requests.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all("a", href=True)

    for j in content:
            
        if 'informacao-contrato/' in j['href']:
            meus_links.append(j['href'])
    
    print(f"Concluído: página {i + 1}")



url_root = 'https://transparencia.tcerr.tc.br{}'
for i in meus_links:
        response = requests.get(url_root.format(i), verify = False)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find_all("p") 
        print(content)