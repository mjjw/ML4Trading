"""Creating NumPy Arrays"""

import numpy as np

def test_run():
    # List to 1D array
    print np.array([2,3,4])
    # 2D array i.e., simply pass a sequence of sequences to this array
    print np.array([(2,3,4),(5,6,7)])    
    # Empty arrays with initial values
    print np.empty(5)
    
if __name__ == '__main__':
    test_run()