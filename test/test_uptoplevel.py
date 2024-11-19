import numpy as np
from PyUncertainNumber.UP.uncertaintyPropagation import up_bb
from PyUncertainNumber import UncertainNumber as UN


# import user-defined function
USER_dir = '../user_dir'
import sys
sys.path.append(USER_dir)

TEST_method = "subinterval"


# define the function Ioann style
def cantilever_beam_deflection(x):
    """Calculates deflection and stress for a cantilever beam.

    Args:
        x (np.array): Array of input parameters:
            x[0]: Length of the beam (m)
            x[1]: Second moment of area (mm^4)
            x[2]: Applied force (N)
            x[3]: Young's modulus (MPa)

    Returns:
        float: deflection (m)
               Returns np.nan if calculation error occurs.
    """

    beam_length = x[0]
    I = x[1]
    F = x[2]
    E = x[3]
    try:  # try is used to account for cases where the input combinations leads to error in fun due to bugs
        deflection = F * beam_length**3 / (3 * E * 10**6 * I)  # deflection in m
        
    except:
        deflection = np.nan

    return deflection

y = UN(name='beam width', symbol='y', units='m', essence='interval', bounds=[0.145, 0.155])
L = UN(name='beam length', symbol='L', units='m', essence='interval', bounds=[9.95, 10.05])
I = UN(name='moment of inertia', symbol='I', units='m', essence='interval', bounds=[0.0003861591, 0.0005213425])
F = UN(name='vertical force', symbol='F', units='kN', essence='interval', bounds=[11, 37])
E = UN(name='elastic modulus', symbol='E', units='GPa', essence='interval', bounds=[200, 220])


# Ioanna style




# Leslie style
a = up_bb(vars=['L', 'I', 'F', 'E'], 
          fun=cantilever_beam_deflection, 
          n = None, 
          method = TEST_method, 
          save_raw_data = "yes", 
          base_path = USER_dir,
        #   name='deflection', 
        #   symbol='D'
         )