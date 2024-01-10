name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

print()


print("🌟Contact Card🌟")
print("Hi ",contact["name"],". Our dictionary says that you were born on ",contact["dob"],"we can call you on ", contact["tel"], "email", contact["email"]," or write to ",contact["address"],".")