import re
import json
import numpy as np

p = [1,2,3]
p.extend(np.zeros(3))
# print(p.extend(list(np.zeros(2))))
print(p)