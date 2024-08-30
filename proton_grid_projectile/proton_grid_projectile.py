import os
import shutil
import subprocess

# Function to update the dft.inp file
class Proton_grid_projectile():
    def __init__(self, d, n, m):
        self.num_atoms = None
        self.lines = []
        self.d = d  # distance between points on i to n axis
        # Number of iterations for i and j
        self.n = n  # Replace with your desired value for n
        self.m = m  # Replace with your desired value for m  
        self.proton_line_index = None
        self.original_working_directory=os.getcwd()

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def read_original_dft_inp(self, file_path):
        with open(file_path, 'r') as file:
            self.lines = file.readlines()

        line_num = -1

        # Find the first integer in the file that is not preceded by a hashtag
        for line in self.lines:
            line_num += 1
            if not line.strip().startswith("#"):
                parts = line.split()
                for part in parts:
                    if part.isdigit():
                        self.num_atoms = int(part)
                        break
                if self.num_atoms is not None:
                    break

        if self.num_atoms is None:
            raise ValueError("No integer value found in the dft.inp file.")

        # Increment the number of atoms by 1
        self.num_atoms += 1
        self.lines[line_num] = f"{str(self.num_atoms)} 2 2 2\n"

        new_atom_line = "0.000000\t0.000000\t0.000000 1 1\n"
        # Find the correct insertion index
        for i in range(len(self.lines) - 2, -1, -1):
            stripped_line = self.lines[i].strip()
            if stripped_line and self.is_float(stripped_line.split()[0]):
                self.proton_line_index = i + 1
                break

        if self.proton_line_index is None:
            raise ValueError("No suitable insertion point found in the dft.inp file.")

        # Insert the new atom line at the found index
        self.lines.insert(self.proton_line_index, new_atom_line)

    def update_dft_inp(self, file_path, x, z, d):
        # Calculate the new atom position
        new_atom_x = x * d
        new_atom_y = 5
        new_atom_z = z * d / 2 - d

        # Add the new atom to the end of the atom list
        new_atom_line = f"{new_atom_x: .6f}\t{new_atom_y: .6f}\t{new_atom_z: .6f} 1 1\n"
        self.lines[self.proton_line_index] = new_atom_line

        # Write the updated lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(self.lines)

    def run(self, new_dir, i, j, execute=True):
        # Path to the job script
        job_script_path = os.path.join(new_dir, "job_script.sh")

        # Read the job script file
        with open(job_script_path, 'r') as file:
            job_script_lines = file.readlines()

        # Modify the job name line
        job_script_lines[1] = f"#SBATCH --job-name=C2H2_grid_x{i}z{j}\n"

        # Write the updated job script back to the file
        with open(job_script_path, 'w') as file:
            file.writelines(job_script_lines)

        new_abs_path = os.path.abspath(new_dir)
        # Calculate the relative path and count how many levels to go up
        relative_path = os.path.relpath(new_abs_path, start=self.original_working_directory)
        num_levels_up = relative_path.count(os.sep)  # Count the number of directory separators
    
        # Change directory to the new directory
        os.chdir(new_dir)

        # Optionally execute the job script using sbatch
        if execute:
            #subprocess.run(["sbatch", "job_script.sh"])
            print("sbatch job_script")

        os.chdir("..")
        for _ in range(num_levels_up):
            os.chdir("..")


def main():
    d = 0.6025963854  # distance between points on i to n axis

    # Number of iterations for i and j
    # x goes from 0 to n, z goes from 0 to m
    n = 3  # Replace with your desired value for n
    m = 4  # Replace with your desired value for m
    
    proton_grid_projectile = Proton_grid_projectile(d, n, m)

    original_dir = "proton_grid_projectile/c2h2_gs/"
    original_dft_inp = original_dir + "dft.inp"

    proton_grid_projectile.read_original_dft_inp(original_dft_inp)

    # Loop through i and j, create new directories, and update dft.inp
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            # Create the new directory name
            new_dir = f"proton_grid_projectile/c2h2_proton_x{i}z{j}_gs"

            # Check if the directory exists
            if not os.path.exists(new_dir):
                # Copy the original directory to the new directory
                shutil.copytree(original_dir, new_dir)

            # Path to the dft.inp file in the new directory
            dft_inp_path = os.path.join(new_dir, "dft.inp")

            # Update the dft.inp file
            proton_grid_projectile.update_dft_inp(dft_inp_path, i, j, d)
            print(dft_inp_path, "created and updated.")

            # Run the job script in the new directory
            proton_grid_projectile.run(new_dir, i, j)

    print("Directories and dft.inp files have been successfully updated.")


if __name__ == '__main__':
    main()
