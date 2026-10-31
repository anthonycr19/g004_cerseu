"""Uso de la librería JSON"""
import json

json_data = '{"nombre": "Python", "tipo": "Backend", "paradigma": "POO"}'
print(json_data)

json_to_python = json.loads(json_data)
print(json_to_python)
print(type(json_to_python))
