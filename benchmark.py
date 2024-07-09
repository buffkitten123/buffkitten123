import numpy as np
import timeit
import multiprocessing
import time
from tqdm import tqdm

def matrix_multiplication(size):
    """Perform matrix multiplication of size x size matrices."""
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = np.dot(A, B)
    return C

def single_core_benchmark(matrix_size, iterations):
    """Benchmark single-core performance and display progress."""
    for _ in tqdm(range(iterations), desc="Single-core progress"):
        matrix_multiplication(matrix_size)

def multi_core_benchmark(matrix_size, num_processes):
    """Benchmark using multiple processes and display progress."""
    start_time = time.time()
    
    with multiprocessing.Pool(num_processes) as pool:
        # Use tqdm to add a progress bar
        list(tqdm(pool.imap(matrix_multiplication, [matrix_size] * num_processes), total=num_processes, desc="Multi-core progress"))
    
    end_time = time.time()
    return end_time - start_time

# Determine the number of CPU cores
num_cores = multiprocessing.cpu_count()
print(f"Number of CPU cores available: {num_cores}")

# Define the matrix size and number of iterations for single-core benchmark
matrix_size = 1000
iterations = 10

# Measure single-core performance
single_core_start_time = time.time()
single_core_benchmark(matrix_size, iterations)
single_core_end_time = time.time()
single_core_time = single_core_end_time - single_core_start_time
print(f"Single-core execution time: {single_core_time:.2f} seconds")

# Measure multi-core performance using all available cores
multi_core_time = multi_core_benchmark(matrix_size, num_cores)
print(f"Multi-core execution time with {num_cores} cores: {multi_core_time:.2f} seconds")

# Compare results
speedup = single_core_time / multi_core_time
print(f"Speedup: {speedup:.2f}x")
