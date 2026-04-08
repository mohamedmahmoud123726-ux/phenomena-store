import streamlit as st
import pandas as pd
from datetime import datetime
import os

# إعدادات الصفحة
st.set_page_config(page_title="Phenomena Luxury", page_icon="💎", layout="centered")

# تصميم الاستايل (CSS) عشان نخليه فخم
st.markdown("""
    <style>
    .main { background-color: #050505; }
    h1 { color: #d4af37; font-family: 'Times New Roman'; text-align: center; }
    .stButton>button { background-color: #d4af37; color: black; width: 100%; border-radius: 5px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("PHENOMENA")
st.write("---")

# بيانات العطور
perfumes = {
    "Milky Way": {"price": "450 EGP", "img": "perfume_images/Milky Way.jpeg"},
    "Roma Aure": {"price": "450 EGP", "img": "perfume_images/Roma Aure.jpeg"},
    "Legacy": {"price": "450 EGP", "img": "perfume_images/Legacy.jpeg"},
    "R9 Elite": {"price": "550 EGP", "img": "perfume_images/R9.jpeg"}
}

# اختيار العطر
selected = st.selectbox("اختر عطرك المفضل:", list(perfumes.keys()))

# عرض الصورة والسعر
col1, col2 = st.columns([1, 1])
with col1:
    if os.path.exists(perfumes[selected]["img"]):
        st.image(perfumes[selected]["img"], use_container_width=True)
with col2:
    st.subheader(selected)
    st.write(f"**Price:** {perfumes[selected]['price']}")
    st.write("**Size:** 50ml")

# خانات البيانات
st.write("---")
name = st.text_input("الاسم الكامل")
phone = st.text_input("رقم الهاتف")

if st.button("تأكيد الطلب الآن"):
    if name and len(phone) >= 11:
        # حفظ الطلب في ملف Excel عشان يفتح معاك أسهل
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_order = {"الوقت": now, "العميل": name, "الهاتف": phone, "العطر": selected}
        
        # كود بسيط لحفظ البيانات في ملف CSV (بيفتح بالإكسيل)
        df = pd.DataFrame([new_order])
        df.to_csv("orders.csv", mode='a', index=False, header=not os.path.exists("orders.csv"), encoding='utf-8-sig')
        
        st.success(f"شكراً يا {name}! تم استلام طلبك لـ {selected} وسنتواصل معك.")
        st.balloons()
    else:
        st.error("برجاء إدخال بيانات صحيحة")