class Utilitarios:

    def check_exit(self, check_x, check_y):
        self.check_x = check_x
        self.check_y = check_y
        if str(self.check_x) == "exit":
            print("Saindo...")
            sys.exit()
        elif str(self.check_x) == "-v":
            print("Voltando...")
            self.check_y = True
            return self.check_y

    def check_modulo(self, check_modulo):
        self.check_modulo = check_modulo
        try:
            self.check_modulo
        except NameError:
            print(self.check_modulo, "- Não foi encontrado")
            pass
