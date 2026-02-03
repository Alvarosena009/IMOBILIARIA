from flask import Flask, render_template, request, send_file, flash
from orcamento import Orcamento
import os

app = Flask(__name__)
app.secret_key = 'chave_secreta'

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            tipo = request.form.get('tipo')
            quartos = int(request.form.get('quartos', 1))
            garagem = 'garagem' in request.form
            tem_criancas = 'tem_criancas' in request.form
            vagas_extra = int(request.form.get('vagas_extra', 0))
            parcelas_contrato = int(request.form.get('parcelas_contrato', 1))
            
            orcamento = Orcamento(tipo, quartos, garagem, tem_criancas, vagas_extra)
            aluguel = orcamento.calcular_aluguel()
            parcela_contrato, num_parcelas = orcamento.calcular_contrato(parcelas_contrato)
            
            csv_gerado = False
            if 'gerar_csv' in request.form:
                orcamento.gerar_csv(aluguel)
                csv_gerado = True
            
            return render_template('resultado.html', aluguel=aluguel, contrato=orcamento.VALOR_CONTRATO, parcela_contrato=parcela_contrato, num_parcelas=num_parcelas, csv_gerado=csv_gerado)
        
        return render_template('index.html')
    except Exception as e:
        flash(str(e))
        return render_template('index.html')

@app.route('/download_csv')
def download_csv():
    if os.path.exists('orcamento_parcelas.csv'):
        return send_file('orcamento_parcelas.csv', as_attachment=True)
    else:
        flash("CSV não encontrado.")
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)