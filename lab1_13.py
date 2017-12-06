import numpy as np;
m_1 = np.random.randint(2, size=(2, 2));
m_2 = np.random.randint(2, size=(2, 2));

rows_1 = len(m_1)
cols_1 = len(m_1[0])
rows_2 = len(m_2)
cols_2 = len(m_2[0])

m_out2 = [[0 for row in range(cols_2)] for col in range(rows_1)]

for i in range(rows_1):
    for j in range(cols_2):
        for k in range(cols_1):
            m_out2[i][j] += m_1[i][k] * m_2[k][j]

print('M_1: \n', m_1);
print('M_2: \n', m_2);
print('M_2_out:  \n', m_out2);
