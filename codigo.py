import tkinter as tk
from tkinter import messagebox
import random

# --------------------------
# CLASE BASE
# --------------------------
class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self._vida = vida
        self._ataque = ataque
        self._defensa = defensa

    def get_vida(self):
        return self._vida

    def set_vida(self, nueva_vida):
        self._vida = max(0, min(100, nueva_vida))

    def get_ataque(self):
        return self._ataque

    def get_defensa(self):
        return self._defensa

    def atacar(self, objetivo):
        pass


# --------------------------
# CLASES HIJAS
# --------------------------
class Guerrero(Personaje):
    def atacar(self, objetivo):
        daño = int(self.get_ataque() * 1.2 - objetivo.get_defensa())
        daño = max(0, daño)
        objetivo.set_vida(objetivo.get_vida() - daño)
        return f"{self.nombre} ataca con FUERZA (+20%) a {objetivo.nombre}, causando {daño} de daño."


class Mago(Personaje):
    def atacar(self, objetivo):
        daño = self.get_ataque()
        objetivo.set_vida(objetivo.get_vida() - daño)
        return f"{self.nombre} lanza un HECHIZO a {objetivo.nombre}, causando {daño} de daño (ignora defensa)."


class Arquero(Personaje):
    def atacar(self, objetivo):
        if self.get_ataque() > objetivo.get_defensa():
            daño = (self.get_ataque() - objetivo.get_defensa()) * 2
        else:
            daño = self.get_ataque() - objetivo.get_defensa()
        daño = max(0, daño)
        objetivo.set_vida(objetivo.get_vida() - daño)
        return f"{self.nombre} dispara a {objetivo.nombre}, causando {daño} de daño."


# --------------------------
# INTERFAZ CON TKINTER
# --------------------------
class Juego:
    def __init__(self, master):
        self.master = master
        self.master.title("Guardians of the Ancient Kingdom")

        self.personajes = [
            Guerrero("GUERRERO", 100, 30, 20),
            Mago("MAGO", 80, 40, 10),
            Arquero("ARQUERO", 90, 35, 15)
        ]

        self.turno = 0

        self.texto = tk.Text(master, height=20, width=70)
        self.texto.pack()

        self.boton_ataque = tk.Button(master, text="¡Siguiente Turno!", command=self.turno_ataque)
        self.boton_ataque.pack(pady=10)

        self.actualizar_estado("¡Batalla entre 3 personajes ha comenzado!")

    def actualizar_estado(self, mensaje_extra=""):
        self.texto.delete("1.0", tk.END)
        estado = ""
        for p in self.personajes:
            estado += f"{p.nombre}: {p.get_vida()} vida\n"
        estado += "\n" + mensaje_extra
        self.texto.insert(tk.END, estado)

    def turno_ataque(self):
        vivos = [p for p in self.personajes if p.get_vida() > 0]
        if len(vivos) == 1:
            messagebox.showinfo("Fin del juego", f"¡{vivos[0].nombre} ha ganado!")
            self.boton_ataque.config(state=tk.DISABLED)
            return

        atacante = self.personajes[self.turno % len(self.personajes)]
        if atacante.get_vida() <= 0:
            self.turno += 1
            self.turno_ataque()
            return

        posibles_objetivos = [p for p in self.personajes if p != atacante and p.get_vida() > 0]
        objetivo = random.choice(posibles_objetivos)

        resultado = atacante.atacar(objetivo)
        self.turno += 1
        self.actualizar_estado(resultado)


# --------------------------
# EJECUCIÓN DEL JUEGO
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    juego = Juego(root)
    root.mainloop()
