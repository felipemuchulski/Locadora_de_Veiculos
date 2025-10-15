from datetime import datetime
class EntradaDados:
    def le_inteiro(self, msg, minimo=None, maximo=None):
        while True:
            try:
                valor = int(input(msg))
                if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                    print(f"Valor fora do intervalo permitido ({minimo}) a ({maximo}). Tente novamente")
                else:
                    return valor
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
    
    def le_float(self, msg, minimo=None, maximo=None):
        while True:
            try:
                valor = float(input(msg))
                if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                   print(f"Valor fora do intervalo permitido ({minimo}) a ({maximo}). Tente novamente") 
                else:
                    return valor
            except ValueError:
                print("Entrada inválida. Digite um número decimal.")
    
    def le_strin(self, msg, obrigatorio=True):
        while True:
            valor = input(msg)
            if obrigatorio and not valor.strip():
                print("Entrada obrigatória. Digite algum valor")
            else:
                return valor.strip()
            
    def le_data(self, msg):
        formato = "%d/%m/%Y"
        hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        while True:
            data_max_str = input("Digite a data máxima permitda (dd/mm/yyyy): ")
            try:
                data_max = datetime.strptime(data_max, formato)
                if data_max < hoje:
                    print("A data máxima não pode ser anterior ao dia atual.")
                else:
                    break
            except ValueError:
                print("Data máxima inválida. Use o formato dd/mm/yyyy.")
        
        while True:
            entrada = input(msg)
            try:
                data = datetime.strptime(entrada, formato)
                if data < hoje or data > data_max:
                    print(f"A data deve estar entre {hoje.strftime(formato)} e {data_max.strftime(formato)}.")
                else:
                    return data
            except ValueError:
                print("Formato inválido. Use o formato dd/mm/yyyy.")