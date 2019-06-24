import matplotlib.pyplot as plt

class Sample:
    def __init__(self, material, energy, y_dir, z_dir, formula, abc, angles,semi_angles, d_spacing, space_group, image_stack):
        self.material = material
        self.energy = energy
        self.y_dir = y_dir
        self.z_dir = z_dir
        self.formula = formula
        self.abc = abc
        self.angles = angles 
        self.semi_angles = semi_angles
        self.d_spacing = d_spacing
        self.space_group = int(space_group)
        self.image_stack = image_stack
    
    def print(self):
        print("material:{}, energy:{}, y_dir:{}, z_dir:{}, formula:{}, abc:{}, angles:{}, semi_angles:{}, d_spacing:{}, space group: {}".format(self.material, self.energy, self.y_dir, self.z_dir, self.formula, self.abc, self.angles, self.semi_angles, self.d_spacing, self.space_group))

    def plot(self):
        fig, axes = plt.subplots(1,3, figsize=(16,12))
        for ax, cbed in zip(axes.flatten(), self.image_stack):
            ax.imshow(cbed**0.25, cmap='gnuplot2')
            ax.axis('off')
        plt.show()