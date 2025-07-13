# DA2005-Labb4-batch_means.py
# Author: Max Nerdal
# Date: 2025-07-02
# AI: Github Copilot integrated to Visual Studio Code
# Most of the code from the plot_data function is taken from github Copilot. 

import matplotlib.pyplot as plt    
import math

def read_file(file):
    """
    takes filename as input and returns a list of stripped strings on for each row
    """
    # uppgift 1 - Bröt ut denna kod från main()
    # uppgift 2 - Lagt till exception handling för att hantera fil inte hittad
    try:
        with open(file, 'r') as infile:
            row_list = [line.strip() for line in infile]
        return row_list
    except FileNotFoundError:
        print(f"File '{file}' not found.")
        return []
        
def insert_sample_to_dict(list,dict):
    """ 
    takes a list with 4 values according to sampledata input
    insert them into a dict as a touple with the batchnumber as key and returns dict
    """
    # uppgift 1 - Bröt ut denna kod från main()
    # uppgift 2 - Lagt till exception handling lagt in exception handeling för konverteringen till float
    
    batch = list[0]
    if batch not in dict:
        dict[batch] = []
    try:
        dict[batch].append((float(list[1]), float(list[2]), float(list[3]))) # Collect data from an experiment
    except ValueError as e:
        print(f"Error converting sample values to float: {list[1:]}. Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return dict

def calculate_average(batch,sample):
    """
    Takes a list of samples and calculates the average of the third value in each sample.
    Returns the average as a float.
    If there are no samples, returns None.
    """
    # uppgift 1 - uträkningen av medelvärde är flyttad till en egen funktion calculate_average
    # uppgift 2 - Lagt till exception handling för att hantera division med noll & unexpected errors
    if not sample:
        return None
    try:
        total = sum(sample[2] for sample in sample)
        average = total / len(sample)
        return average
    except ZeroDivisionError as e:
        print(f"Error: {e} - No valid samples for batch {batch} to calculate average ")
        return None
    except Exception as e:
        print(f"Unexpected error while calculating average: {e}")
        return None

def plot_data(data, f):
    """
    Takes a dictionary with batch numbers as keys and lists of samples as values.
    Plots the samples on a scatter plot, coloring them by batch number.
    Also draws a unit circle for reference
    Saves the plot to a PDF file named f.pdf.
    Returns the filename of the saved plot.
    """
    # Draw the unit circle
    angles = [n / 150 * 2 * math.pi for n in range(151)]
    x_coords = [math.cos(a) for a in angles]
    y_coords = [math.sin(a) for a in angles]
    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, label='Unit Circle', color='black')

    # Get a list of colors from matplotlib's tab10 colormap
    color_list = plt.cm.tab10.colors  # 10 distinct colors

    # uppgift 4 - plotta värden
    # id via enumerate för att hantera färger
    for idx, (batch, samples) in enumerate(sorted(data.items())):
        xs = [x for x, y, val in samples]
        ys = [y for x, y, val in samples]
        vals = [val for x, y, val in samples]
        color = color_list[idx % len(color_list)]  # Cycle through colors
        # Draw the sample points for each sample in the batch
        plt.scatter(xs, ys, label=f'Batch {batch}', color=color, s=50, alpha=0.7)
        # Label the points with their values
        for x, y, val in samples:
            plt.text(x-0.04, y-0.01, f'{val:.0f}', fontsize=6, ha='right')

    plt.axis('equal') # Set equal scaling for x and y axes
    plt.xlabel('x') # Set x-axis label
    plt.ylabel('y') # Set y-axis label
    plt.title('Samples by Batch') # Set plot title
    plt.legend() # Adds info about the batches colours
    plt.tight_layout() # Adjust layout to prevent clipping of labels
    plt.savefig(f + ".pdf") # Save the plot to a PDF file
    plt.close() # Close the plot to free up memory
    
    return f + ".pdf"

def main():
    '''This is the main body of the program.'''
    filename = input('Which csv file should be analyzed?')
    sample_dict = {}
    # uppgift 1 - koden för att läsa filen är flyttat till functionen read_file()
    sample_list = read_file(filename)

    # uppgift 1 - koden till for loopen är nu minskad pga att vi lagt viss kod i funktionen insert_sample_to_dict()
    for sample in sample_list:
        single_sample_list = sample.strip().split(',')
        sample_dict = insert_sample_to_dict(single_sample_list,sample_dict)
    
    # uppgift 1 - uträkningen av medelvärde är flyttad till en egen funktion calculate_average
    # uppgift 2 - exception handling för att hantera division med noll & unexpected errors
    print("Batch\t Average")
    # uppgift 3 - sorted batch data
    for batch, sample in sorted(sample_dict.items()): 
        average = calculate_average(batch,sample)
        print(batch, "\t", average)
 
    # uppgift 4 - plotta värden
    print(f'A plot of the data can be found in {plot_data(sample_dict,filename[0:7])}')
 
# Start the main program: this is idiomatic python
if __name__ == '__main__':
    main()
    
