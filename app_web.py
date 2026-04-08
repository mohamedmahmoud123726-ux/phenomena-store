import streamlit as st
import pandas as pd
from datetime import datetime
import os
import urllib.parse

# إعدادات الصفحة
st.set_page_config(page_title="Phenomena Luxury", page_icon="💎", layout="centered")

# تصميم الاستايل (CSS)
st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    h1 { color: #d4af37; font-family: 'Times New Roman'; text-align: center; font-size: 3em; }
    .stButton>button { background-color: #d4af37; color: black; width: 100%; border-radius: 5px; font-weight: bold; height: 3em; border: none; }
    .stTextInput label, .stSelectbox label { color: #d4af37 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("PHENOMENA")
st.write("<h4 style='text-align: center; color: #3776ab;'>POWERED BY PYTHON</h4>", unsafe_allow_html=True)
st.write("---")

# بيانات العطور بالصور الـ 3D
perfumes = {
    "Milky Way": {"price": "450", "img": "milky_3d.png"},
    "Roma Aure": {"price": "450", "img": "roma_3d.png"},
    "Legacy": {"price": "450", "img": "legacy_3d.png"},
    "R9 Elite": {"price": "550", "img": "r9_3d.png"}
}

selected = st.selectbox("اختر عطر الانفراد الحصري:", list(perfumes.keys()))

# عرض الصورة
if os.path.exists(perfumes[selected]["img"]):
    st.image(perfumes[selected]["img"], use_container_width=True)
else:
    st.info("📸 برجاء رفع الصور الـ 3D الجديدة على GitHub لتظهر هنا")

st.write(f"### **Price:** {perfumes[selected]['price']} EGP")
st.write("**Size:** 50ml | **Gender:** Unisex")

# خانات البيانات
st.write("---")
name = st.text_input("الاسم الكامل")
phone = st.text_input("رقم الهاتف")

# رقم الواتساب الخاص بك
my_whatsapp = "201100331533" 

if st.button("تأكيد الطلب عبر واتساب 💬"):
    if name and len(phone) >= 11:
        # تجهيز رسالة الواتساب
        message = f"طلب جديد من Phenomena 💎\n\nالاسم: {name}\nالهاتف: {phone}\nالعطر: {selected}\nالسعر: {perfumes[selected]['price']} EGP"
        msg_encoded = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me/{my_whatsapp}?text={msg_encoded}"
        
        # حفظ الطلب في ملف CSV
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        df = pd.DataFrame([{"الوقت": now, "العميل": name, "الهاتف": phone, "العطر": selected}])
        df.to_csv("orders.csv", mode='a', index=False, header=not os.path.exists("orders.csv"), encoding='utf-8-sig')
        
        st.success(f"شكراً يا {name}! اضغط على الزر بالأسفل لإرسال طلبك.")
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank">
                <div style="text-align: center; background-color: #25D366; color: white; padding: 10px; border-radius: 5px; font-weight: bold; text-decoration: none;">
                    إرسال الطلب الآن (فتح واتساب)
                </div>
            </a>
            ''', unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("برجاء إدخال الاسم ورقم هاتف صحيح")
