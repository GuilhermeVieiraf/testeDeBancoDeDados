import csv
import os

input_dir = 'dados/padronizados/' 
output_dir = 'dados/limpos/'  

os.makedirs(output_dir, exist_ok=True)

csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

for file_name in csv_files:
    input_file = os.path.join(input_dir, file_name)
    output_file = os.path.join(output_dir, file_name.replace('.csv', '_limpo.csv'))

    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            reader = csv.reader(infile, delimiter=';')  
            writer = csv.writer(outfile, delimiter=';')
            for row in reader:
                writer.writerow(row)

        print(f"Arquivo CSV padronizado salvo em: {output_file}")
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_name}: {e}")