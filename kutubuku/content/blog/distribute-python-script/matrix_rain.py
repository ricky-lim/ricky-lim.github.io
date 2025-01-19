# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "numpy~=2.0",
# ]
# ///

import numpy as np
import time
import os

def create_matrix_rain():
    width = 50
    height = 15
    
    while True:
        # Generate random matrix
        matrix = np.random.randint(2, size=(height, width))
        
        # Clear screen
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Convert to ASCII art
        for row in matrix:
            print(''.join(['*' if cell else ' ' for cell in row]))
            
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        print("Starting Matrix Rain...")
        create_matrix_rain()
    except KeyboardInterrupt:
        print("\nMatrix Rain Terminated!")