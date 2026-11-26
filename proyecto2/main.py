import tkinter as tk
from gui import Aplicacion


def main() -> None:
    # Crea la ventana principal y arranca el ciclo de eventos.
    raiz = tk.Tk()
    Aplicacion(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()