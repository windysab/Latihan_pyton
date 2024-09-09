from flask import render_template
from app import app
from quickchart import QuickChart

@app.route('/line_chart')
def line_chart():
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.version = '2.9.4'

    # Config can be set as a string or as a nested dict
    qc.config = """{
      type: 'line',
      data: {
        labels: ['January', 'February', 'March', 'April', 'May'],
        datasets: [
          {
            label: 'Dogs',
            data: [50, 60, 70, 180, 190],
            fill: false,
            borderColor: 'blue',
          },
          {
            label: 'Cats',
            data: [100, 200, 300, 400, 500],
            fill: false,
            borderColor: 'green',
          },
        ],
      },
    }"""

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