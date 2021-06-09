import pandas as pd
import hashlib
import os

def main():
    data_name = get_csv_name()
    if if_exsists_in_cd(data_name):
        pass
    else:
        print('No such file or directory: "%s"'% data_name)
        exit()
    df = pd.read_csv(data_name, header=0)
    target_column = get_target_column_name()
    check_if_the_column_exists_in_df(target_column, df)
    hashed_df = hash_column(df, target_column)
    newname = new_csv_name(data_name)
    hashed_df.to_csv(newname)
    print("The process has been completed.")

def get_csv_name():
    try:
        csv_name = str(input('Please input name of target csv: '))
    except ValueError:
        print("invalid input")
        exit()
    if csv_name[-4:] == ".csv":
        return csv_name
    else:
        print('Please input file of csv like "filename.csv".')
        exit()

def if_exsists_in_cd(filename):
    if os.access(filename, os.F_OK):
        return True
    else:
        return False

def get_target_column_name():
    try:
        return str(input('Please input name of target column: '))
    except ValueError:
        print("invalid input")
        exit()

def check_if_the_column_exists_in_df(columnname, dataframe):
    if columnname in dataframe.columns:
        pass
    else:
        print("The column with the specified name does not exist in the csv.")
        exit()

def hash_column(dataframe, columnname):
    for i in range(len(dataframe.index)):
        m = hashlib.sha256()
        b = bytes(str(dataframe.loc[dataframe.index[i], columnname]), encoding='utf8')
        m.update(b)
        dataframe.loc[dataframe.index[i], columnname] = m.digest()
    return dataframe

def new_csv_name(filename):
    newname = filename[:-4] + "_hashed.csv"
    if if_exsists_in_cd(newname):
        return new_csv_name(newname)
    else:
        return newname

if __name__ == "__main__":
    main()
