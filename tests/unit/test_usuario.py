# test_usuario.py
# Edición realizada por Víctor Figueroa
# Pruebas unitarias para verificar el correcto funcionamiento del método actualizar_peso

import sys
import os

# Ajuste para que Python pueda encontrar la carpeta src desde entornos CI/CD
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import pytest
from src.usuario import Usuario

def test_actualizar_peso_correcto():
    # Creo un usuario con peso inicial de 70 kg
    usuario = Usuario("Victor", 70)
    
    # Actualizo el peso a 75 kg
    usuario.actualizar_peso(75)
    
    # Verifico que el nuevo peso sea 75
    assert usuario.get_peso() == 75

def test_peso_no_cambia_si_actualizar_con_mismo_valor():
    # Compruebo que el peso no cambia si se actualiza con el mismo valor
    usuario = Usuario("Victor", 70)
    usuario.actualizar_peso(70)
    assert usuario.get_peso() == 70

def test_actualizar_peso_varios_cambios():
    # Realizo varias actualizaciones de peso y verifico que se registran correctamente
    usuario = Usuario("Victor", 70)
    usuario.actualizar_peso(72)
    assert usuario.get_peso() == 72
    usuario.actualizar_peso(68)
    assert usuario.get_peso() == 68

