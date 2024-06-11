import sys
import os

import torch
import numpy as np
import mace

import matplotlib as mpl
import matplotlib.pyplot as plt

from mace.calculators import mace_mp, MACECalculator
from ase.calculators.loggingcalc import LoggingCalculator
from ase.optimize import BFGS

from ase.visualize import view
from ase.visualize.plot import plot_atoms
from ase import build, units, atoms
from ase.io import read, write, Trajectory
from ase.io.animation import write_gif

from ase.constraints import ExpCellFilter, StrainFilter, UnitCellFilter
from ase.spacegroup.symmetrize import FixSymmetry, check_symmetry

# Set Folder
folder = sys.argv[1]

# Iterate in Folder
for filename in os.listdir(folder):

    # Set File
    file = os.path.join(folder, filename)
    base = '/home/cgurwell/scratch/optimise/'

    # Filter CIFs
    if file.endswith('.cif'):

        # Importing CIF
        atoms = read(file)

        # Setting the MACE-MP-0 Calculator
        calculator = MACECalculator(model_paths='~/projects/rrg-ravh011/cgurwell/Ion_Channels/2024-01-07-mace-128-L2_epoch-199.model',
                                    dispersion=False, device='cuda', default_dtype='float64')
        atoms.calc = calculator

        # Set Cell Filter (preserve unit cell symmetry)
        atoms.set_constraint(FixSymmetry(atoms))

        # Run Optimise
        opt = BFGS(UnitCellFilter(atoms), trajectory=base + filename.replace('.cif', '.traj'))
        opt.run(fmax=1e-4)

        atoms.write(base + filename)