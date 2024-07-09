import numpy as np
import timeit
import multiprocessing
import time

def matrix_multiplication(size):
    """Perform matrix multiplication of size x size matrices."""
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = np.dot(A, B)
    return C

def multi_core_benchmark(matrix_size, num_processes):
    """Benchmark using multiple processes."""
    start_time = time.time()
    
    with multiprocessing.Pool(num_processes) as pool:
        pool.map(matrix_multiplication, [matrix_size] * num_processes)
    
    end_time = time.time()
    return end_time - start_time

# Determine the number of CPU cores
num_cores = multiprocessing.cpu_count()
print(f"Number of CPU cores available: {num_cores}")

# Define the matrix size
matrix_size = 1000

# Measure single-core performance
single_core_time = timeit.timeit('matrix_multiplication(matrix_size)', globals=globals(), number=10)
print(f"Single-core execution time: {single_core_time:.2f} seconds")

# Measure multi-core performance using all available cores
multi_core_time = multi_core_benchmark(matrix_size, num_cores)
print(f"Multi-core execution time with {num_cores} cores: {multi_core_time:.2f} seconds")

# Compare results
speedup = single_core_time / multi_core_time
print(f"Speedup: {speedup:.2f}x")
