import uvicorn
from fastapi import FastAPI, HTTPException, status, Body
import crud as database
import json

app = FastAPI()

@app.get("/")
def get_root():
    return "Hello World"

@app.get("/health")
def health_check():
    return "OK"

@app.get("/asignatura")
def get_asignatura(nombre = None):
    if nombre:
        return database.get_asig_by_name(nombre)
    else:
        return database.listar_asignaturas()


@app.get("/asignatura/{idasig}")
def get_asignatura(idasig):
    if asig := database.get_asig_by_id(idasig):
        return asig
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"La asignatura con el ID {idasig} no existe en la base de datos.")


@app.post("/insertar_asignatura", status_code=status.HTTP_201_CREATED)
def insertar_asignatura(datos = Body()):
    try:
        nuevos_datos= json.loads(datos)
        print(nuevos_datos)
        nueva = database.json_to_pithon(nuevos_datos)
        # print(nueva)
        nueva.insertar_asignatura()
        return "Asignatura insertada con éxito"
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail=f"Imposible insertar asignatura")


@app.put("/asignatura/{idasig}")
def update_asignatura(idasig, datos2 = Body()):
    try:
        nuevos_datos= json.loads(datos2)
        modificada= database.json_to_pithon_2(nuevos_datos)
        if old_idasig := database.get_asig_by_id(idasig):
            modificada.update_asig_by_id(idasig)
            return "La asignatura ha sido actualizada con éxito"
        else:
            return "El nombre de asignatura introducido no se encuentra en la base de datos"
    except Exception:
        raise HTTPException(
            # status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Error a al actualizar la asignatura.")


@app.delete("/asignatura/{idasig}", status_code=status.HTTP_204_NO_CONTENT)
def delete_asignatura(idasig):
    try:
        check= database.delete_asig_by_id(idasig)
        if check == 0:
            return "La signatura ha sido borrada con éxito"
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Imposible eliminar la asignatura.")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
