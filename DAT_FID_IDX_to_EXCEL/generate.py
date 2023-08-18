import random

num_records = 100
data = [(i, f'Dados Ficticios {i}', random.randint(18, 60)) for i in range(1, num_records + 1)]

with open('data.dat', 'w') as dat_file:
    for record in data:
        dat_file.write(f'{record[0]}, {record[1]}, {record[2]}\n')

with open('data.fid', 'w') as fid_file:
    for record in data:
        fid_file.write(f'{record[0]}\n')

with open('data.idx', 'w') as idx_file:
    for i, record in enumerate(data):
        idx_file.write(f'{i}, {record[0]}\n')