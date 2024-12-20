# TDDFT-output-and-scripts

**Description:** Data, output files, figures, and Python visualization scripts used for computational nanoscience research with Varga group.

  **-=# SEE BELOW FOR INFORMATION ON EACH FOLDER AND WHAT OUTPUT/DATA/SCRIPTS IS CONTAINED #=-**

**_FIGURES:** Contains figures, diagrams, screenshots, and images that were generated using external software sources.

**angular_distribution:** Script to visualize the angular distribution of each atom in a molecule.

<img src="angular_distribution/images/angular_distribution.png" width="400"/>

**cluster_job_run_script:** Contains python scripts to automate running jobs on the cluster. Copies directories and renames the files accordingly, then submits each job ("qsub job.pbs")

**ELI_pulse_data_and_scale:** Contains all of the laser pulse data on pulses used in ELI-ALPS Coulomb explosion experiments AND scripts to scale the laser electric fields and visualize the pulse.

<img src="_FIGURES/C4H10_snapshot_diagrams/snapshots_new_CH.png" alt="Snapshot diagram of CH formation resulting from Coulomb explosion fragmentation of butane" width="400"/>

**excel_laser_generation:** Excel sheet provided by Cody Covington. Used to generate laser pulses given different parameters.

**histograms_stats_molecule_formation:** Contains statistical data on fragment formation Coulomb Explosion in hydrocarbons AND scripts to generate these figures.

<img src="histograms_stats_molecule_formation/c4h10/karcsi_paper_histo_x_polarized/frag_charge_averages_two_axes.png" alt="Histogram of fragment formations from 88 different simulations of butane Coulomb explosion" width="400"/>

**kinematics_plot:** Script to create plots of the kinematics from a simulation trajectory.xyz file. position, speed, acceleration, and force v.s. time.

<img src="kinematics_plot/images/velocity.png" width="400"/>

**molecule_flip_rotate:** Script to flip or rotate molecules along a specified plane or axis in the dft.inp file.

**newton_plot:** Contains figures of newton plots (velocity v.s. velocity) AND scripts to generate them.

<img src="newton_plot\images\presentation\ELI-VMI.png" alt="Coulomb explosion imaging of Acetylene with 75 simulations" width="400"/>

**proton_grid_projectile:** Contains a script to copy ground state directories and adjust the locations of the proton projectile to be placed in a grid. for being launched at a molecule

<img src="proton_grid_projectile\xz_birdseye_view.jpg" alt="Grid of initial proton positions to shoot as projectiles" width="400"/>

**pulse_electron_graph:** Contains data, figures, and animations on the pulse and the number of electrons in the grid AND scripts to generate line graphs of the pulse E-field and number of electrons v.s. time.

<img src="pulse_electron_graph\info_r6.png" alt="Laser pulse electric field and number of electrons in Butane from Coulomb explosion simulation" width="400"/>

**pulse_vector_animation:** Contains animation of the electric field vector of a given pulse AND scripts to create this animation.

<img src="pulse_vector_animation\pulse_vector_screenshot.jpg" alt="Electric field vector of laser pulse" width="400"/>

**seeds_script:** Contains files of seeds for TDDFT Boltzmann distribution based runs AND scripts to generate/extend these seed files.

**speed_distribution:** Script to generate histogram distributions of the final velocities for each atom in classical and quantum Coulomb explosion.

<img src="speed_distribution/images/speed_histogram.png" width="400"/>

**trajectory_density_extract:** Script to extract trajectory files or the last time step of trajectory files. Same for their corresponding density.dat and density.bov files.

**trajectory_screenshots_mogli:** Contains generate screenshots of the a molecule at its last frame in the trajectory.xyz using mogli (https://github.com/sciapp/mogli).


**Acknowledgements:** Kalman Varga, Cody Covington
