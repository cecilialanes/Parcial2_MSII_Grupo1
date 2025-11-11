#test/test_promedio.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funciones.promedioolmedo import promedio
def test_promedio():
 assert promedio([2, 4, 6]) == 4
 assert promedio([]) is None
