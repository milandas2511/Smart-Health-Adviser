print("=== Smart Health Adviser ===")
print("Common symptoms: fever, cough, cold, headache, rash, sneezing, breathing problem, body pain, chills")
print("-------------------------------------------------------------------")

symptoms = input("Enter your main symptoms (comma separated): ").strip().lower()

print("\n--- Health Advice ---")

# Cold
if "cold" in symptoms or "sneeze" in symptoms:
    print("\n☃ You might have a Common Cold.")
    print("Advice:")
    print("- Drink warm water and rest well.")
    print("- Take steam inhalation to relieve congestion.")
    print("- Avoid cold food and drinks.")
    print("- If symptoms last more than 3 days, consult a doctor.")

# Flu
elif "fever" in symptoms and "body pain" in symptoms:
    print("\n🤒 You might have Flu.")
    print("Advice:")
    print("- Take plenty of fluids and rest.")
    print("- Eat food rich in vitamin C (like oranges).")
    print("- Use mild pain relievers if needed.")
    print("- Consult a doctor if fever is high or persistent.")

# Cough
elif "cough" in symptoms and "throat" in symptoms or "dry cough" in symptoms:
    print("\n😷 You might have Cough or Throat Infection.")
    print("Advice:")
    print("- Drink warm water and honey-lemon tea.")
    print("- Avoid dust, smoke, and cold drinks.")
    print("- Gargle with warm salt water.")
    print("- Visit a doctor if it lasts more than a week.")

# Dengue
elif "fever" in symptoms and "rash" in symptoms:
    print("\n🦟 You might have Dengue Fever.")
    print("Advice:")
    print("- Drink plenty of fluids and take rest.")
    print("- Drink papaya leaf juice to improve platelet count.")
    print("- Avoid aspirin or ibuprofen.")
    print("- See a doctor immediately if rashes or fever worsen.")

# Malaria
elif "fever" in symptoms and "chills" in symptoms:
    print("\n🌿 You might have Malaria.")
    print("Advice:")
    print("- Take antimalarial medicine as prescribed.")
    print("- Sleep under mosquito nets and prevent mosquito bites.")
    print("- Keep surroundings clean and free from stagnant water.")
    print("- Visit a doctor immediately.")

# COVID-19
elif "cough" in symptoms and "breath" in symptoms:
    print("\n🫁 You might have COVID-19 or a respiratory infection.")
    print("Advice:")
    print("- Isolate yourself and wear a mask.")
    print("- Monitor oxygen levels and temperature.")
    print("- Stay hydrated and rest.")
    print("- Seek medical help if breathing difficulty increases.")

# Allergy
elif "itch" in symptoms or "sneeze" in symptoms:
    print("\n🤧 You might have an Allergy.")
    print("Advice:")
    print("- Avoid known triggers (dust, pollen, pets, etc.).")
    print("- Keep your room clean and dust-free.")
    print("- Take antihistamines if prescribed.")
    print("- Visit a doctor if symptoms persist.")
else:
    print("\n❌ Unable to identify disease from given symptoms.")
    print("Please consult a doctor for proper diagnosis.")

print("\nStay Healthy! 💪")
