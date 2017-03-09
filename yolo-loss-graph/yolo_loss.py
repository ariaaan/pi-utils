import os
import argparse
import matplotlib.pyplot as plt


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

with open(args.log_file, 'r') as f:
    for line in f:
        tokens = line.split(":")
        if tokens[0].isdigit():
            loss_data[0].append(int(tokens[0]))

            tokens = tokens[1].split(",")
            loss_data[1].append(float(tokens[0]))


# Graph loss
plt.plot(loss_data[0], loss_data[1])
plt.xlabel('No. Iterations')
plt.ylabel('Loss')


# Save file if output argument is present
if args.output_path:
    filename = os.path.join(args.output_path, 'output.png')
    plt.savefig(filename)


# Show graph
plt.show()
