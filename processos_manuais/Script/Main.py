from Billing import Billin_

class Main:

    def Run(self):

        print("Inicio processo Billing ")

        try:

            run = Billin_()
            run.Run()

            print("Processamento finalizado com sucesso.")
        
        except Exception as e:
            print('Erro no processo de automatização Billing: ---------->  ' + str(e))
            raise ValueError('Billing --->  ', e)

if __name__=='__main__':
    run = Main()
    run.Run()
    