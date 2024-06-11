#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --error=error.txt
#SBATCH --output=output.txt
#SBATCH --job-name=Li_battery_descent
#SBATCH --account=def-ravh011
#SBATCH --time=00:05:00
#SBATCH --mail-user=gurwellc@mcmaster.ca
#SBATCH --mail-type=ALL

python "$HOME/projects/rrg-ravh011/cgurwell/Ion_Channels/Code/opt.py" "$HOME/projects/rrg-ravh011/cgurwell/Ion_Channels/Code/cif/mp-752786.cif"
