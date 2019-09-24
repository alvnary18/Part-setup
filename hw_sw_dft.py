import pandas as pd
import time

start_time = time.time()
if __name__ == '__main__':
    # filling the tanglible value from hw, sw sheet
    file = 'C:/Projects HP/Part setup/'
    dft = "cs.csv"
    hw = "HW.csv"
    ven = "vendor.csv"
    swp = "swop.csv"
    rd = pd.read_csv(file + dft)#read dft results of cs.csv
    hw1 = pd.read_csv(file + hw)# read tangible data of hw.csv
    ve = pd.read_csv(file + ven)# read HP Procurement vendor of vendor.csv
    sw = pd.read_csv(file + swp)# read SWOP Update(Y/N) of swop.csv
    # get the result of HW and SW
    result = pd.merge(rd, hw1)
    # get the swap flag result
    result1 = pd.merge(result, sw)
    # get the HP Procurement vendor
    result2 = pd.merge(result1, ve)

    result2.to_csv(file + "final_output_3.csv", columns=['Type of Txn', 'Object', 'Buyer User Login', 'Region', 'Customer Name(opt)', 'Deal ID(opt)','M-Vendor', 'Manf Prod Number', 'Customer Hyphenation', 'HP Prod Number','Product Classification', 'Tax Classification Code', 'Short Desc', 'Long Desc','500 Char Desc', 'Product Line', 'UNSPSC Code', 'Phweb M-Level', 'GA Update(Y/N)','EAN Category', 'EAN-UPC', 'Unit Of Measure', 'SWOP Update(Y/N)', 'Weight Unit', 'Net weight','Gross weight', 'Dimension unit', 'Box length', 'Box width', 'Box height','Local currency Name', 'Average HP Purchasing price', 'Supplier list price', 'IATA code','EPEAT status level', 'EPEAT status date (MM/DD/YYYY)', 'TAA', 'Screen size','HP supplier codes (max = 10) 4 digits', 'delivering plants (max = 10) 4 digits','One reference material (combination)', 'Buyer purch group', 'serial Profile','HP Procurement vendor', 'Supplier Prod Number', 'Primary Supplier(Y/N)','Purchasing plant Plants(PIR)', 'Country Of Origin', 'Currency name','HP Purchasing Price from Supplier', 'PIR Purchasing Group', 'Manufacturer', 'MFgPartNum', 'MFgPartNum1', 'MFgPartNum2', 'MFgPartNum3', 'MFgPartNum4', 'MFgPartNum5', 'MFgPartNum6', 'MFgPartNum7', 'MFgPartNum8', 'MFgPartNum9', 'MFgPartNum10'])

print("--- %s seconds ---" % (time.time() - start_time))
