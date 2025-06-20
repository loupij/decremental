import tkinter as tk
from tkinter import messagebox

NOMBRE = 1e13

class Jeu:
    def __init__(self):
        self.racine = tk.Tk()
        self.racine.title("Decremental")

        self.nombre = NOMBRE
        self.argent = 0
        self.vitesse = 1  # décrément de base : -1/s
        self.prix = self.get_prix()
        self.progression = 0

        self.stats = {
            "Décrémenté" : 0,
            "Upgrades" : 0,
            "Argent dépensé" : 0,

        }

        self.label = tk.Label(self.racine, text=str(self.nombre), font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.progression_label = tk.Label(self.racine, text=f"{self.progression}%", font=("Helvetica", 16))
        self.progression_label.pack(pady=0)

        self.vitesse_label = tk.Label(self.racine, text=f"Vitesse : {self.vitesse}/sec", font=("Helvetica", 16))
        self.vitesse_label.pack(pady=5)

        self.argent_label = tk.Label(self.racine, text=f"Argent : {self.argent}", font=("Helvatica", 16))
        self.argent_label.pack(pady=10)

        self.prix_label = tk.Label(self.racine, text=f"Prix : {self.prix}", font=("Helvatica", 16))
        self.prix_label.pack(pady=1)

        self.bouton_upgrade_vitesse = tk.Button(self.racine, text="Augmenter la vitesse", font=("Helvetica", 16), command=self.augmenter_vitesse)
        self.bouton_upgrade_vitesse.pack(pady=20)

        self.bouton_afficher_stats = tk.Button(self.racine, text="Afficher les stats", font=("Helvatica", 16), command=self.show_stats)
        self.bouton_afficher_stats.pack(pady=25)

        self.update_values()

        self.racine.mainloop()

    def update_values(self):
        self.nombre -= self.vitesse
        self.argent += self.vitesse
        
        self.stats["Décrémenté"] += self.vitesse
        
        self.update_display()
        self.racine.after(1000, self.update_values)

    def augmenter_vitesse(self):
        if self.argent > self.prix:
            self.vitesse += 1
            self.argent -= self.prix

            self.stats["Upgrades"] += 1
            self.stats["Argent dépensé"] += self.prix

            self.prix = self.get_prix()
            self.update_display()

    def get_prix(self):
        return self.vitesse**1.1+1
    
    def get_progression(self):
        return self.stats["Décrémenté"] / NOMBRE * 100
    
    def update_display(self):
        self.label.config(text=int(self.nombre))
        self.progression_label.config(text=f"{round(self.get_progression(), 5)}%")
        self.vitesse_label.config(text=f"Vitesse : {int(self.vitesse)}/sec")
        self.prix_label.config(text=f"Prix : {round(self.prix, 3)}")
        self.argent_label.config(text=f"Argent : {int(self.argent)}")

    def show_stats(self):
        texte = f"""
        Décrémenté : {self.stats["Décrémenté"]}
        Progression : {round(self.get_progression(), 10)}%
        Upgrades : {self.stats["Upgrades"]}
        Argent dépensé : {round(self.stats["Argent dépensé"], 3)}
        """
        messagebox.showinfo("Statistiques", texte)

Jeu()
