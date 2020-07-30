# parallelmap.py
from mpi4py import MPI
import time
import numpy as np

def myfunc(x):
    time.sleep(0.2)
    return np.sqrt(x)

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()   

if rank==0:
  start = time.perf_counter()

x = range(20)
m = int(np.ceil(float(len(x)) / size))
x_chunk = x[rank*m:(rank+1)*m]
r_chunk = list(map(myfunc, x_chunk))

r = comm.gather(r_chunk, root=0)

if rank==0:
  end = time.perf_counter()
  print(np.array(r))
  print(f'Elapsed time: {end - start:.04} s')
