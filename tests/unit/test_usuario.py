# test_usuario.py
# Edición realizada por Víctor Figueroa
# Pruebas unitarias para la clase Usuario, especialmente método actualizar_peso

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

import pytest
from src.usuario import Usuario

def test_actualizar_peso_correcto():
    # Crear instancia del usuario con peso inicial 70 kg
    usuario = Usuario("Victor", 70)
    
    # Actualizar el peso a 75 kg
    usuario.actualizar_peso(75)
    
    # Verificar que el peso se actualizó correctamente
    assert usuario.get_peso() == 75

def test_peso_no_cambia_si_actualizar_con_mismo_valor():
    usuario = Usuario("Victor", 70)
    usuario.actualizar_peso(70)
    assert usuario.get_peso() == 70

def test_actualizar_peso_varios_cambios():
    usuario = Usuario("Victor", 70)
    usuario.actualizar_peso(72)
    assert usuario.get_peso() == 72
    usuario.actualizar_peso(68)
    assert usuario.get_peso() == 68
