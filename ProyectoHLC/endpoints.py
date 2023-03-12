from crud import Asignatura
#from pokemon_service.entity import Pokemon
from fastapi import APIRouter, HTTPException, status, Body

get_db("/asignatura")
def get_asignatura(nombre_asignatura = None):
    if nombre_asignatura:
        return get_db.get_asig_by_name(nombre_asignatura)
    else:
        return get_db.listar_asignaturas()

"""
@router.get("/alumno/{nombre}_{apellidos}")
def get_alumno(nombre, apellidos):
    if alu := get_db.get_alum_by_name(nombre, apellidos):
        return alu
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"El alumno {apellidos}, {nombre} no existe en la base de datos.")


@router.post("/pokemon", status_code=status.HTTP_201_CREATED)
def create_pokemon(pokemon = Body()):
    try:
        return get_db().save(Pokemon(pokemon.get("name"), pokemon.get("pkmn_type")))
    except Exception:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Couldn't save new pokemon {pokemon}")


@router.put("/pokemon/{pokemon_id}")
def update_pokemon(pokemon_id, pokemon = Body()):
    try:
        return get_db().save(Pokemon(pokemon_id, pokemon["name"], pokemon["pkmn_type"]))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Couldn't update pokemon ID {pokemon_id} with {pokemon}")


@router.delete("/pokemon/{pokemon_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pokemon(pokemon_id):
    try:
        get_db().delete(pokemon_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Couldn't delete pokemon ID {pokemon_id}")
"""