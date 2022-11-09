import bz2file as bz2
import pickle

rf_final = pickle.load(open('C:/Users/mansi/OneDrive/Desktop/Study/Data_Science_Projects/Quora_Question_Pairs/pythonProject1/rf_final.pkl','rb'))

#compressing pkl file
def compressed_pickle(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w') as f:
        pickle.dump(data, f)

compressed_pickle('model_compressed',rf_final)

# def decompress_pickle(file):
#
# data = bz2.BZ2File(file, ‘rb’)
# data = pickle.load(data)
# return data
#
# model = decompress_pickle(‘filename.pbz2’)