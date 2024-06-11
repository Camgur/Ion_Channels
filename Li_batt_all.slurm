#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --gres=gpu:v100:4
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --mem=32G
#SBATCH --error=error.txt
#SBATCH --output=output.txt
#SBATCH --job-name=Li_batt_all
#SBATCH --account=def-ravh011
#SBATCH --time=14:00:00
#SBATCH --mail-user=gurwellc@mcmaster.ca
#SBATCH --mail-type=ALL

python "$HOME/projects/rrg-ravh011/cgurwell/Ion_Channels/Code/opt_all.py" "$HOME/projects/rrg-ravh011/cgurwell/Ion_Channels/Code/cif/"
