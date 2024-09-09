from flask import render_template
from app import app
from app.utils import load_data, plot_data, generate_colors

@app.route('/')
@app.route('/index')
def index():
    table = load_data("dataset.csv")
    plot_url = plot_data(table)
    if plot_url:
        return f'''
        <html>
            <head>
                <title>Home Page - Data Plot</title>
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
                    
                </style>
                <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            </head>
            <body>
                <div class="container">
                    <h1>Jumlah Perkara per Kategori</h1>
                    <div id="chartContainer">
                        <canvas id="myChart" width="400" height="300"></canvas>
                    </div>
                </div>
                <script>
                    var ctx = document.getElementById('myChart').getContext('2d');
                    var chart = new Chart(ctx, {{
                        type: 'pie',
                        data: {{
                            labels: {table['PERKARA'].tolist()},
                            datasets: [{{
                                data: {table['Jumlah'].tolist()},
                                backgroundColor: {generate_colors(len(table['PERKARA']))}
                            }}]
                        }},
                        options: {{
                            plugins: {{
                                datalabels: {{
                                    display: true,
                                    color: 'white'
                                }}
                            }},
                            onClick: function(evt, item) {{
                                if (item.length) {{
                                    var index = item[0].index;
                                    var chart = item[0]._chart;
                                    var data = chart.data.datasets[0].data[index];
                                    var label = chart.data.labels[index];
                                    chart.data.datasets[0].data = [data];
                                    chart.data.labels = [label];
                                    chart.update();
                                }}
                            }}
                        }}
                    }});
                </script>
            </body>
        </html>
        '''
    else:
        return "Failed to generate chart."