
# This is a program to calculate Indonesian Value Added Tax/VAT

# As of the time this program made, the VAT rate in Indonesia is 11%
PPN_Rate=0.11

# Greetings message
print("Selamat datang di kalkulator PPN Indonesia ")

# Input the DPP amount for calculation while implemented error handling mechanism
while True:
  try:
    DPP = float(input("Masukkan nilai DPP: "))
    PPN_amount = DPP * PPN_Rate
    break  # Successful conversion and calculation, exit the loop
  except ValueError:
    print("Nilai DPP yang anda masukkan belum sesuai, silahkan masukkan ulang nilai DPP")

# Format with commas and 2 decimals
formatted_DPP = "{:,.2f}".format(DPP)  
formatted_PPN = "{:,.2f}".format(PPN_amount)


print("Nilai PPN atas DPP", "Rp",formatted_DPP, "adalah:", "Rp", formatted_PPN)
