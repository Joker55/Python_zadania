import numpy as np;
m_1 = np.random.randint(1000, size=(8, 8));
m_2 = np.random.randint(1000, size=(8, 8));
m_out1 = np.zeros((8,8));
m_out1 = np.add(m_1,m_2);
print('M_1: ' , m_1);
print('M_2: ' , m_2);
print('M_1_out: ' , m_out1);

