# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import json
from datetime import datetime, date, time
from typing import Dict, List
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def import_json() -> Dict:
    with open('resultados_promax_dia_29-09-2020_as_JSON_array.json') as f:
        data = json.load(f)
    return data



class Pedido:
    chave_unica: str
    timestamp: datetime
    codigo: int
    data: datetime
    cliente: int
    saldoCredito: float
    numero_dias_atraso: int
    valor_titulo_atraso: int
    numero_titulos_atraso: int
    total_pedido: float
    setor: int
    status: int
    critica_principal: int
    critica_cdp: int
    alcada1: int
    alcada2: int
    alcada3: int
    codigo_critica: int
    status_critica: int
    alcada_critica: int
    produto_critica: int
    combo_critica: int
    quantidade_critica: int
    valor_critica: float

    def __repr__(self):
      return str(self.__dict__)



dict_header = ["chave_unica", "timestamp", "codigo", "data", "cliente", "saldo_credito", "numero_dias_atraso", "valor_titulo_atraso", "numero_titulos_atraso", "total_pedido", "setor", "status", "critica_principal", "critica_cdp", "alcada1", "alcada2", "alcada3", "codigo_critica", "status_critica", "alcada_critica", "produto_critica", "combo_critica", "quantidade_critica", "valor_critica"]

def save_to_csv(lista_de_pedidos_para_csv: List[Pedido]) -> None:
     with open('transformado.csv', 'w') as myfile:
         wr = csv.DictWriter(myfile, fieldnames=dict_header)
         wr.writeheader()
         for item in lista_de_pedidos_para_csv:
             wr.writerow(item.__dict__)


# Function to convert string to datetime
def convert_datetime(date_pedido: str, hora_pedido: str)-> None:
    format_date = "%Y%m%d"  # The format
    format_time = "%H%M%S"
    date_ped = datetime.strptime(date_pedido, format_date)
    hora_ped = datetime.strptime(hora_pedido, format_time)
    date_time = datetime.combine(date_ped.date(), hora_ped.time())
    return date_time


def transform_data(json: Dict) -> None:
    lista_de_pedidos_para_csv: List[Pedido] = []
    for lista in json:
        p = Pedido()
        p.chave_unica = lista['chave_unica']
        p.timestamp = lista['chave_unica']
        lista_pedidos = lista['envio_promax']['resultadoHercules']['listaPedidos']
        for ped in lista_pedidos:
            p.codigo = ped['codigo']
            p.data = convert_datetime(ped['data'], ped['hora'])
            p.cliente = ped['cliente']
            p.saldo_credito = ped['saldoCredito']
            p.numero_dias_atraso = ped['numeroDiasAtraso']
            p.valor_titulo_atraso = ped['valorTitulosAtraso']
            p.numero_titulos_atraso = ped['numeroTitulosAtraso']
            p.total_pedido = ped['totalPedido']
            p.setor = ped['setor']
            p.status = ped['status']
            p.critica_principal = ped['criticaPrincipal']
            p.critica_cdp = ped['criticaCDP']
            p.alcada1 = ped['alcada1']
            p.alcada2 = ped['alcada2']
            p.alcada3 = ped['alcada3']
            lista_de_pedidos_para_csv.append(p)

            #for pelas criticas
            # codigo_critica: int
            # status_critica: int
            # alcada_critica: int
            # produto_critica: int
            # combo_critica: int
            # quantidade_critica: int
            # valor_critica: float
    save_to_csv(lista_de_pedidos_para_csv)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = import_json()
    transform_data(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
