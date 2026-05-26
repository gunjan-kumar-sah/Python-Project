import qrcode

# ---- UPI Payment Details ----
upi_id = "7079503713@ybl"   # Replace this with your actual UPI ID
name = "Vishal Raj"          # Receiver's name
note = "Thanks for payment"  # Payment note

# ---- UPI URI WITHOUT Amount ----
upi_link = f"upi://pay?pa={upi_id}&pn={name}&cu=INR&tn={note}"
         
# ---- Generate QR Code ----
qr = qrcode.make(upi_link)

# ---- Save and Show QR ----
qr.save("upi_qr_no_amount.png")
qr.show()

print("✅ QR code saved as 'upi_qr_no_amount.png'")  