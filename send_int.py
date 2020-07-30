from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    idata = 2300
    comm.send(idata, dest=1)
    print(f'Rank {rank} sends {idata}')
elif rank == 1:
    data = comm.recv(source=0)
    print(f'Rank {rank} receives {data}')
else:
    print(f'Rank {rank} does nothing')
    
