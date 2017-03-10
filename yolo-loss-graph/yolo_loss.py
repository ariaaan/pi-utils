import os
import sys
import argparse
from matplotlib import style
from matplotlib import pyplot as plt


# Parse arguments
parser = argparse.ArgumentParser(description='yolo-loss-graph')
parser.add_argument('log_file', help='path for the yolo training log file')

parser.add_argument('-o', '--output', dest='output_path', help='folder path for generated plot')

args = parser.parse_args()


# Check if log file exists
if not os.path.isfile(args.log_file):
    parser.print_help()
    sys.exit()


# Read log file and extract loss data
loss_data = []
loss_data.append([])
loss_data.append([])
loss_data.append([])

last_iteration = 0

with open(args.log_file, 'r') as f:
    for line in f:
        tokens = line.split(":")
        if tokens[0].isdigit():
            # Iteration number
            iteration = int(tokens[0])

            if iteration > last_iteration:
                last_iteration = iteration
                
                # Iteration
                loss_data[0].append(iteration)

                # Split with commas
                tokens = tokens[1].split(",")

                # Loss
                loss_data[1].append(float(tokens[0]))

                # Average loss
                loss_data[2].append(float(tokens[1].split()[0]))


# Graph loss
style.use('ggplot')
plt.plot(loss_data[0], loss_data[1], color='#e74c3c', label='Loss')
plt.plot(loss_data[0], loss_data[2], color='#f1c40f', label='Average loss')
plt.xlabel('No. Iterations')
plt.ylabel('Loss')
plt.legend()


# Save file if output argument is present
if args.output_path:
    filename = os.path.join(args.output_path, 'output.png')
    plt.savefig(filename)


# Show graph
plt.show()
