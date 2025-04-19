from typing import Sequence, Iterable, Callable
from utils import allFloats

# bbox = [minx, miny, maxx, maxy]

africa_bbox = [
    -18.022376915540377,
    -36.631667126187935,
    54.422534599309245,
    38.309187802512156
]

brazil_bbox = [
    -74.17935124250016,
    -22.8443429976208,
    -34.66405004888776,
    5.337248309614139
]

# Inside the boundary
africa_chad_bbox = [
    13.669204215230337,
    7.488620023885076,
    24.108788022973926,
    23.6838459645045
  ]

# Outside the boundary
bahia_bbox = [
    -47.75168445188001,
    -15.705403381680512,
    -40.12271304066891,
    -9.769839216364048
]

def it_contains(a, b):
    """
        Determine if bounding box B is within bounding box A. 
    """

    if not isinstance(a, Sequence) or not isinstance(b, Sequence):
        return False

    if not 4 >= len(a) <= 6 or not 4 >= len(b) <= 6: return False

    if not allFloats(a) or not allFloats(b):
        return False

    return (a[0] <= b[0] and b[2] <= a[2]) and (a[1] <= b[1] and b[2] <= a[2])

def main():

    # Should be True
    print( it_contains(brazil_bbox, bahia_bbox) )
    print( it_contains(africa_bbox, africa_chad_bbox) )
    
    # Should be False
    print( it_contains(brazil_bbox, africa_chad_bbox)  )
    print( it_contains(africa_bbox, bahia_bbox) )




if __name__ == "__main__":
    main()