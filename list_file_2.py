import os


# for meta_file in os.listdir('data/meta-data'):
#     print(meta_file)

def read_meta_data(path):
    data = open(path, 'rt')
    meta_data = []
    for line in data:
        line_data = line.split('\t')
        #for i in range(len(line_data)):
            #meta_data.append(line_data[i])
            #meta_data.insert(i, line_data[i])
        meta_data.append((line_data[0], line_data[1], line_data[2]))
    data.close()
    return meta_data

print(read_meta_data('data/meta-data/Instituicao.txt'))