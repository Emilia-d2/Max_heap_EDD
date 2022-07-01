import os
from Paciente import Paciente

class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def put(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def get(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    #Topo
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    #troca de lugar
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1: # nao faz nada se for raiz
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.heap) > left and self.heap[maior] < self.heap[left]:
            maior = left
        if len(self.heap) > right and self.heap[maior] < self.heap[right]:
            maior = right

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)
    
    def inicio(self):
        indice = 999
        listaChamados = []
        while True:    
            print("""
            ---------------------------------------------------
            | BEM-VINDO AO SISTEMA!                            |
            | Digite 0 para sair do sistema:                   |
            | Digite 1 cadastrar/adicionar paciente:           |
            | Digite 2 para chamar o próximo paciente:         |
            | Digite 3 para mostrar o próximo paciente:        |
            | Digite 4 para listar os últimos 5 chamados:      |
            ---------------------------------------------------
            """)
            
            op = input("Digite uma opção: ")

            if op == "1":
               
                print("Cadastre seu usuário!")

                p = Paciente()
                p.setNome(input('Digite seu nome: '))
                p.setDataNascimento(input('Digite sua data de nascimento: '))
                p.setTipoSanguineo(input('Digite seu tipo sanguineo: '))

                prioridade = int(input("Prioridade 10 ou 1: "))

                gravarDados = (prioridade, indice, p)
                self.put(gravarDados)
                indice -= 1

               
            if op == "2": 
                #chamar o primeiro que chegou, elemnto 0 da tupla
                dados = self.get()
                print(dados[0], dados[1], dados[2].getNome())
                listaChamados.append(dados)

            if op == "3":
                #Mostrar o próximo a ser chamado, mas sem chamar 
                dados = self.peek()
                print(dados[0], dados[1], dados[2].getNome())

            if op == "4":
                #listar os 5 últimos a serem chamados 
                for paciente in listaChamados[-5:]:
                    print(paciente[0], paciente[1], paciente[2].getNome())


            if op == "0":
                break

he = MaxHeap()
he.inicio()


