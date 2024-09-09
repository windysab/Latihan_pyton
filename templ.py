import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded dataset.
    """
    return pd.read_csv(file_path)

def plot_data(table):
    """
    Plot the data from the dataset.
    
    Parameters:
    table (pd.DataFrame): The dataset to plot.
    """
    # Define the labels and colors
    x_label = table['NAMA KELURAHAN']
    colors = ['red', 'blue', 'green', 'purple', 'orange']
    
    # Create the bar plot with different colors
    plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'], color=colors, tick_label=x_label)
    plt.xlabel('NAMA KELURAHAN')
    plt.ylabel('LAKI-LAKI WNI')
    plt.title('Jumlah Laki-Laki WNI per Kelurahan')
    plt.show()

def main():
    """
    Main function to load data and plot it.
    """
    # Read the dataset
    table = load_data("dataset.csv")
    print(table.head())
    
    # Plot the data
    plot_data(table)

if __name__ == "__main__":
    main()