import os
import streamlit as st
import time
import serial
import random


def data_nivel():
    arduino = serial.Serial('COM7', 9600)
    linha = str(arduino.readline())
    a = linha[2:-9]
    b = a.replace('.00', '')
    arduino.close()
    return b



def data_volume():
    arduino = serial.Serial('COM7', 9600)
    linha = str(arduino.readline())
    c = linha[4:-5]
    return c

st.title("LMS")

# Crie espaços vazios para dados
data_placeholder = st.empty()
volume_placeholder = st.empty()

while True:
    nivel = data_nivel()
    volume = data_volume()

    # Atualize os espaços vazios com os novos valores
    data_placeholder.text("Nivel da Água: {}%".format(nivel))
    volume_placeholder.text("Volume da Água: {}L".format(volume))

    # Espera por um curto período antes de atualizar novamente
    time.sleep(1)
