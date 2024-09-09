from flask import render_template
from app import app
from app.utils import load_data
from quickchart import QuickChart

@app.route('/doughnut')
def doughnut_chart():
    table = load_data("dataset.csv")
    labels = table['PERKARA'].tolist()
    data = table['Jumlah'].tolist()
    total = sum(data)

    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.version = '2.9.4'
    qc.config = {
        "type": "doughnut",
        "data": {
            "labels": labels,
            "datasets": [{
                "data": data
            }]
        },
        "options": {
            "plugins": {
                "doughnutlabel": {
                    "labels": [
                        {"text": str(total), "font": {"size": 20}},
                        {"text": 'total'}
                    ]
                }
            }
        }
    }

    chart_url = qc.get_url()
    return f'''
    <html>
        <head>
            <title>Doughnut Chart</title>
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
                <h1>Doughnut Chart Example</h1>
                <img src="{chart_url}" alt="Doughnut Chart" />
            </div>
        </body>
    </html>
    '''