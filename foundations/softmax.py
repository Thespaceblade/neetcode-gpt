import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        exponentials = (np.exp(z - np.max(z)))
        denominator = np.sum(exponentials)
        answer = exponentials/denominator
        return np.round(answer, 4)
        pass
