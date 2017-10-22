import pandas as pd
import tkinter
import tkinter.filedialog as tkfl
import glob
import os

#読み込むフォルダパスを取得(返り値：フォルダパス(str))
def getreaddir_path():
    tk = tkinter.Tk()
    tk.withdraw()  
    readf_path = tkfl.askdirectory()

    return readf_path

#出力ファイル名の取得
def getwritef_path():
    tk = tkinter.Tk()
    tk.withdraw()  
    writef_path = tkinter.filedialog.asksaveasfilename(filetypes=[('csv file','*.csv')])

    return writef_path
    
#指定されたフォルダ内の
def read(f_path):
    data_list = []

    #指定のフォルダからすべてのcsvファイルのパスをリスト化
    files = glob.glob(os.path.join(f_path,'*.csv')) 

    #ヘッダーファイルの読み込み
    headerfile = ".\\data\\matrix_columns.txt"
    with open (headerfile, 'r', encoding='utf-8') as input:
        data = input.read()
        data = data.split('\n')

    #フォルダ内のCSVファイルをすべて読み込み、条件に一致するレコードを取り出す
    for file in files:
        temp_f = pd.read_csv(file,names=data,encoding='shift_jis')
        temp_f['filename'] = os.path.basename(file)
        data_list.append(temp_f)

    #リスト化されたデータフレームを結合。indexも降りなおす
    data_f = pd.concat(data_list, ignore_index=True)

    return data_f

def select(data_f, name, value):
    select_f = data_f[data_f[name].isin(value)]

    return select_f
    

#データフレームをファイル出力
def matrix_to_csv(data_f, wf_path):
    data_f.to_csv(path_or_buf=wf_path)

    return True
    
if __name__ == "__main__":
    data_f = read(getreaddir_path())

    name  = '格付会社コード'
    value = [1]
    select_f = select(data_f, name, value)

    matrix_to_csv(select_f, getwritef_path())