#!/bin/bash
#SBATCH --job-name=battery_cifs_Li        # Job name
#SBATCH --output=output.txt           # Standard output file
#SBATCH --error=error.txt             # Standard error file
#SBATCH --partition=partition_name    # Partition or queue name
#SBATCH --nodes=1                     # Number of nodes
#SBATCH --ntasks-per-node=1           # Number of tasks per node
#SBATCH --cpus-per-task=1             # Number of CPU cores per task
#SBATCH --time=1:00:00                # Maximum runtime (D-HH:MM:SS)
#SBATCH --mail-type=END               # Send email at job completion
#SBATCH --mail-user=your@email.com    # Email address for notifications

