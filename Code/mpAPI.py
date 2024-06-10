import os
import time
from mp_api.client import MPRester

# Find relative directory
module_path = os.path.dirname(os.path.realpath(__file__))

# Initialise MPRester class
mpr = MPRester(api_key='n2wdTtixZm1iaLdGBjboJmEEv4TEc4zl')

# Get structures
structures = mpr.materials.insertion_electrodes.search(working_ion='Li', fields='material_ids')

x = 0

# print(type(structures[0]))
# assert 0

# Parse structures
for structure in structures:
    id = structure.material_ids

    # Convert the structure to a CIF string and save to a CIF file
    cif = mpr.get_structure_by_material_id(id)
    if type(cif) == 'list':
        continue
    cif_data = cif.to(fmt="cif")

    # Set output directory
    output = os.path.join(module_path, 'cif/', id[0].join('.cif'))

    # Write to CIF
    with open(output, "w") as f:
        f.write(cif_data)

    x += 1

    if x%100 == 0:
        time.sleep(5)


'''
At about iteration 520:
Traceback (most recent call last):
  File "c:\Users\camgu\Goward Group\Goward Group Code\Ion_Channels\Code\mpAPI.py", line 27, in <module>
    cif_data = cif.to(fmt="cif")
               ^^^^^^
AttributeError: 'list' object has no attribute 'to'
'''