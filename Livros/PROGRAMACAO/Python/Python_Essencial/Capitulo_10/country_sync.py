import json
import asyncio
import random
import requests as req 
import aiohttp
from time import perf_counter
from country_util import api_url, codes2a

# Exemplo 1

def http_get_country_name(code:str) -> str:
    resp = req.get(f"{api_url}{code}")
    
    json_data = resp.json()
    dados_json = json.dumps(json_data)
    
    dados_dict = json.loads(dados_json)[0]
    name = dados_dict['name']['common']
    return name

def get_names_sync() -> list:
    nomes = []
    for code in random.choices(codes2a, k=10):
        nome = http_get_country_name(code)
        nomes.append(nome)
        
        return nomes
    
inicio = perf_counter()
print("Execução iniciada. Aguarde...")

nomes = get_names_sync()
print(nomes)
fim = perf_counter()
tempo = fim - inicio
print(f"Tempo de execução: {tempo:.2f} segundos.")


# Exemplo 2

async def get_country_name_async(session, code):
    async with session.get(f"{api_url}{code}") as response:
        json_data = await response.json()
        dados_json = json.dumps(json_data)
        dados_dict = json.loads(dados_json)[0]
        name = dados_dict['name']['common']
        return name
    
async def get_names_async() -> list:
    async with aiohttp.ClientSession() as session:
        codes = random.choices(codes2a, k=10)
        tasks = [get_country_name_async(session, code) for code in codes]
        countries = await asyncio.gather(*tasks)
        
        return countries
    
inicio = perf_counter()
print("Execução iniciada. Aguarde....")

nomes = asyncio.run(get_names_async())
print(nomes)
fim = perf_counter()
tempo = fim - inicio
print(f"Tempo de execução: {tempo:.2f} segundos.")