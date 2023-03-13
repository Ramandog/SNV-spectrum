import numpy as np

class Snv( ):

            def __init__(self):       
                        pass 

            def snv(self, data):
            
                        typeX = type(data)
                        if typeX == list:
                                    data = np.array(data).astype(float)
                        elif typeX == np.float32 or typeX == float or typeX == np.int32 or typeX == int:
                                    data = np.array([data]).astype(float)
                        
                        if len(data.shape) == 1:
                                    data = data.reshape(1, data.shape[0])

                        m = data.shape[0]
                        n = data.shape[1]

                        data_std = np.std(data, axis=1)
                        data_average = np.mean(data, axis=1)
                        data_snv = [[((data[i][j] - data_average[i]) / data_std[i]) for j in range(n)] for i in range(m)]

                        return  np.array(data_snv)