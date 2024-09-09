from quickchart import QuickChart
import requests

qc = QuickChart()
qc.width = 500
qc.height = 300
qc.version = '2.9.4'

# Config can be set as a string or as a nested dict
qc.config = """{
  type: 'bar',
  data: {
    labels: ['January', 'February', 'March', 'April', 'Mji'],
    datasets: [
      { label: 'Dogs', data: [50, 60, 70, 180, 190] },
      { label: 'Cats', data: [100, 200, 300, 400, 500] },
    ],
  },
}"""

# Get the chart URL
chart_url = qc.get_url()
print(chart_url)

# Fetch the image from the URL
response = requests.get(chart_url)

# Save the image to a file
if response.status_code == 200:
    with open('mychart.png', 'wb') as f:
        f.write(response.content)
else:
    print("Failed to fetch the image. Status code:", response.status_code)