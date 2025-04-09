from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import yaml
import os
class ActionCourseScheduleBasedOnYear(Action):
    def name(self) -> str:
        return "utter_course_schedule_based_on_year"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        year = tracker.get_slot("year")
        
        if year == "3":
            dispatcher.utter_message(text="Here is the course schedule for year 3.")
        elif year == "4":
            dispatcher.utter_message(text="Here is the course schedule for year 4.")
        elif year == "5":
            dispatcher.utter_message(text="Here is the course schedule for year 5.")
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find the course schedule for that year.")

        return []


# Action pour les examens
class ActionLireReglementationExamens(Action):
    def name(self):
        return "action_lire_reglementation_examens"

    def run(self, dispatcher, tracker, domain):
        chemin_fichier = os.path.join("data", "reglementations.yaml")
        with open(chemin_fichier, "r") as file:
            data = yaml.safe_load(file)

        examens = data["reglementations_isty"]["examens"]
        reponse = (
            f"Pour valider un module, la moyenne est de {examens['moyenne_validation']}/20. "
            f"Une note inférieure à {examens['note_eliminatoire']} est éliminatoire. "
            f"Les rattrapages sont autorisés ({examens['rattrapages']['autorisation']}) "
            f"durant la période : {examens['rattrapages']['periode']}."
        )

        dispatcher.utter_message(text=reponse)
        return []

# Action pour les règles intérieures
class ActionLireReglesInterieures(Action):
    def name(self):
        return "action_lire_regles_interieures"

    def run(self, dispatcher, tracker, domain):
        chemin_fichier = os.path.join("data", "rules.yaml")
        with open(chemin_fichier, "r") as file:
            data = yaml.safe_load(file)

        conduite = data["reglementations_isty"]["bonne_conduite"]
        reponse = (
            f"{conduite['interdiction_manger_salles']} "
            f"{conduite['gestion_dechets']} "
            f"{conduite['usage_telephone']} "
            f"{conduite['depart_salle']['mobilier']} "
            f"{conduite['depart_salle']['lumières']}"
        )

        dispatcher.utter_message(text=reponse)
        return []
class ActionDonnerHoraires(Action):
    def name(self):
        return "action_donner_horaires"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Les cours ont lieu du lundi au vendredi, de 8h30 à 17h30, avec une pause déjeuner entre 12h et 13h30.")
        return []

class ActionDonnerFraisInscription(Action):
    def name(self):
        return "action_donner_frais_inscription"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Les frais d’inscription s’élèvent à 614 euros par an.")
        return []

class ActionDonnerAidesFinancieres(Action):
    def name(self):
        return "action_donner_aides_financieres"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Des bourses sont disponibles via le CROUS, ainsi que des aides spécifiques pour les étudiants en difficulté. Renseignez-vous auprès du service scolarité.")
        return []

class ActionDonnerDiplome(Action):
    def name(self):
        return "action_donner_diplome"

    def run(self, dispatcher, tracker, domain):
        specialite = tracker.get_slot("specialite")
        if specialite:
            specialite = specialite.lower()
            valeurs = {
                "informatique": "Le diplôme en informatique est très recherché dans les entreprises du numérique et du développement logiciel.",
                "mecatronique": "La mécatronique est prisée dans les secteurs industriels, notamment en robotique et en automatisme.",
                "electronique": "Le diplôme en électronique est reconnu dans l’industrie, les télécommunications et les systèmes embarqués."
            }
            message = valeurs.get(specialite, "Le diplôme est reconnu dans plusieurs secteurs selon la spécialité.")
        else:
            message = "Le diplôme de l’ISTY est un diplôme d’ingénieur reconnu par l'État et les entreprises."

        dispatcher.utter_message(text=message)
        return []

class ActionDonnerSpecialites(Action):
    def name(self):
        return "action_donner_specialites"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="L’ISTY propose des formations en informatique, mécatronique et électronique.")
        return []