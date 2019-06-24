import numpy as np
import h5py
import matplotlib.pyplot as plt
from data_class import Sample


def read_data(filename, samples_arr): 
    f = h5py.File(filename,'r', swmr=True)
    prev_index = None

    for key in list(f.keys()):
        group = f[key]
        attribs = dict(group.attrs.items())
        
        # Ignore duplicates
        curr_index = int(attribs["space_group"].decode("utf-8"))
        prev_index_copy = prev_index
        prev_index = curr_index
        if (curr_index == prev_index_copy):
            continue

        material = attribs["material"].decode("utf-8")
        energy = attribs["energy_keV"]
        y_dir = attribs["y_dirs"]
        z_dir = attribs["z_dirs"]
        formula = attribs["formula"]
        abc = attribs["abc_angstrom"]
        angles = attribs["angles_degree"]
        semi_angles = attribs["semi_angles_rad"]
        d_spacing = attribs["d_hkls_angstrom"]
        space_group = attribs["space_group"].decode("utf-8")
        cbed_stack = group['cbed_stack'][()]

        x = Sample(material, energy, y_dir, z_dir, formula, abc, angles, semi_angles, d_spacing, space_group, cbed_stack)
        samples_arr.append(x)
    
    f.close()


def load(samples):
    print("Loading data:")
    for i in range(10):
        filename = "/home/user1/train/batch_train_" + str(i) + ".h5"
        try: read_data(filename, samples)
        except: continue
        print(i, len(samples))
    print("Loading successful.")
