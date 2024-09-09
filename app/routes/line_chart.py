from flask import render_template
from app import app
from app.utils import load_data, generate_colors
from quickchart import QuickChart

@app.route('/line_chart')
def line_chart():
    table = load_data("dataset2.csv")
    labels = ['sisa lama', 'masuk', 'putus', 'sisa baru']
    
    datasets = []
    for perkara in table['PERKARA']:
        data = table[table['PERKARA'] == perkara][labels].values.flatten().tolist()
        datasets.append({
            "label": perkara,
            "data": data,
            "fill": False,
            "borderColor": generate_colors(1)[0]
        })

    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.version = '2.9.4'
    qc.config = {
        "type": "line",
        "data": {
            "labels": labels,
            "datasets": datasets
        }
    }

    chart_url = qc.get_url()
    return f'''
    <html>
        <head>
            <title>Line Chart</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .container {{
                    text-align: center;
                    background: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    color: #444;
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                    border-radius: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Line Chart Example</h1>
                <img src="{chart_url}" alt="Line Chart" />
            </div>
        </body>
    </html>
    '''