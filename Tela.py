import customtkinter
from ConversorRomano import ConversorRomano


class Tela:
    def __init__(self):
        self.janela = customtkinter.CTk()
        self.janela.geometry("260x237")
        self.janela.title("Conversor de Algarismos Romanos")
        self.conversor = ConversorRomano()

        self.criar_componentes()

    def criar_componentes(self):
        self.titulo = customtkinter.CTkLabel(
            self.janela, text="CONVERSOR DE ALGARISMOS ROMANOS")
        self.titulo.pack(padx=10, pady=10)

        self.opcoes = ["Inteiros para romanos", "Romanos para inteiros"]
        self.btn_selecionar = customtkinter.CTkComboBox(
            self.janela, values=self.opcoes, width=175)
        self.btn_selecionar.pack(padx=10, pady=10)

        self.txt_numero = customtkinter.CTkEntry(
            self.janela, placeholder_text="Digite algum número inteiro", width=175)
        self.txt_numero.pack(padx=10, pady=10)

        botao = customtkinter.CTkButton(
            self.janela, text="Converter", command=self.realizar_conversao)
        botao.pack(padx=5, pady=5)

    def validar_entrada(self):
        numero_texto = self.txt_numero.get()
        try:
            numero_inteiro = int(numero_texto)
            return True
        except ValueError:
            return False

    def converter_para_romano(self):
        if self.validar_entrada():
            try:
                numero_inteiro = int(self.txt_numero.get())
                result = self.conversor.para_romano(numero_inteiro)
                self.titulo.configure(text=result)
            except ValueError as e:
                self.titulo.configure(text=e)
        else:
            self.titulo.configure(text="Não é um número inteiro!")

    def converter_para_inteiro(self):
        try:
            valor_digitado = self.txt_numero.get().upper()
            result = self.conversor.para_arabico(valor_digitado)
            if result > 0:
                self.titulo.configure(text=result)
            else:
                self.titulo.configure(text="Digite um simbolo válido!")
        except ValueError as e:
            self.titulo.configure(text=e)

    def realizar_conversao(self):
        if self.btn_selecionar.get() == self.opcoes[0]:
            self.converter_para_romano()
        else:
            self.converter_para_inteiro()


if __name__ == "__main__":
    tela = Tela()
    tela.janela.mainloop()
