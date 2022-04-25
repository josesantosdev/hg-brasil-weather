class Precisao:

    def __init__(self, id: int = -1, temp_celsius: float = 0.0, data: str = '', hora: str = '', descricao: str = '',
                 dia_noite: str = '', umidade: int = 0, velocidade_vento: str = '', sunrise: str = '', sunset: str = '',
                 condicao: str = '', forecast: [] = 0) -> None:
        super().__init__()
        self.__id = id
        self.__temp_celsius = temp_celsius
        self.__data = data
        self.__hora = hora
        self.__descricao = descricao
        self.__dia_noite = dia_noite
        self.__umidade = umidade
        self.__velocidade_vento = velocidade_vento
        self.__sunrise = sunrise
        self.__sunset = sunset
        self.__condicao = condicao
        self.__forecast = forecast

        @property
        def id(self):
            return self.__id

        @property
        def temp_celsius(self):
            return self.__temp_celsius
        @temp_celsius.setter
        def temp_celsius(self, value):
            self.__temp_celsius = value

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            self.__data = value

        @property
        def hora(self):
            return self.__hora

        @hora.setter
        def hora(self, value):
            self.__hora = value

        @property
        def descricao(self):
            return self.__descricao

        @descricao.setter
        def descricao(self, value):
            self.__descricao = value

        @property
        def dia_noite(self):
            return self.__dia_noite

        @dia_noite.setter
        def dia_noite(self, value):
            self.__dia_noite = value

        @property
        def umidade(self):
            return self.__umidade

        @umidade.setter
        def umidade(self, value):
            self.__umidade = value

        @property
        def velocidade_vento(self):
            return self.__velocidade_vento

        @velocidade_vento.setter
        def velocidade_vento(self, value):
            self.__velocidade_vento = value

        de(self):
        return
            @property





