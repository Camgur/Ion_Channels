#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --error=error.txt
#SBATCH --output=output.txt
#SBATCH --job-name=Li_battery_descent
#SBATCH --account=def-ravh011
#SBATCH --time=00:05:00

python "/home/cgurwell/projects/rrg-ravh011/cgurwell/Ion_Channels/opt.py" "/home/cgurwell/projects/rrg-ravh011/cgurwell/Ion_Channels\Code\cif\mp-752786.cif"