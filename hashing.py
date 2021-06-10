import pandas as pd
import hashlib
import os

def main():
    data_name = let_input_string('Please input the name of target csv in this directory like "filename.csv"\n: ')

    if data_name[-4:] == ".csv":
        pass
    else:
        print('Please input the name of csv like "filename.csv".')
        exit()

    try:
        df = pd.read_csv(data_name, header=0, encoding="utf-8")
    except:
        print('No such file in this directory: "%s"' % data_name)
        exit()

    target_column_name = let_input_string('Please input the name of target column in the csv\n: ')

    if target_column_name in df.columns:
        pass
    else:
        print('No such column in the csv: "%s"' % target_column_name)
        exit()

    hashed_df = hash_column(df, target_column_name)
    new_data_name = genelate_new_csv_name(data_name)
    hashed_df.to_csv(new_data_name, encoding='utf_8_sig')
    print('The process has been completed.')

def let_input_string(message):
    try:
        return str(input(message))
    except ValueError:
        print('could not convert the input to a string')
        exit()

def hash_column(dataframe, columnname):
    for i in range(len(dataframe.index)):
        m = hashlib.sha256()
        b = bytes(str(dataframe.loc[dataframe.index[i], columnname]), encoding='utf8')
        m.update(b)
        dataframe.loc[dataframe.index[i], columnname] = m.digest()
    return dataframe

def genelate_new_csv_name(filename):
    newname = filename[:-4] + "_hashed.csv"
    if os.access(newname, os.F_OK):
        return genelate_new_csv_name(newname)
    else:
        return newname

if __name__ == "__main__":
    main()
