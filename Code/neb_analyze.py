import matplotlib.pyplot as plt

from mace.calculators import MACECalculator
from ase.io import read, Trajectory
from ase.neb import NEBTools

images = read(r'C:\Users\camgu\Goward Group\Code\Ion_Channels\Code\Elastic\Na22Na3.traj@-5:')

calculator = MACECalculator(model_paths=r'C:\Users\camgu\Goward Group\Code\Ion_Channels\2024-01-07-mace-128-L2_epoch-199.model', device='cpu', default_dtype='float32')

for i in images:
    i.calc = calculator

# calculators = [image.calc for image in images
                    #    if image.calc is not None]
# for image in images:
#     print(images)
#     print("\n")
#     for i in image:
#         print(i)
#     print("\n")
        

# print( len(set(calculators)))
# print( len(calculators))


# assert 0


print('ye')
nebtools = NEBTools(images)
print('yeah')



# assert 0
# Get the calculated barrier and the energy change of the reaction.
Ef, dE = nebtools.get_barrier()
print('ye')


# Get the barrier without any interpolation between highest images.
Ef, dE = nebtools.get_barrier(fit=False)
print('ye')

# Get the actual maximum force at this point in the simulation.
max_force = nebtools.get_fmax(allow_shared_calculator=True)
print('ye')

# Create a figure like that coming from ASE-GUI.
fig = nebtools.plot_band()
# fig.savefig('diffusion-barrier.png')
print('ye')

# Create a figure with custom parameters.
fig = plt.figure(figsize=(5.5, 4.0))
ax = fig.add_axes((0.15, 0.15, 0.8, 0.75))
nebtools.plot_band(ax)
# fig.savefig('diffusion-barrier.png')
plt.show()