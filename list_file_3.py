import os


# for meta_file in os.listdir('data/meta-data'):
#     print(meta_file)

def extract_name(name):
    return name.split('.')[0]


def read_lines(filename):
    _file = open(os.path.join('data/meta-data', filename), 'rt')
    data = _file.read().split('\n')
    _file.close()
    return data


def read_meta_data(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            #values = column.split('\t')
            #nome = values[0]
            #tipo = values[1]
            #desc = values[2]
            metadata.append(tuple(column.split('\t')[:3]))
    return metadata


def main():
    # dicionário nome entidade -> atributos
    meta = {}
    
    # dicionário identificador -> nome entidade
    keys = {}
    
    for meta_data_file in os.listdir('data/meta-data'):
        table_name = extract_name(meta_data_file)
        attributes = read_meta_data(meta_data_file)
        identifier = attributes[0][0]
        
        meta[table_name] = attributes
        keys[identifier] = table_name

    for key, val in meta.items():
        print('\nEntidade {}'.format(key))
        print('Atributos: ')
        for col in val:
            print('{}: {}'.format(col[1], col[0]))

    print('')
    
    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    print('Entidade {} -> {}'.format(key, col[0]))
                        

if __name__ == '__main__':
    main()            
