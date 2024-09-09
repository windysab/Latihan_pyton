import pandas as pd
from quickchart import QuickChart

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded dataset.
    """
    return pd.read_csv(file_path)

def generate_colors(num_colors):
    """
    Generate a list of colors.
    
    Parameters:
    num_colors (int): The number of colors to generate.
    
    Returns:
    list: A list of color strings.
    """
    colors = [
        'red', 'blue', 'green', 'purple', 'orange', 'yellow', 'pink', 'cyan', 'magenta', 'lime'
    ]
    return colors[:num_colors]

def plot_data(table):
    """
    Plot the data using QuickChart API.
    
    Parameters:
    table (pd.DataFrame): The dataset to plot.
    
    Returns:
    str: The URL of the generated chart or the path to the saved image.
    """
    # Define the chart configuration
    colors = generate_colors(len(table['PERKARA']))
    qc = QuickChart()
    qc.width = 400  # Set the width of the chart
    qc.height = 300  # Set the height of the chart
    qc.version = '2.9.4'
    qc.config = {
        "type": "pie",
        "data": {
            "labels": table['PERKARA'].tolist(),
            "datasets": [{
                "data": table['Jumlah'].tolist(),
                "backgroundColor": colors
            }]
        },
        "options": {
            "plugins": {
                "datalabels": {
                    "display": True,
                    "color": "white"
                }
            },
            "onClick": "function(evt, item) { if (item.length) { var index = item[0].index; var chart = item[0]._chart; var data = chart.data.datasets[0].data[index]; var label = chart.data.labels[index]; chart.data.datasets[0].data = [data]; chart.data.labels = [label]; chart.update(); }}",
        }
    }

    # Get the chart URL
    chart_url = qc.get_url()
    return chart_url