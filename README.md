ML training interatomic potential for Uranium Nitride defect behaviors prediction

Install MLIP-3, LAMMPS-MLIP-3 interface, VASP needed, NERSC environment

Begin with a initial.lmp sctructure, a pot.almtp potential, and a training set.

To start loop, sbatch run_lmp.sm first, it will generate preselected.cfg, then automatically submit run_vasp.sm

run_vasp.sm selects configurations from preselected.cfg and submits vasp jobs for DFT, at the end, submits checksvasp.sm

checksvasp.sm is checking if all vasp jobs finished, automatically submits run_convert.sm if all vasp jobs completed.

run_convert.sm adding vasp output to trainings set, then automatically submits run_mlp.sm.

run_mlp.sm trains machine learning interatomic potential based on updated train.cfg, and submits run_lmp.sm with the updated potential.

Loops continue until no preselected.cfg generated, then in.npt and initial.lmp can be adjusted and start new training.

