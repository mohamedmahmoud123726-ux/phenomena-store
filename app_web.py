import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse
import os

# 1. Page Configuration
st.set_page_config(page_title="Phenomena Luxury", page_icon="💎", layout="centered")

# 2. Custom CSS for Luxury Light Mode & Professional Look
st.markdown("""
    <style>
    /* Main Background and Text Color */
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    
    /* Promotional Banner */
    .free-delivery { 
        text-align: center; 
        color: #155724; 
        background-color: #d4edda;
        font-weight: bold; 
        border: 1px solid #c3e6cb; 
        padding: 12px; 
        border-radius: 8px;
        margin: 20px 0;
    }

    /* Titles style in Gold */
    h1, h2, h3 { color: #d4af37; font-family: 'Times New Roman', serif; text-align: center; }

    /* Buttons Style */
    .stButton>button { 
        background-color: #d4af37; 
        color: white; 
        width: 100%; 
        border-radius: 8px; 
        font-weight: bold; 
        height: 3.5em; 
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        font-size: 1.1em;
    }
    .stButton>button:hover { background-color: #b8962e; color: #f0f0f0; }

    /* Inputs and Selectbox Style */
    .stTextInput label, .stSelectbox label { color: #d4af37 !important; font-weight: bold; font-size: 1.1em; }
    div[data-baseweb="input"] { background-color: #f8f9fa !important; border: 1px solid #d4af37 !important; border-radius: 8px; }
    
    /* Center Images */
    .stImage > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logo Section
# Display your custom logo (Ensure logo.png is uploaded to GitHub)
if os.path.exists("logo.png"):
    st.image("logo.png", width=300) # عرض اللوجو الجديد بشكل مناسب
else:
    st.write("<h1 style='text-align:center;'>PHENOMENA</h1>", unsafe_allow_html=True)

# Powered by Python (أضفت تنسيق ذهبي بسيط لها)
st.write("<p style='text-align: center; color: #b8962e; font-family: Courier New, monospace; font-size: 1.1em; margin-top: -10px;'>POWERED BY PYTHON</p>", unsafe_allow_html=True)
st.write("---")

# 4. Special Offer
st.write("<div class='free-delivery'>🔥 Special Offer: FREE DELIVERY for your first order! 🔥</div>", unsafe_allow_html=True)

# 5. Product Data
perfumes = {
    "Milky Way": {"price": "450", "img": "Milky Way.jpeg"},
    "Roma Aure": {"price": "450", "img": "Roma Aure.jpeg"},
    "Legacy": {"price": "450", "img": "Legacy.jpeg"},
    "R9 Elite": {"price": "550", "img": "R9.jpeg"}
}

selected = st.selectbox("Select Your Exclusive Fragrance:", list(perfumes.keys()))

# 6. Display Product Image (Controlled Width)
st.image(perfumes[selected]["img"], width=350, use_container_width=False) # تم إضافة use_container_width=False للتحكم في الحجم بشكل أدق

# 7. Pricing and Info
st.markdown(f"<h2>{perfumes[selected]['price']} EGP</h2>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #666;'>Size: 50ml | Concentration: Eau de Parfum | Unisex</p>", unsafe_allow_html=True)

# 8. Shipping Form
st.write("---")
st.write("<h3>Shipping Details</h3>", unsafe_allow_html=True)

full_name = st.text_input("Full Name")
phone_number = st.text_input("WhatsApp Number")
address = st.text_input("Detailed Delivery Address")

# Your WhatsApp Business Number
my_whatsapp = "201100331533" 

# 9. WhatsApp Order Logic
if st.button("Confirm Order via WhatsApp 💬"):
    if full_name and len(phone_number) >= 11 and address:
        message = (f"New Order from Phenomena Website 💎\n\n"
                   f"👤 Customer: {full_name}\n"
                   f"📱 Phone: {phone_number}\n"
                   f"📍 Address: {address}\n"
                   f"✨ Product: {selected}\n"
                   f"💰 Price: {perfumes[selected]['price']} EGP\n"
                   f"🚚 Shipping: FREE (First Order)")
        
        msg_encoded = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me/{my_whatsapp}?text={msg_encoded}"
        
        # Save to local CSV for backup (إضافة os للتحقق من وجود الملف)
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        df = pd.DataFrame([{"Time": now, "Name": full_name, "Phone": phone_number, "Address": address, "Product": selected}])
        df.to_csv("orders.csv", mode='a', index=False, header=not os.path.exists("orders.csv"), encoding='utf-8-sig')
        
        st.success(f"Almost there, {full_name}! Click the green button to finish.")
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
                <div style="text-align:center;background-color:#25D366;color:white;padding:15px;border-radius:10px;font-weight:bold;font-size:1.2em;">
                    SEND VIA WHATSAPP NOW
                </div>
            </a>
            ''', unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("Please fill in all details (Name, Phone, and Address).")
