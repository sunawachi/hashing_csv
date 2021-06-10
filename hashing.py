import pandas as pd
import hashlib
import os

def main():
    data_name = get_csv_name()

    try:
        df = pd.read_csv(data_name, header=0)
    except:
        print('No such file or directory: "%s"'% data_name)
        exit()

    target_column = get_target_column_name()

    if target_column in df.columns:
        pass
    else:
        print("The column with the specified name does not exist in the csv.")
        exit()

    hashed_df = hash_column(df, target_column)
    newname = genelate_new_csv_name(data_name)
    hashed_df.to_csv(newname)
    print("The process has been completed.")

def get_csv_name():
    try:
        s = str(input('Please input name of target csv: '))
    except ValueError:
        print("invalid input")
        exit()
    if s[-4:] == ".csv":
        return s
    else:
        print('Please input file of csv like "filename.csv".')
        exit()

def get_target_column_name():
    try:
        return str(input('Please input name of target column: '))
    except ValueError:
        print("invalid input")
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
    if os.access(filename, os.F_OK):
        return genelate_new_csv_name(newname)
    else:
        return newname

if __name__ == "__main__":
    main()
