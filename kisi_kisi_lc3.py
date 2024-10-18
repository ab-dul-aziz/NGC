from fastapi import FastAPI, HTTPException, Header
import uvicorn
import pandas as pd

app = FastAPI()

@app.get('/')

def home():
    return {'message':'Silahkan pilih menu di bawah ini',
            'menu':{
                1:'/data',
                2:'/hapus_data/{id}'
            }}

trip_duration = pd.read_json('data_after_handling.csv')

# Endpoint menampilkan entry data
@app.get('/data')
def trip_data():
    return trip_duration.to_dict()

@app.delete('/hapus_data/{id}')
def del_id(id:int):
    if id in trip_duration.keys():
        del trip_duration[id]
        return {'message':f'ID {id} berhasil dihapus.'}
    else:
        raise HTTPException(status_code=404, detail=f'ID {id} tidak berhasil ditemukan')

if __name__ == '__main__':
    uvicorn.run('kisi_kisi_lc3:app', host='127.0.0.1', port=8000, reload=True)