from decimal import Decimal


class Relationship:
    '''Classe que representa um relacionamento entre DataTables.
    Essa classe tem todas as informações que identificam um
    relacionamento entre tabelas.
    '''

    def __init__(self, name, _from, to, on):
        '''Construtor
        args:
            name: Nome
            _from: Tabela de onde sai
            to: Tabela pra onde vai
            on: Instância de coluna onde existe
        '''
        self._name = name
        self._from = _from
        self._to = to
        self._on = on


class Column:
    """Representa uma coluna em um DataTable.
    Essa classe contém as informações de uma coluna
    e deve validar um dado de acordo com o tipo de
    dado configurado no construtor.
    Attributes:
        name: Nome da Coluna
        king: Tipo do Dado (varchar, bigint, numeric)
        description: Descrição da coluna
    """

    def __init__(self, name, kind, description=''):
        """Construtor
        Args:
        name: Nome da Coluna
        kind: Tipo do dado (varchar, bigint, numeric)
        description: Descrição da coluna
        """
        self._name = name
        self._kind = kind
        self._description = description
        self._is_pk = False

    def __str__(self):
        _str = 'Col: {} : {} {}'.format(self._name,
                                        self._kind,
                                        self._description)
        return _str

    def validate(self, data):
        if self._kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif self._kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif self._kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True


class PrimaryKey(Column):

    def __init__(self, table, name, kind, description=''):
        super().__init__(name, kind, description=description)
        self._is_pk = True

    def __str__(self):
        _str = 'Col: {} : {} {}'.format(self._name,
                                        self._kind,
                                        self._description)
        return '{} - {}'.format('PK', _str)


class DataTable:
    """Representa uma tabela de dados.
    Essa classe representa uma tabela de dados do portal
    da transparência.
    Attributes:
        name: Nome da tabela.
        columns: [Lista de colunas]
        data: [Lista de dados]
    """

    def __init__(self, name):
        '''Construtor
        args:
            name: Nome da tabela
        '''
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []

    def _get_name(self):
        print('Getter Executado!')
        return self._name

    def _set_name(self, _name):
        print('Setter Executado!')
        self._name = _name

    def _del_name(self):
        print('Deletter Executado!')
        raise AttributeError('Esse atributo não pode ser deletado.')

    name = property(_get_name, _set_name, _del_name)

    def add_column(self, name, kind, description=''):
        '''Adiciona uma coluna na tabela
        '''
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        '''Cria uma referência dessa tabela para uma outra tabela.
        Args:
            name: Nome da relação
            to: Instância da tabela apontada
            on: Instância da coluna onde existe a relação
        '''
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        '''Cria uma referência para outra tabela que aponta para essa.
        Args:
            name: Nome da relação
            by: Instância da tabela que aponta para essa
            on: Instância da coluna que existe a relação
        '''
        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)
