#!/bin/bash
#SBATCH -A m4796  # e.g., m1111
#SBATCH -C gpu
#SBATCH -q shared
#SBATCH -N 1
#SBATCH -G 2
#SBATCH -n 2
#SBATCH -t 6:00:00
#SBATCH -J svasp
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err

# Record the start time
start_time=$(date +%s)
echo "Job started at: $(date)"

module load vasp/6.4.3-gpu

# One can use up to 16 OpenMP threads-per-MPI-rank when using
#  4 GPUs-per-node.
export OMP_NUM_THREADS=2
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

# Run 8 MPI ranks (-n 8) with 8 GPUs (-G 8) on 2 nodes:
#  The number of MPI ranks MUST match the number of GPUs.
#  The number of GPUs-per-node may not exceed 4.
#  Set -c ("--cpus-per-task") = 32 for the ideal MPI rank spacin
#bash -c 'echo "Rank $SLURM_PROCID on $(hostname) using GPU: $(nvidia-smi --query-compute-apps=pid --format=csv)"'
srun vasp_ncl

# Record the end time
end_time=$(date +%s)
# Calculate and output the job duration
duration=$((end_time - start_time))
echo "Job finished at: $(date)"
echo "Job running time: $(($duration / 3600))h $(($duration % 3600 / 60))m $(($duration % 60))s"
