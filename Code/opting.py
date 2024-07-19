from ase import units
from ase import atoms
from ase.io import read, write
from ase.optimize import BFGS
import numpy as np
import torch

from ase.visualize import view
from ase.io import Trajectory

from ase.constraints import ExpCellFilter, StrainFilter, UnitCellFilter
from ase.spacegroup.symmetrize import FixSymmetry, check_symmetry
from spglib import get_spacegroup
from ase.calculators.loggingcalc import LoggingCalculator
import matplotlib as mpl
import matplotlib.pyplot as plt

from mace.calculators import MACECalculator

'''

ASE Calculator
https://wiki.fysik.dtu.dk/ase/ase/

MACE Initialisation
https://mace-docs.readthedocs.io/en/latest/guide/


Optimisation Using ASE
https://docs.matlantis.com/atomistic-simulation-tutorial/en/2_1_opt.html

https://docs.matlantis.com/atomistic-simulation-tutorial/en/2_2_opt_symmetry.html


'''


# Importing Stuff
calculator = MACECalculator(model_paths='/home/camgur/Documents/Coding/Chem_4PB3/Resources/2024-01-07-mace-128-L2_epoch-199.model', device='cuda', default_dtype='float64')
atoms = read('/home/camgur/Documents/Coding/Goward/MACEMP0/Resources/Elastic/Na4Sn2Ge5O16_na1na1start.cif')


# Set Calculator
atoms.calc = calculator
print(atoms.symbols, '\n')


# Set Cell filter (preserve unit cell ratioe)
# atoms = ExpCellFilter(atoms, hydrostatic_strain=False)
# atoms.set_constraint(FixSymmetry(atoms))


# Optimise
opt = BFGS(UnitCellFilter(atoms), trajectory='/home/camgur/Documents/Coding/Goward/MACEMP0/Resources/Elastic/Na4Sn2Ge5O16_na1na1start.traj')


# Run Optimise
opt.run(fmax=1e-4)
atoms.write('/home/camgur/Documents/Coding/Goward/MACEMP0/Resources/Elastic/Na4Sn2Ge5O16_na1na1startopt.cif')


print('Finished!!!')