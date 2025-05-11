# ✨ 100 Days of Code Challenge - Day 10/100 💻

from flask import Flask
from flask import jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "API está funcionando!"

@app.route('/total_vendas', methods=['GET'])

def get_total_vendas():
    tabela = pd.read_csv('advertising.csv')
    total_vendas = tabela['Vendas'].sum()
    return jsonify({'Total Vendas': total_vendas}) 

app.run()