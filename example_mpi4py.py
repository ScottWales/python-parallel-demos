#!/g/data/hh5/public/apps/miniconda3/envs/analysis3/bin/python
## Scott Wales 2024

from mpi4py import MPI

def hello(task):
    print(f"Hello {task}")

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        print(f"mpi4py with {comm.Get_size()} workers")

    hello(rank)

if __name__ == '__main__':
    main()
