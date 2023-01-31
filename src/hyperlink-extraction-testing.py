from openpyxl import load_workbook
import openpyxl
import os
import pandas as pd
from src.utils import data_cleaner
import re
 
 
def Find(string):
 
    # Use a regular expression pattern to match URLs
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    links = re.findall(pattern, string)
    
    # Return the first link if any are found, or None if not
    return links[0] if links else None

test_data_dir  = os.path.join("artifacts","new_test_data")
test_data_files_name =  os.listdir(test_data_dir)

import pandas as pd
from openpyxl import load_workbook

for file_name in test_data_files_name[:]:
    print()
    print(f" =========== File Name : {file_name} ============")
    
    # if file_name != "MSURESH.xlsx":
    #     continue

    df = pd.read_excel(os.path.join(test_data_dir,file_name), None)
    sheet_names = list(df.keys())
    cur_sheet = df[sheet_names[0]]
    columns_name = list(cur_sheet.columns)

    wb = openpyxl.load_workbook(os.path.join(test_data_dir,file_name))
    ws = wb[sheet_names[0]]

    cols_link = []

    for cur_col in range(1,len(columns_name)+1):
        
        if ws.cell(row = 12, column = cur_col).value is not None:
            cur_link = ws.cell(row = 12, column = cur_col).hyperlink

            if cur_link is not None:
                if cur_link.target is not None:
                    cols_link.append((columns_name[cur_col-1],cur_col))

            else:
                if type(ws.cell(row = 12, column = cur_col).value) == str:
                    if Find(ws.cell(row = 12, column = cur_col).value) is not None:
                        cols_link.append((columns_name[cur_col-1],cur_col))

    cur_sheet = df[sheet_names[0]]
    df,correct_row_idx = data_cleaner.correct_df_headers(cur_sheet)
    
    df_link = pd.DataFrame()

    total_link_columns = len(cols_link)

    if total_link_columns == 0:
        continue

    for j in range(len(cols_link)):
        df_link[df.columns[cols_link[j][1]-1] + "_link"] = [None]*len(df)

    t = 0

    for i in range(correct_row_idx+3,ws.max_row+1):
        
        for j in range(len(cols_link)):

            cur_cell = ws.cell(row=i,column=cols_link[j][1])
            
            # If completely empty simply return None
            if cur_cell.value is None and cur_cell.hyperlink is None:
                df_link[df.columns[cols_link[j][1]-1] + "_link"].iloc[t] = None
                continue

            # If hyperlink is not None
            cur_hyperlink_value = cur_cell.hyperlink

            if cur_hyperlink_value is not None:
                
                # If hyperlink is not given
                if cur_hyperlink_value.target is not None:
                    df_link[df.columns[cols_link[j][1]-1] + "_link"].iloc[t] = cur_hyperlink_value.target
                    continue

            # If hyperlink is None or hyperlink.target is None
            else:
                df_link[df.columns[cols_link[j][1]-1] + "_link"].iloc[t] = Find(cur_cell.value)
            
        t+=1

    print("+==========================+")
    
    print(len(df_link) == len(df))

    print(df.head(3))

    df = pd.concat([df,df_link],axis=1)

    print(df.head(5))