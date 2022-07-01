class Paciente:
    def __init__(self):
        self.nome = ''
        self.sangue = ''
        self.dt_nascimento = ''

    def setNome(self, nome):
        self.nome = nome

    def setTipoSanguineo(self, sangue):
        self.sangue = sangue

    def setDataNascimento(self, dtNascimento):
        self.dt_nascimento  = dtNascimento

    def getNome(self):
        return self.nome

    def getTipoSanguineo(self):
        return self.sangue

    def getDataNascimento(self):
        return self.dt_nascimento