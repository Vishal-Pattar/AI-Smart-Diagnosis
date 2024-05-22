class SuggestionFactory:
    def __init__(self):
        self.suggestion_classes = {
            "Brain Tumor": BrainSuggestion,
            "Tuberculosis": TuberculosisSuggestion,
            "Kidney Disease": KidneySuggestion,
            "Lungs Disease": LungsSuggestion,
        }

    def get_suggestion(self, disease, dis_name):
        suggestion_class = self.suggestion_classes.get(disease)
        if suggestion_class:
            suggestion_obj = suggestion_class(dis_name)
            return suggestion_obj.generate()
        return "No suggestion available."

class Suggestion:
    def __init__(self, dis_name, disease_info):
        self.dis_name = dis_name
        self.disease_info = disease_info

    def generate(self):
        if self.dis_name not in ["Normal", "None"]:
            header = f"The following CT-Scan Image has been identified as {self.dis_name}\n\n"

            symptoms_section = "**Symptoms:**\n"
            symptoms_list = "".join([f"\t\n\n • \t\t {symptom}\n" for symptom in self.disease_info["symptoms"]])

            medication_section = "\n**Suggested Medication:**\n"
            medication_list = "".join([f"\t\n\n • \t\t {medication}\n" for medication in self.disease_info["medications"]])

            precautions_section = "\n**Precautions:**\n"
            precautions_list = "".join([f"\t\n\n • \t\t {precaution}\n" for precaution in self.disease_info["precautions"]])

            suggestion = (
                header + 
                symptoms_section + symptoms_list +
                medication_section + medication_list +
                precautions_section + precautions_list
            )
        elif self.dis_name == "Normal":
            suggestion = f"The following CT-Scan Image seems to be {self.dis_name}"
        else:
            suggestion = "The following CT-Scan Image was not able to classify in any of the related diseases"

        return suggestion


class KidneySuggestion(Suggestion):
    def __init__(self, dis_name):
        disease_info = {
            "symptoms": ["Fatigue and weakness", "Swelling of feet and ankles", "High blood pressure", "Nausea and vomiting", 
                         "Changes in urine frequency, color and in some cases blood in urine", "Muscle cramps or twitches"],
            "medications": ["Medications to control high blood pressure", "Fluid management", "Dietary and lifestyle changes", 
                            "Dialysis", "Kidney transplant"],
            "precautions": ["Monitoring blood pressure", "Managing blood sugar level", "Avoiding nephrotoxic substances", 
                            "Hygiene and infection prevention", "Following a renal-friendly diet"]
        }
        super().__init__(dis_name, disease_info)

class BrainSuggestion(Suggestion):
    def __init__(self, dis_name):
        disease_info = {
            "symptoms": ["Headaches", "Cognitive or neurological changes", "Behavioral or mood changes", "Nausea and vomiting", 
                         "Fatigue and weakness"],
            "medications": ["Surgery", "Radiation therapy", "Chemotherapy", "Targeted therapy", "Corticosteroids"],
            "precautions": ["Regular check-ups", "Practice healthy lifestyle habits", "Avoid exposure to harmful substances", 
                            "Follow prescribed treatment plan", "Seek medical attention for concerning symptoms"]
        }
        super().__init__(dis_name, disease_info)

class LungsSuggestion(Suggestion):
    def __init__(self, dis_name):
        disease_info = {
            "symptoms": ["Persistent cough", "Shortness of breath", "Fatigue and chest pain", "Respiratory infections", 
                         "Changes in sputum or coughing up blood", "Chest tightness or discomfort", "Changes in voice"],
            "medications": ["Medications to manage symptoms", "Oxygen therapy", "Pulmonary rehabilitation", "Immunizations", 
                            "Targeted therapies"],
            "precautions": ["Avoiding smoking and exposure to smoke", "Reducing exposure to air pollutants", 
                            "Following prescribed treatment plans", "Monitoring symptoms", "Avoiding respiratory infections"]
        }
        super().__init__(dis_name, disease_info)

class TuberculosisSuggestion(Suggestion):
    def __init__(self, dis_name):
        disease_info = {
            "symptoms": ["Persistent cough", "Chest pain", "Fatigue", "Weight loss", "Fever and chills", "Breathlessness"],
            "medications": ["Isoniazid", "Rifampin", "Pyrazinamide", "Ethambutol", "Streptomycin"],
            "precautions": ["Take medications as prescribed", "Follow infection control measure", "Avoid close contact with others", 
                            "Practice good hygiene", "Stay informed", "Get screened"]
        }
        super().__init__(dis_name, disease_info)