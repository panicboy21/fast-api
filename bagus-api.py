from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

students = {
    "Aqila": {
        "score": 85,
        "age": 24
    },
    "Catherine": {
        "score": 82,
        "age": 20
    },
    "Bagus": {
        "score": 88,
        "age": 28
    },
    "Adriansyah": {
        "score": 86,
        "age": 27
    },
    "Rahardiansyah": {
        "score": 83,
        "age": 26
    }
}

# base url itu adalah secara default adalah
# http://127.0.0.1:8000
#static url harus diatas dinamis
@app.get("/") # `/` setara dengan base url
def home():
    return {"message": "Hello World"}

#static url
@app.get('/students')
def student():
    return students

@app.get('/hacktiv-rmt-27')
def info_rmt_27():
    return {
        "message": "Hacktiv RMT 27 adalah murid batch remote yang sudah dilatih di Hacktiv selama 3 bulan dengan skill yang dibutuhkan oleh perusahaan "
    }

# dinamic url
@app.get('/{name}')
def findStudentName(name:str):
    if name in students.keys():
        return students[name]
    else:
        raise HTTPException(status_code=404, detail='Murid tidak ditemukan')

@app.post('/students')
def addStudent(studentData:dict): # untuk method post dan put pasti sifat variable nya dictionary
    print('StudentData: ', studentData)
    studentName = studentData['name']
    studentScore = studentData['score']
    studentAge = studentData['age']

    students[studentName] = {
        "score": studentScore,
        "age": studentAge
    }

    return {"messsage": "Student berhasil ditambahkan"}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)