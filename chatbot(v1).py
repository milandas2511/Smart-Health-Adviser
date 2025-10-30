print("=== Smart Health Adviser ===")
print("Select your main symptoms by number (comma separated):")
print("1. Fever")
print("2. Cough")
print("3. Cold")
print("4. Headache")
print("5. Rash")
print("6. Sneezing")
print("7. Breathing problem")
print("8. Body pain")
print("9. Chills")
print("10. Itching / Allergy")
print("-------------------------------------------------------------------")
symptom_numbers = input("Enter your symptom numbers (comma separated): ").strip()
symptom_map = {
    "1": "fever",
    "2": "cough",
    "3": "cold",
    "4": "headache",
    "5": "rash",
    "6": "sneeze",
    "7": "breath",
    "8": "body pain",
    "9": "chills",
    "10": "itch"
}
symptoms = [symptom_map.get(num.strip()) for num in symptom_numbers.split(",") if num.strip() in symptom_map]
print("\n--- Health Advice ---")
# Cold
if "cold" in symptoms or "sneeze" in symptoms:
    print("\nYou might have a Common Cold.")
    print("Advice:")
    print("- Drink warm water and rest well.")
    print("- Take steam inhalation to relieve congestion.")
    print("- Avoid cold food and drinks.")
    print("- If symptoms last more than 3 days, consult a doctor.")

# Flu
elif "fever" in symptoms and "body pain" in symptoms:
    print("\nYou might have Flu.")
    print("Advice:")
    print("- Take plenty of fluids and rest.")
    print("- Eat food rich in vitamin C (like oranges).")
    print("- Use mild pain relievers if needed.")
    print("- Consult a doctor if fever is high or persistent.")

# Cough or throat infection
elif "cough" in symptoms and "headache" in symptoms or "dry cough" in symptoms:
    print("\nYou might have Cough or Throat Infection.")
    print("Advice:")
    print("- Drink warm water and honey-lemon tea.")
    print("- Avoid dust, smoke, and cold drinks.")
    print("- Gargle with warm salt water.")
    print("- Visit a doctor if it lasts more than a week.")

# Dengue
elif "fever" in symptoms and "rash" in symptoms:
    print("\nYou might have Dengue Fever.")
    print("Advice:")
    print("- Drink plenty of fluids and take rest.")
    print("- Drink papaya leaf juice to improve platelet count.")
    print("- Avoid aspirin or ibuprofen.")
    print("- See a doctor immediately if rashes or fever worsen.")

# Malaria
elif "fever" in symptoms and "chills" in symptoms:
    print("\nYou might have Malaria.")
    print("Advice:")
    print("- Take antimalarial medicine as prescribed.")
    print("- Sleep under mosquito nets and prevent mosquito bites.")
    print("- Keep surroundings clean and free from stagnant water.")
    print("- Visit a doctor immediately.")

# COVID-19
elif "cough" in symptoms and "breath" in symptoms:
    print("\nYou might have COVID-19 or a respiratory infection.")
    print("Advice:")
    print("- Isolate yourself and wear a mask.")
    print("- Monitor oxygen levels and temperature.")
    print("- Stay hydrated and rest.")
    print("- Seek medical help if breathing difficulty increases.")

# Allergy
elif "itch" in symptoms or "sneeze" in symptoms:
    print("\nYou might have an Allergy.")
    print("Advice:")
    print("- Avoid known triggers (dust, pollen, pets, etc.).")
    print("- Keep your room clean and dust-free.")
    print("- Take antihistamines if prescribed.")
    print("- Visit a doctor if symptoms persist.")
else:
    print("\nUnable to identify disease from given symptoms.")
    print("Please consult a doctor for proper diagnosis.")

print("\nStay Healthy! 💪")
