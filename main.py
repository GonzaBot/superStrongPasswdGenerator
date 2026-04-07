import secrets
import string
import tkinter as tk
from tkinter import messagebox

class PasswordFortressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Fortress - Día 1")
        self.root.geometry("450x500")
        self.root.configure(bg="#1e1e1e") # Fondo oscuro (estilo hacker)

        # --- Título ---
        self.lbl_titulo = tk.Label(root, text="PASSWORD FORTRESS", font=("Courier", 18, "bold"), fg="#00ff00", bg="#1e1e1e")
        self.lbl_titulo.pack(pady=20)

        # --- Entrada de Usuario ---
        self.lbl_instruccion = tk.Label(root, text="Ingresa una base (opcional):", fg="white", bg="#1e1e1e")
        self.lbl_instruccion.pack()
        
        self.entry_pw = tk.Entry(root, font=("Segoe UI", 12), width=30, justify='center', bg="#333", fg="white", insertbackground="white")
        self.entry_pw.pack(pady=10)

        # --- Botones ---
        self.btn_generar = tk.Button(root, text="GENERAR ALEATORIA", command=self.ui_generar, bg="#007acc", fg="white", width=25, relief="flat")
        self.btn_generar.pack(pady=5)

        self.btn_mejorar = tk.Button(root, text="MEJORAR MI BASE", command=self.ui_mejorar, bg="#28a745", fg="white", width=25, relief="flat")
        self.btn_mejorar.pack(pady=5)

        # --- Resultados ---
        self.lbl_res_titulo = tk.Label(root, text="Resultado:", fg="#00ff00", bg="#1e1e1e", font=("Arial", 10, "bold"))
        self.lbl_res_titulo.pack(pady=(20, 0))

        self.text_resultado = tk.Text(root, height=3, width=40, font=("Consolas", 11), bg="#2d2d2d", fg="#ffffff", padx=10, pady=10)
        self.text_resultado.pack(pady=10)

        self.lbl_seguridad = tk.Label(root, text="Seguridad: ---", fg="white", bg="#1e1e1e", font=("Arial", 9, "italic"))
        self.lbl_seguridad.pack()

        self.btn_copiar = tk.Button(root, text="Copiar al Portapapeles", command=self.copiar_portapapeles, bg="#444", fg="white")
        self.btn_copiar.pack(pady=15)

    # --- Lógica de Seguridad ---
    def calcular_seguridad(self, password):
        variedad = 0
        if any(c.islower() for c in password): variedad += 26
        if any(c.isupper() for c in password): variedad += 26
        if any(c.isdigit() for c in password): variedad += 10
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password): variedad += 32
        
        if len(password) == 0: return "Nula"
        
        combinaciones = (variedad or 1) ** len(password)
        if combinaciones < 10**10: return "🔴 Muy Débil"
        if combinaciones < 10**15: return "🟠 Débil"
        if combinaciones < 10**25: return "🟡 Moderada"
        return "🟢 Ultra Segura"

    def ui_generar(self):
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
        pw = ''.join(secrets.choice(caracteres) for _ in range(24))
        self.mostrar_resultado(pw)

    def ui_mejorar(self):
        base = self.entry_pw.get()
        if not base:
            messagebox.showwarning("Atención", "Escribe algo primero para mejorarlo.")
            return
        
        # Inyectamos entropía con secrets
        extra = string.ascii_uppercase + string.digits + "!@#$"
        mejorada = base + "-" + ''.join(secrets.choice(extra) for _ in range(8))
        self.mostrar_resultado(mejorada)

    def mostrar_resultado(self, pw):
        self.text_resultado.delete(1.0, tk.END)
        self.text_resultado.insert(tk.END, pw)
        seguridad = self.calcular_seguridad(pw)
        self.lbl_seguridad.config(text=f"Estado: {seguridad}")

    def copiar_portapapeles(self):
        pw = self.text_resultado.get(1.0, tk.END).strip()
        if pw:
            self.root.clipboard_clear()
            self.root.clipboard_append(pw)
            messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordFortressApp(root)
    root.mainloop()