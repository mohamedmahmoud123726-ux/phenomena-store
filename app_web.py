import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

# إعدادات الصفحة
st.set_page_config(page_title="Phenomena Luxury", page_icon="💎", layout="centered")

# تصميم الاستايل الفخم
st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    h1 { color: #d4af37; font-family: 'Times New Roman'; text-align: center; }
    .stButton>button { background-color: #d4af37; color: black; width: 100%; border-radius: 5px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("PHENOMENA")
st.write("<h4 style='text-align: center; color: #3776ab;'>POWERED BY PYTHON</h4>", unsafe_allow_html=True)

# بيانات العطور (تعديل الأسماء لتطابق ملفاتك المرفوعة فعلياً)
perfumes = {
    "Milky Way": {"price": "450", "img": "Milky Way.jpeg"},
    "Roma Aure": {"price": "450", "img": "Roma Aure.jpeg"},
    "Legacy": {"price": "450", "img": "Legacy.jpeg"},
    "R9 Elite": {"price": "550", "img": "R9.jpeg"}
}

selected = st.selectbox("اختر عطرك المفضل:", list(perfumes.keys()))

# عرض الصورة مباشرة
st.image(perfumes[selected]["img"], use_container_width=True)

st.write(f"### **السعر:** {perfumes[selected]['price']} EGP")

# خانات البيانات
name = st.text_input("الاسم الكامل")
phone = st.text_input("رقم الهاتف")

# رقم الواتساب بتاعك
my_whatsapp = "201100331533" 

if st.button("تأكيد الطلب عبر واتساب 💬"):
    if name and len(phone) >= 11:
        message = f"طلب جديد من Phenomena 💎\n\nالاسم: {name}\nالهاتف: {phone}\nالعطر: {selected}\nالسعر: {perfumes[selected]['price']} EGP"
        msg_encoded = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me/{my_whatsapp}?text={msg_encoded}"
        
        st.success("تم تسجيل طلبك! اضغط بالأسفل لفتح واتساب:")
        st.markdown(f'<a href="{whatsapp_url}" target="_blank" style="text-decoration:none;"><div style="text-align:center;background-color:#25D366;color:white;padding:10px;border-radius:5px;">إرسال الطلب الآن</div></a>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("برجاء إدخال بيانات صحيحة")
