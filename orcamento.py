class Orcamento:
    def __init__(self, tipo_imovel, quartos=1, garagem=False, tem_criancas=True, vagas_extra=0):
        self.tipo_imovel = tipo_imovel.lower()  # 'apartamento', 'casa' ou 'estudio'
        self.quartos = quartos  # 1 ou 2
        self.garagem = garagem  # True/False
        self.tem_criancas = tem_criancas  # True/False (afeta desconto para apartamentos)
        self.vagas_extra = vagas_extra  # Apenas para estudio (vagas além das 2 iniciais)
        self.VALOR_CONTRATO = 2000.00
        self.MAX_PARCELAS_CONTRATO = 5

    def calcular_aluguel(self):
        # Valores base conforme regras da R.M
        if self.tipo_imovel == 'apartamento':
            valor = 700.00
            if self.quartos == 2:
                valor += 200.00
            if self.garagem:
                valor += 300.00
            if not self.tem_criancas:
                valor *= 0.95  # Desconto de 5%
        elif self.tipo_imovel == 'casa':
            valor = 900.00
            if self.quartos == 2:
                valor += 250.00
            if self.garagem:
                valor += 300.00
        elif self.tipo_imovel == 'estudio':
            valor = 1200.00
            # Estudio tem 2 vagas por R$ 250, extras por R$ 60
            valor += 250.00  # 2 vagas incluídas
            valor += self.vagas_extra * 60.00
        else:
            raise ValueError("Tipo de imóvel inválido.")
        return round(valor, 2)

    def calcular_contrato(self, parcelas=1):
        if parcelas < 1 or parcelas > self.MAX_PARCELAS_CONTRATO:
            raise ValueError("Parcelas do contrato devem ser entre 1 e 5.")
        valor_parcela = self.VALOR_CONTRATO / parcelas
        return round(valor_parcela, 2), parcelas

    def gerar_csv(self, aluguel_mensal, filename='orcamento_parcelas.csv'):
        # Gera CSV com 12 parcelas mensais do aluguel (interpretação: 12 meses de orçamento)
        import csv
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Parcela', 'Valor (R$)'])
            for i in range(1, 13):
                writer.writerow([f'Mês {i}', f'{aluguel_mensal:.2f}'])
        print(f"Arquivo '{filename}' gerado com sucesso!")