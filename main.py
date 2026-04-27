#print("Here will be my backand")
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import db
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # разрешить запросы с ЛЮБЫХ доменов
    allow_methods=["*"],   # …любыми методами
    allow_headers=["*"],   # …и любыми заголовками
)

@app.get("/all_messages")
def show_messages(id):
    try:
        return {"message":db.show_messages(id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_message")
def del_message(id):
    try:
        result = db.delite_message(id)
        if result:
            return {"message": f"сообщение с ID {id} удалено"}
        else:
            raise HTTPException(status_code=404, detail="сообщение не найдено")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/")
def del_contact(id):
    try:
        result = db.delite_contact(id)
        if result:
            return {"message": f"контакт с ID {id} удален"}
        else:
            raise HTTPException(status_code=404, detail="контакт не найден")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/get_profile")
def show_profile(id):
    try:
        return db.show_profile(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/show_contacts")
def show_contacts(id):
    try:
        return db.show_contacts(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/add_contact")
def add_contact(id):
    try:
        db.add_contact(id)
        return {"message": "контакт успешно добавлен"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/enter_message")
def enter_message(autor: int,text: str,chatname: str):
    try:
        db.enter_message(autor, text, chatname)
        return {"message": "сообщение отправлено"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/change_profile")
def change_profile(id, password, email, username, city):
    try:
        db.change_profile(id, password, email, username, city)
        return {"message": "профиль изменен"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
