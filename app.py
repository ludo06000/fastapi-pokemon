from fastapi import FastAPI, Path, HTTPException
from dataclasses import dataclass
from typing import Union
import json

with open('pokemons.json', 'r') as file :
    pokemons = json.load(file)

list_pokemons = {k+1:v for k,v in enumerate(pokemons)}

@dataclass
class Pokemon():
    id: int
    name: str
    types: list[str]
    total: int
    hp: int
    attack: int
    defense: int
    attack_special: int
    defense_special: int
    speed: int
    evolution_id: Union[int, None] = None

app = FastAPI()

@app.get("/total_pokemons")
def get_total_pokemons() -> dict :
    nombre_pokemons = len(list_pokemons)
    return {"total_pokemons": nombre_pokemons}

@app.get("/pokemons")
def get_all_pokemons() -> list[Pokemon] :
    res = []
    for id in list_pokemons:
        res.append(Pokemon(**list_pokemons[id]))
    return res

@app.get("/pokemon/{id}")
def get_pokemon_by_id(id: int = Path(ge=1)) -> Pokemon :
    if id not in list_pokemons:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return Pokemon(**list_pokemons[id])