import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse
import os

# Page Settings
st.set_page_config(page_title="Phenomena Luxury", page_icon="💎", layout="centered")

# Custom CSS for Luxury Look
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    h1 { color: #d4af37; font-family: 'Times New Roman'; text-align: center; font-size: 3.5em; margin-bottom: 0px; }
    .powered { text-align: center; color: #3776ab; font-family: 'Courier New'; font-size: 1.1em; margin-top: -10px; }
    .free-delivery { 
        text-align: center; 
        color: #00ff00; 
        font-weight: bold; 
        border: 1px dashed #00ff00; 
        padding: 10px; 
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .stButton>button { 
        background-color: #d4af37; 
        color: black; 
        width: 100%; 
        border-radius: 8px; 
        font-weight: bold; 
        height: 3.5em; 
        border: none;
    }
    .stTextInput label, .stSelectbox label { color: #d4af37 !important; font-weight: bold; }
    
    /* Control Image Size */
    .stImage > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-width: 350px; 
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.write("<h1>PHENOMENA</h1>", unsafe_allow_html=True)
st.write("<p class='powered'>POWERED BY PYTHON</p>", unsafe_allow_html=True)
st.write("---")

# Free Delivery Promo
st.write("<div class='free-delivery'>🔥 Special Offer: FREE DELIVERY for your first order! 🔥</div>", unsafe_allow_html=True)

# Perfume Data
perfumes = {
    "Milky Way": {"price": "450", "img": "Milky Way.jpeg"},
    "Roma Aure": {"price": "450", "img": "Roma Aure.jpeg"},
    "Legacy": {"price": "450", "img": "Legacy.jpeg"},
    "R9 Elite": {"price": "550", "img": "R9.jpeg"}
}

selected = st.selectbox("Select Your Fragrance:", list(perfumes.keys()))

# Display Image
st.image(perfumes[selected]["img"])

# Price Display
st.markdown(f"<h2 style='text-align: center; color: #d4af37;'>{perfumes[selected]['price']} EGP</h2>", unsafe_allow_html=True)
st.write("<p style='text-align: center; opacity: 0.8;'>Size: 50ml | Concentration: Eau de Parfum</p>", unsafe_allow_html=True)

# Order Form
st.write("---")
st.write("<h3 style='text-align: center; color: #d4af37;'>Shipping Details</h3>", unsafe_allow_html=True)

full_name = st.text_input("Full Name")
phone_number = st.text_input("Phone Number (WhatsApp)")
address = st.text_input("Detailed Address")

# Your WhatsApp Number
my_whatsapp = "201100331533" 

if st.button("Confirm Order via WhatsApp 💬"):
    if full_name and len(phone_number) >= 11 and address:
        # WhatsApp Message Construction
        message = (f"New Order from Phenomena 💎\n\n"
                   f"👤 Customer: {full_name}\n"
                   f"📱 Phone: {phone_number}\n"
                   f"📍 Address: {address}\n"
                   f"✨ Fragrance: {selected}\n"
                   f"💰 Price: {perfumes[selected]['price']} EGP\n"
                   f"🚚 Shipping: FREE (First Order Promo)")
        
        msg_encoded = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me/{my_whatsapp}?text={msg_encoded}"
        
        # Save to CSV
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        df = pd.DataFrame([{"Time": now, "Name": full_name, "Phone": phone_number, "Address": address, "Product": selected}])
        df.to_csv("orders.csv", mode='a', index=False, header=not os.path.exists("orders.csv"), encoding='utf-8-sig')
        
        st.success(f"Thank you, {full_name}! Please click the button below to send your order.")
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
                <div style="text-align:center;background-color:#25D366;color:white;padding:15px;border-radius:10px;font-weight:bold;font-size:1.2em;">
                    SEND ORDER NOW (Open WhatsApp)
                </div>
            </a>
            ''', unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("Please fill in all fields correctly (Name, Phone, and Address).")
