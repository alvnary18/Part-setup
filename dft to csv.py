import pandas as pd
import pandas
import os
import time
start_time = time.time()
if __name__ == '__main__':
    # converting the null values of DFT results to merged cs.csv file
    path = os.chdir('C:/Projects HP/Part setup/')
    data = pd.read_csv('DFT results.csv')
    dft = pd.DataFrame(data,
                       columns={'RequestID', 'Tangible', 'ContactName', 'ManufacturerName', 'Product Line', 'Vendor',
                                'Weight', 'Length', 'Width', 'Height', 'COO', 'MFgPartNum', 'MFgPartNum1'},
                       index=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    #df = dft.dropna(thresh=2)
    df = data.dropna(thresh=2)
    df.to_csv("cs.csv", columns =['RequestID', 'Tangible', 'ContactName', 'ManufacturerName', 'Product Line', 'Vendor',
                                'Weight', 'Length', 'Width', 'Height', 'COO', 'MFgPartNum', 'MFgPartNum1',
                                'MFgPartNum2', 'MFgPartNum3', 'MFgPartNum4', 'MFgPartNum5', 'MFgPartNum6',
                                'MFgPartNum7', 'MFgPartNum8', 'MFgPartNum9', 'MFgPartNum10'])


print("--- %s seconds ---" % (time.time() - start_time))

















