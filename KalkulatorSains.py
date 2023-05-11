#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import streamlit.components.v1 as components

st.sidebar.markdown("**Nama Kelompok**")
st.sidebar.markdown("**Bintang Fadillah**")
st.sidebar.markdown("**Daviq Panji**")
st.sidebar.markdown("**Diyah Astika**")
st.sidebar.markdown("**Nazwa Salsabilla**")
st.sidebar.markdown("**Yulia Oktaviyenti**")

st.sidebar.markdown("**REFERENCE USAGE**")
st.sidebar.markdown("**! Factorial, eg. 5! gives 120,( jadi () **")
st.sidebar.markdown("**% Percent, eg. 5% jadi 0.05, 10 + 50% jadi 15 **")
st.sidebar.markdown("**% Modulus (remainder), eg. 23 % 3 gives 2**")
st.sidebar.markdown("**sqrt jadi √, deg jadi °**")
st.sidebar.markdown("**pi jadi π, sum jadi Σ()**")
st.sidebar.markdown("**integrate jadi ∫(), tau jadi τ**")
st.sidebar.markdown("**phi jadi ϕ, floor jadi ⌊⌋**")
st.sidebar.markdown("**ceil jadi ⌈⌉, gamma jadi Γ**")
st.sidebar.markdown("**log Eg. log(1000, 10) sama dengan log10(1000)**")
st.sidebar.markdown("**root Eg. root(16, 3) sama dengan 3√16**")
st.sidebar.markdown("**integrate Eg. integrate(0, pi, sin(x) dx)**")
st.sidebar.markdown("**sum Eg. sum(1, 4, 2n)**")


st.title("Streamlit - Scientific Calculator")
components.iframe("https://kalker.strct.net/kalk", width=800, height=250)
st.markdown("__________________________________________________________________________________")

c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,buffer,c11,c12,=st.columns(13)

with c1:st.markdown("sin")
with c2:st.markdown("cos")
with c3:st.markdown("tan")
with c4:st.markdown("cot")
with c5:st.markdown("sec")
with c6:st.markdown("sinh")
with c7:st.markdown("cosh")
with c8:st.markdown("tanh")
with c9:st.markdown("coth")
with c10:st.markdown("cosech")
with c11:st.markdown("sech")
with c12:st.markdown("asin")

c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,buffer,c24 = st.columns(13)

with c13:st.markdown("asin")
with c14:st.markdown("acos")
with c15:st.markdown("atan")
with c16:st.markdown("acot")
with c17:st.markdown("acosec")
with c18:st.markdown("asec")
with c19:st.markdown("asinh")
with c20:st.markdown("acosh")
with c21:st.markdown("atanh")
with c22:st.markdown("acoth")
with c23:st.markdown("acosech")
with c24:st.markdown("asech")

c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38 = st.columns(14)

with c25:st.markdown("abs")
with c26:st.markdown("ceil")
with c27:st.markdown("floor")
with c28:st.markdown("frac")
with c29:st.markdown("round")
with c30:st.markdown("trunc")
with c31:st.markdown("sqrt")
with c32:st.markdown("cbrt")
with c33:st.markdown("exp")
with c34:st.markdown("log")
with c35:st.markdown("ln")
with c36:st.markdown("Re")
with c37:st.markdown("Im")
with c38:st.markdown("min")

c39,c40,c41,c42,c43,c44,c45,buffer,c46,c47,c48,c49,c50,c51,c52,c53,c54,c55 = st.columns(18)

with c39:st.markdown("abs")
with c40:st.markdown("max")
with c41:st.markdown("max")
with c42:st.markdown("!")
with c43:st.markdown("%")
with c44:st.markdown("pi")
with c45:st.markdown("integrate")
with c46:st.markdown("sum")
with c47:st.markdown("deg")
with c48:st.markdown("e")
with c49:st.markdown("tau")
with c50:st.markdown("phi")
with c51:st.markdown("+")
with c52:st.markdown("-")
with c53:st.markdown("*")
with c54:st.markdown("/")
with c55:st.markdown("(")

