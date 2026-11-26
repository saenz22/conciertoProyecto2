import sys
import tkinter as tk
from tkinter import messagebox, ttk

from entrada import ErrorEntrada, parsear_entrada
from generador import cargar_plantilla, generar_minizinc
from tema import (
    ACENTO,
    BORDES,
    CODIGO_FONDO,
    CODIGO_TEXTO,
    ERROR,
    EXITO,
    FONDO,
    PRIMARIO,
    PRIMARIO_OSCURO,
    TARJETA,
    TEXTO,
    TEXTO_SECUNDARIO,
)
from validacion import validar


class Aplicacion:
    # Interfaz para interpretar una entrada y generar su modelo MiniZinc.

    def __init__(self, raiz: tk.Tk):
        # Configura la ventana principal y enlaza Ctrl+Enter.
        #
        # Entrada: raiz, la ventana Tk que contiene la aplicación.
        self.raiz = raiz
        self.raiz.title("Ubicador de concierto")
        self.raiz.geometry("1000x640")
        self.raiz.minsize(800, 520)
        self.raiz.configure(bg=FONDO)
        self._configurar_estilos()
        self.construir_widgets()
        self.raiz.bind("<Control-Return>", self._atajo_solucionar)

    def _configurar_estilos(self) -> None:
        # Configura el tema ttk y los estilos de los controles de la aplicación.
        estilo = ttk.Style(self.raiz)
        estilo.theme_use("clam")
        estilo.configure("App.TFrame", background=FONDO)
        estilo.configure(
            "Header.TLabel",
            background=FONDO,
            foreground=PRIMARIO,
            font=("Segoe UI", 19, "bold"),
        )
        estilo.configure(
            "Panel.TLabel",
            background=TARJETA,
            foreground=TEXTO_SECUNDARIO,
            font=("Segoe UI", 9, "bold"),
        )
        estilo.configure(
            "Primario.TButton",
            background=PRIMARIO,
            foreground="white",
            padding=(18, 10),
            borderwidth=0,
            font=("Segoe UI", 10, "bold"),
        )
        estilo.map(
            "Primario.TButton",
            background=[("active", PRIMARIO_OSCURO), ("disabled", BORDES)],
            foreground=[("disabled", TEXTO_SECUNDARIO)],
        )
        estilo.configure(
            "Secundario.TButton",
            background=TARJETA,
            foreground=PRIMARIO,
            padding=(14, 9),
            borderwidth=1,
            relief="solid",
            font=("Segoe UI", 10),
        )
        estilo.map(
            "Secundario.TButton",
            background=[("active", FONDO)],
            foreground=[("active", PRIMARIO_OSCURO)],
        )
        estilo.configure(
            "Treeview",
            background=TARJETA,
            fieldbackground=TARJETA,
            foreground=TEXTO,
            rowheight=27,
            font=("Segoe UI", 10),
        )
        estilo.map(
            "Treeview",
            background=[("selected", ACENTO)],
            foreground=[("selected", "white")],
        )
        estilo.configure(
            "Treeview.Heading",
            background=FONDO,
            foreground=TEXTO,
            font=("Segoe UI", 9, "bold"),
        )
        estilo.map(
            "Treeview.Heading",
            background=[("active", BORDES)],
        )
        estilo.configure(
            "Estado.TLabel",
            background=FONDO,
            foreground=TEXTO_SECUNDARIO,
            font=("Segoe UI", 9),
        )

    def construir_widgets(self) -> None:
        # Crea y distribuye los paneles, campos, botones y etiquetas de la ventana.
        contenedor = ttk.Frame(self.raiz, style="App.TFrame", padding=18)
        contenedor.grid(row=0, column=0, sticky="nsew")
        contenedor.columnconfigure(0, weight=1)
        contenedor.rowconfigure(1, weight=1)

        encabezado = ttk.Label(
            contenedor,
            text="🎤  Ubicador de concierto",
            style="Header.TLabel",
        )
        encabezado.grid(row=0, column=0, sticky="w", pady=(0, 16))

        cuerpo = ttk.Frame(contenedor, style="App.TFrame")
        cuerpo.grid(row=1, column=0, sticky="nsew")
        cuerpo.columnconfigure(0, weight=1, uniform="panel")
        cuerpo.columnconfigure(1, weight=1, uniform="panel")
        cuerpo.rowconfigure(0, weight=1)

        panel_izquierdo = ttk.Frame(cuerpo, style="App.TFrame")
        panel_izquierdo.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        panel_izquierdo.columnconfigure(0, weight=1)
        panel_izquierdo.rowconfigure(0, weight=3)
        panel_izquierdo.rowconfigure(1, weight=2)

        tarjeta_entrada = self._crear_tarjeta(panel_izquierdo)
        tarjeta_entrada.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
        tarjeta_entrada.columnconfigure(0, weight=1)
        tarjeta_entrada.rowconfigure(1, weight=1)
        ttk.Label(
            tarjeta_entrada,
            text="ENTRADA",
            style="Panel.TLabel",
        ).grid(row=0, column=0, sticky="w", padx=14, pady=(12, 8))

        entrada_contenido = ttk.Frame(tarjeta_entrada, style="App.TFrame")
        entrada_contenido.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 12))
        entrada_contenido.columnconfigure(0, weight=1)
        entrada_contenido.rowconfigure(0, weight=1)
        entrada_contenido.columnconfigure(1, weight=0)
        self.entrada = tk.Text(
            entrada_contenido,
            height=8,
            wrap="none",
            relief="flat",
            bd=0,
            padx=12,
            pady=10,
            font=self._fuente_mono(),
            bg=TARJETA,
            fg=TEXTO,
            insertbackground=TEXTO,
            undo=True,
        )
        self.entrada.grid(row=0, column=0, sticky="nsew")
        entrada_scroll = ttk.Scrollbar(
            entrada_contenido,
            orient="vertical",
            command=self.entrada.yview,
        )
        entrada_scroll.grid(row=0, column=1, sticky="ns")
        entrada_scroll_x = ttk.Scrollbar(
            entrada_contenido,
            orient="horizontal",
            command=self.entrada.xview,
        )
        entrada_scroll_x.grid(row=1, column=0, sticky="ew")
        self.entrada.configure(
            yscrollcommand=entrada_scroll.set,
            xscrollcommand=entrada_scroll_x.set,
        )

        tarjeta_resumen = self._crear_tarjeta(panel_izquierdo)
        tarjeta_resumen.grid(row=1, column=0, sticky="nsew")
        tarjeta_resumen.columnconfigure(0, weight=1)
        tarjeta_resumen.rowconfigure(1, weight=1)
        ttk.Label(
            tarjeta_resumen,
            text="INTERPRETACIÓN",
            style="Panel.TLabel",
        ).grid(row=0, column=0, sticky="w", padx=14, pady=(12, 8))
        self.tabla = ttk.Treeview(
            tarjeta_resumen,
            columns=("nombre", "x", "y"),
            show="headings",
            height=5,
        )
        self.tabla.heading("nombre", text="Ciudad")
        self.tabla.heading("x", text="X")
        self.tabla.heading("y", text="Y")
        self.tabla.column("nombre", anchor="w", width=150)
        self.tabla.column("x", anchor="center", width=55, stretch=False)
        self.tabla.column("y", anchor="center", width=55, stretch=False)
        self.tabla.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 12))

        tarjeta_codigo = self._crear_tarjeta(cuerpo)
        tarjeta_codigo.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        tarjeta_codigo.columnconfigure(0, weight=1)
        tarjeta_codigo.rowconfigure(1, weight=1)
        ttk.Label(
            tarjeta_codigo,
            text="CÓDIGO MINIZINC",
            style="Panel.TLabel",
        ).grid(row=0, column=0, sticky="w", padx=14, pady=(12, 8))
        codigo_contenido = ttk.Frame(tarjeta_codigo, style="App.TFrame")
        codigo_contenido.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 12))
        codigo_contenido.columnconfigure(0, weight=1)
        codigo_contenido.columnconfigure(1, weight=0)
        codigo_contenido.rowconfigure(0, weight=1)
        self.salida = tk.Text(
            codigo_contenido,
            wrap="none",
            relief="flat",
            bd=0,
            padx=12,
            pady=10,
            font=self._fuente_mono(),
            bg=CODIGO_FONDO,
            fg=CODIGO_TEXTO,
            insertbackground=CODIGO_TEXTO,
            selectbackground=PRIMARIO,
            state="disabled",
        )
        self.salida.grid(row=0, column=0, sticky="nsew")
        codigo_scroll = ttk.Scrollbar(
            codigo_contenido,
            orient="vertical",
            command=self.salida.yview,
        )
        codigo_scroll.grid(row=0, column=1, sticky="ns")
        codigo_scroll_x = ttk.Scrollbar(
            codigo_contenido,
            orient="horizontal",
            command=self.salida.xview,
        )
        codigo_scroll_x.grid(row=1, column=0, sticky="ew")
        self.salida.configure(
            yscrollcommand=codigo_scroll.set,
            xscrollcommand=codigo_scroll_x.set,
        )

        barra = ttk.Frame(contenedor, style="App.TFrame")
        barra.grid(row=2, column=0, sticky="ew", pady=(16, 0))
        barra.columnconfigure(0, weight=1)
        ttk.Button(
            barra,
            text="Cargar ejemplo",
            style="Secundario.TButton",
            cursor="hand2",
            command=self.cargar_ejemplo,
        ).grid(row=0, column=0, sticky="w")
        ttk.Button(
            barra,
            text="Limpiar",
            style="Secundario.TButton",
            cursor="hand2",
            command=self.limpiar,
        ).grid(row=0, column=0, sticky="w", padx=(142, 0))
        ttk.Button(
            barra,
            text="Solucionar",
            style="Primario.TButton",
            cursor="hand2",
            command=self.al_solucionar,
        ).grid(row=0, column=1, sticky="e", padx=(0, 10))
        ttk.Button(
            barra,
            text="Copiar",
            style="Secundario.TButton",
            cursor="hand2",
            command=self.copiar_al_portapapeles,
        ).grid(row=0, column=2, sticky="e")

        self.estado = ttk.Label(
            contenedor,
            text="Estado: listo",
            style="Estado.TLabel",
        )
        self.estado.grid(row=3, column=0, sticky="w", pady=(9, 0))

        self.raiz.columnconfigure(0, weight=1)
        self.raiz.rowconfigure(0, weight=1)

    @staticmethod
    def _fuente_mono() -> tuple:
        # Selecciona una fuente monoespaciada según el sistema operativo.
        #
        # Salida: tupla con el nombre de la fuente y su tamaño.
        if sys.platform == "win32":
            return ("Consolas", 10)
        if sys.platform == "darwin":
            return ("Menlo", 10)
        return ("Courier New", 10)

    @staticmethod
    def _crear_tarjeta(parent) -> tk.Frame:
        # Crea un marco con el fondo y el borde de una tarjeta.
        #
        # Entrada: parent, el widget contenedor.
        # Salida: el marco tk.Frame creado.
        return tk.Frame(
            parent,
            bg=TARJETA,
            highlightbackground=BORDES,
            highlightthickness=1,
            bd=0,
        )

    def al_solucionar(self) -> None:
        # Lee el texto del formulario, lo analiza y valida. Muestra las ciudades y el modelo MiniZinc generado, o los errores encontrados.
        self.mostrar_codigo("")
        texto = self.entrada.get("1.0", "end-1c")
        try:
            instancia = parsear_entrada(texto)
        except ErrorEntrada as error:
            self.mostrar_errores([str(error)])
            return

        errores = validar(instancia)
        if errores:
            self.mostrar_errores(errores)
            return

        self.mostrar_resumen_entrada(instancia)
        try:
            plantilla = cargar_plantilla()
            codigo = generar_minizinc(instancia, plantilla)
        except (OSError, ValueError) as error:
            self.mostrar_errores([str(error)])
            return
        self.mostrar_codigo(codigo)

    def mostrar_resumen_entrada(self, instancia) -> None:
        # Actualiza la tabla de ciudades y el mensaje de estado.
        #
        # Entrada: instancia validada con el tamaño del cuadrado y sus ciudades.
        self.tabla.delete(*self.tabla.get_children())
        for ciudad in instancia.ciudades:
            self.tabla.insert(
                "",
                "end",
                values=(ciudad.nombre, ciudad.x, ciudad.y),
            )
        self._actualizar_estado(
            f"Entrada válida: N = {instancia.n}, M = {instancia.m}.",
            EXITO,
        )

    def mostrar_codigo(self, codigo: str) -> None:
        # Reemplaza el contenido del área de salida.
        #
        # Entrada: codigo, texto MiniZinc. Una cadena vacía limpia el área.
        self.salida.configure(state="normal")
        self.salida.delete("1.0", "end")
        if codigo:
            self.salida.insert("1.0", codigo)
        self.salida.configure(state="disabled")
        if codigo:
            self._actualizar_estado("Modelo MiniZinc generado.", EXITO)

    def mostrar_errores(self, errores: list) -> None:
        # Limpia el resultado anterior y muestra los errores en un cuadro de diálogo.
        #
        # Entrada: errores, lista de mensajes u objetos convertibles a texto.
        self.mostrar_codigo("")
        self.tabla.delete(*self.tabla.get_children())
        detalle = "\n".join(str(error) for error in errores)
        self._actualizar_estado(
            f"Error: {errores[0]}" if errores else "Error de entrada.",
            ERROR,
        )
        messagebox.showerror("No se pudo generar el modelo", detalle, parent=self.raiz)

    def copiar_al_portapapeles(self) -> None:
        # Copia al portapapeles el código mostrado y actualiza el estado. Si el área está vacía, muestra un aviso.
        codigo = self.salida.get("1.0", "end-1c")
        if not codigo:
            self._actualizar_estado("No hay código para copiar.", ERROR)
            return
        self.raiz.clipboard_clear()
        self.raiz.clipboard_append(codigo)
        self._actualizar_estado("Código copiado al portapapeles.", EXITO)

    def cargar_ejemplo(self) -> None:
        # Carga un ejemplo en el formulario y borra el resultado anterior.
        ejemplo = "12\n5\nPalmira 2 3\nCali 10 2\nBuga 11 0\nTulua 0 3\nRioFrio 1 2"
        self.entrada.delete("1.0", "end")
        self.entrada.insert("1.0", ejemplo)
        self.mostrar_codigo("")
        self.tabla.delete(*self.tabla.get_children())
        self._actualizar_estado("Ejemplo cargado.", TEXTO_SECUNDARIO)

    def limpiar(self) -> None:
        # Vacía el formulario, el área de código y la tabla de ciudades, y restablece el estado.
        self.entrada.delete("1.0", "end")
        self.mostrar_codigo("")
        self.tabla.delete(*self.tabla.get_children())
        self._actualizar_estado("Estado: listo", TEXTO_SECUNDARIO)

    def _actualizar_estado(self, texto: str, color: str) -> None:
        # Actualiza el mensaje de estado de la ventana.
        #
        # Entrada: texto del mensaje y color de primer plano aceptado por Tkinter.
        self.estado.configure(text=texto, foreground=color)

    def _atajo_solucionar(self, _evento=None) -> str:
        # Ejecuta la generación del modelo al pulsar Ctrl+Enter.
        #
        # Entrada: _evento, evento opcional de Tkinter que el método ignora.
        # Salida: "break", que detiene la propagación del evento.
        self.al_solucionar()
        return "break"
