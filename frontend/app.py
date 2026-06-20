import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from gra_chiral_null import mirror_operator_nd, chiral_pair, gra_null_as_chiral

st.title("GRA Chiral Nullification Explorer")

dim = st.sidebar.slider("Размерность", 2, 5, 3)
axis = st.sidebar.number_input("Ось отражения", 0, dim-1, dim-1)

Z = mirror_operator_nd(axis)

x = np.random.randn(dim)
x_input = st.text_input("Вектор (через запятую)", ",".join(map(str, x)))
x = np.array([float(v) for v in x_input.split(",")])

R, L = chiral_pair(x, Z)
st.write("Правая (R):", R)
st.write("Левая (L):", L)

if st.button("GRA-обнулёнка"):
    result = gra_null_as_chiral(x, {"w":1.0}, {"state":0}, Z)
    st.success(f"Результат: политика = {result.policy}, веса = {result.weights}")

# Визуализация для 2D/3D
if dim == 2:
    fig, ax = plt.subplots()
    ax.quiver(0,0, R[0], R[1], angles='xy', scale_units='xy', scale=1, color='r', label='R')
    ax.quiver(0,0, L[0], L[1], angles='xy', scale_units='xy', scale=1, color='b', label='L')
    ax.legend()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    st.pyplot(fig)
