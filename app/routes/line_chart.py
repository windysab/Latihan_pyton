from flask import render_template
from app import app
from app.utils import load_data, generate_colors
import calendar
from datetime import datetime
from quickchart import QuickChart

@app.route('/line_chart')
def line_chart():
    table = load_data("dataset2.csv")
    labels = ['SISA LAMA', 'MASUK', 'PUTUS', 'SISA BARU']
    
    datasets = []
    for index, perkara in enumerate(table['PERKARA']):
        data = table[table['PERKARA'] == perkara][labels].values.flatten().tolist()
        border_color = 'red' if perkara == 'Gugatan' else 'green' if perkara == 'Permohonan' else generate_colors(1)[0]
        datasets.append({
            "label": perkara,
            "data": data,
            "fill": False,
            "borderColor": border_color
        })

    chart_config = {
        "type": "line",
        "data": {
            "labels": labels,
            "datasets": datasets
        },
        "options": {
            "onClick": "function(event, array) { if(array.length > 0) { alert(array[0].element.$context.raw); } }"
        }
    }

    # Extract E-Court data from the CSV
    e_court_gugatan = float(table[table['PERKARA'] == 'Gugatan']['E-COURT'].str.rstrip('%').values[0])
    e_court_permohonan = float(table[table['PERKARA'] == 'Permohonan']['E-COURT'].str.rstrip('%').values[0])
    
    # Menghitung rasio penyelesaian perkara
    # jumlah_gugatan = float(table[table['PERKARA'] == 'Gugatan']['MASUK'].values[0]) 
    # jumlah_gugatan_putus = float(table[table['PERKARA'] == 'Gugatan']['PUTUS'].values[0])
    # rasio_gugatan = jumlah_gugatan_putus / jumlah_gugatan * 100
    

    # jumlah_permohonan = float(table[table['PERKARA'] == 'Permohonan']['MASUK'].values[0])
    # jumlah_permohonan_putus = float(table[table['PERKARA'] == 'Permohonan']['PUTUS'].values[0])
    # rasio_permohonan = jumlah_permohonan_putus / jumlah_permohonan * 100

    # Create QuickChart progress bar for Gugatan
    qc_gugatan = QuickChart()
    qc_gugatan.width = 300
    qc_gugatan.height = 50
    qc_gugatan.version = '2.9.4'
    qc_gugatan.config = {
        "type": "progressBar",
        "data": {
            "datasets": [
                {
                    "data": [e_court_gugatan],
                    "backgroundColor": "rgba(204, 33, 33, 0.8)"  # Light red
                },
            ],
        },
    }
    progress_bar_url_gugatan = qc_gugatan.get_url()

    # Create QuickChart progress bar for Permohonan
    qc_permohonan = QuickChart()
    qc_permohonan.width = 300
    qc_permohonan.height = 50
    qc_permohonan.version = '2.9.4'
    qc_permohonan.config = {
        "type": "progressBar",
        "data": {
            "datasets": [
                {
                    "data": [e_court_permohonan],
                    "backgroundColor": "rgba(45, 160, 45, 0.8)"  # Light green
                },
            ],
        },
    }
    progress_bar_url_permohonan = qc_permohonan.get_url()

    # Generate a radial gauge chart for Gugatan using QuickChart
    rasio_gugatan = float(table[table['PERKARA'] == 'Gugatan']['PUTUS'].values[0]) / float(table[table['PERKARA'] == 'Gugatan']['MASUK'].values[0]) * 100
    
    qc_radial_gugatan = QuickChart()
    qc_radial_gugatan.width = 300
    qc_radial_gugatan.height = 100
    qc_radial_gugatan.version = '2.9.4'
    qc_radial_gugatan.config = {
        "type": "radialGauge",
        "data": {
            "datasets": [
                {
                    "data": [rasio_gugatan],  # Use actual data for Gugatan
                    "backgroundColor": "red"
                }
            ]
        }
    }
    radial_chart_url_gugatan = qc_radial_gugatan.get_url()
    qc_radial_gugatan.to_file('mychart_gugatan.png')

    # Generate a radial gauge chart for Permohonan using QuickChart
    rasio_permohonan = float(table[table['PERKARA'] == 'Permohonan']['PUTUS'].values[0]) / float(table[table['PERKARA'] == 'Permohonan']['MASUK'].values[0]) * 100
    qc_radial_permohonan = QuickChart()
    qc_radial_permohonan.width = 300
    qc_radial_permohonan.height = 100
    qc_radial_permohonan.version = '2.9.4'
    qc_radial_permohonan.config = {
        "type": "radialGauge",
        "data": {
            "datasets": [
                {
                    "data": [rasio_permohonan] ,  # Use actual data for Permohonan
                    "backgroundColor": "green"
                }
            ]
        }
    }
    radial_chart_url_permohonan = qc_radial_permohonan.get_url()
    qc_radial_permohonan.to_file('mychart_permohonan.png')

    # Get current month name
    current_month = calendar.month_name[datetime.now().month]

    return render_template(
        'line_chart.html', 
        chart_config=chart_config, 
        current_month=current_month, 
        progress_bar_url_gugatan=progress_bar_url_gugatan, 
        progress_bar_url_permohonan=progress_bar_url_permohonan,
        radial_chart_url_gugatan=radial_chart_url_gugatan,
        radial_chart_url_permohonan=radial_chart_url_permohonan
    )