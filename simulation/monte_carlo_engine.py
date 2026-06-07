import numpy as np
import matplotlib.pyplot as plt

nominal_peg_diameter = 10.0
nominal_hole_diameter = 10.1
nominal_hole_position_x = 0.0
nominal_hole_position_y = 0.0

peg_diameter_tolerance = 0.05
hole_diameter_tolerance = 0.05
hole_position_tolerance = 0.1
robot_position_std = 0.05

n_samples = 10000

peg_diameters = np.random.normal(nominal_peg_diameter, peg_diameter_tolerance / 3, n_samples)
hole_diameters = np.random.normal(nominal_hole_diameter, hole_diameter_tolerance / 3, n_samples)

angles = np.random.uniform(0, 2 * np.pi, n_samples)
radii = np.random.uniform(0, hole_position_tolerance / 2, n_samples)
hole_pos_x = radii * np.cos(angles)
hole_pos_y = radii * np.sin(angles)

robot_pos_x = np.random.normal(0, robot_position_std, n_samples)
robot_pos_y = np.random.normal(0, robot_position_std, n_samples)

clearance = (hole_diameters - peg_diameters) / 2
offset = np.sqrt((hole_pos_x - robot_pos_x)**2 + (hole_pos_y - robot_pos_y)**2)

success = clearance > offset
success_rate = np.mean(success)

print(f"Assembly success rate: {success_rate * 100:.2f}%")

plt.figure(figsize=(10, 6))
plt.scatter(offset[success], clearance[success], alpha=0.3, label='Success', s=5, color='blue')
plt.scatter(offset[~success], clearance[~success], alpha=0.3, label='Failure', s=5, color='red')

plt.xlabel('Position Offset (mm)')
plt.ylabel('Clearance (mm)')
plt.title(f'Monte Carlo Peg-in-Hole Assembly: {success_rate * 100:.1f}% Success Rate')
plt.legend()
plt.grid(True)

plt.savefig('assembly_simulation.png', dpi=150)
plt.show()
