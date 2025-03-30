import pandas as pd 

class load_data:
    def __init__(self,file_path=None):
        self.file_path=file_path
        self.data=None
    
    def import_data(self):
        #checking if the file path is provided
        if self.file_path:
            try:
                data=pd.read_csv(self.file_path)
                print("data loaded successfully")
                return data.head()
            
            except Exception as e:
                print("error loading : {e}")

        else:
            print("no file path provided")

loader=load_data("/Users/puravgupta/Desktop/python/streamli_test/data/kdrama_DATASET1.csv")
df=loader.import_data()
print(df)
