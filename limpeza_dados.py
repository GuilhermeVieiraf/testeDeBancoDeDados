import csv

def limpar_dados(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r', encoding='utf-8') as infile, open(arquivo_saida, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        for row in reader:
            if len(row) != 6:
                continue

            try:
                row[1] = int(row[1]) 
            except ValueError:
                row[1] = 0 
            
            row[2] = row[2][:255] 

            writer.writerow(row)

limpar_dados('dados/padronizados/1T2023.csv', 'dados/limpos/1T2023_limpo.csv')
limpar_dados('dados/padronizados/2T2023.csv', 'dados/limpos/2T2023_limpo.csv')
limpar_dados('dados/padronizados/3T2023.csv', 'dados/limpos/3T2023_limpo.csv')
limpar_dados('dados/padronizados/4T2023.csv', 'dados/limpos/4T2023_limpo.csv')
limpar_dados('dados/padronizados/1T2024.csv', 'dados/limpos/1T2024_limpo.csv')
limpar_dados('dados/padronizados/3T2024.csv', 'dados/limpos/3T2024_limpo.csv')
limpar_dados('dados/padronizados/4T2024.csv', 'dados/limpos/4T2024_limpo.csv')
limpar_dados('dados/padronizados/Relatorio_cadop.csv', 'dados/limpos/Relatorio_cadop_limpo.csv')

print("Dados limpos com sucesso!")