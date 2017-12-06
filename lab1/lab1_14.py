import numpy as np;

s = np.random.randint(10);
m_1 = np.random.randint(100, size=(s, s));
det = np.linalg.det(m_1);
print (m_1);
print(det);