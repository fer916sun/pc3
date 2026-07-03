# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
# with st.sidebar:
    # slected = option_menu(None, ['Inicio', 'Experiencia', 'Gráficos'], 
        # icons=['camera reels fill', 'stars', 'brilliance'], menu_icon=None, default_index=0)
    # Crea un menú de slected dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de slected disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
selected = option_menu(
    menu_title="Mi información: ", 
    options=['Inicio', 'Experiencia', 'Gráficos'], 
    icons=['camera reels fill', 'stars', 'brilliance'], 
    menu_icon=None, default_index=0, orientation="horizontal")
    # Título que aparece antes de las slected del menú -> menu_title="Selecciona una sección: "
    # Lista de slected que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'stars', 'brilliance']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "slected"
if selected == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>Mi blog</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    col1.image("fotpc3.png", caption='Fernanda', width=300)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
    Soy Fernanda y tengo 19 años, nací en Lima y vivo en Comas.
    Estudio Publicidad, voy en el 5to ciclo y me gusta mucho mi carrera porque me permite ser creativa y aprender cosas nuevas.
    Me gustaría trabajar de creativa en empresas o ser freelancer y crear campañas publicitarias innovadoras. 
    También me gusta mucho el arte y la música, en mi tiempo libre suelo dibujar y escuchar mis canciones favoritas.
    Mi color favorito es el verde y me gusta mucho la naturaleza, por eso disfruto salir a caminar y explorar nuevos lugares.
    Mi pokemón favorito es Piplup porque es muy tierno y me gustan los pinguinos.
    En el futuro me gustaría viajar por el mundo y conocer diferentes culturas y aprender nuevos idiomas.
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif selected == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'>Mi experiencia programando</h1>", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    Mi experiencia aprendiendo a programar ha sido muy interesante y un reto. LLegué casi sin conocimientos previos y al principio
    me sentí un poco abrumada por la cantidad de conceptos nuevos que tenía que aprender.
    Pero ya me he familiarizado con estos conceptos y he aprendido a resolver problemas de manera lógica y ordenada.
    Me gusta mucho la programación porque me permite crear cosas nuevas y es muy curioso ver como se ejecuten los códigos.
    Me gustaría seguir aprendiendo y mejorar mis habilidades para poder desarrollar proyectos más complejos en el futuro.
    Se relaciona con mi carrera porque la publicidad cada vez depende más de la tecnología y la programación,
    y tener conocimientos en este campo me permite tener una ventaja competitiva y poder crear campañas más innovadoras y efectivas.
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - YouTube")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.video("https://youtu.be/FHBf-vXDBus")
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta el desarrollo de un proyecto en Canva para mi Práctica Calificada 1." \
        "Este video muestra una explicación de los operadores booleanos, de pertenencia y lógicos, y cómo se aplican en la programación, así como ejemplos prácticos de su uso." \
    )

    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 2 - YouTube")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    st.link_button(
            "Ver video",
            "https://youtu.be/WIw7eK9-YDg"
        )
    st.video("https://youtu.be/WIw7eK9-YDg")
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta el desarrollo de un proyecto en Canva para mi Práctica Calificada 2." \
        "Este video muestra una explicación de los operadores condicionales: if, elif y else. Se muestram también ejemplos prácticos de su uso." \
    )

elif selected == 'Gráficos':
    st.markdown("<h2 style='text-align: center;'>Gráficos hechos por mí (4 graf y 1 mapa))</h2>", unsafe_allow_html=True)

    graficos = ['Gráfico_1', 'Gráfico_2', 'Gráfico_3', 'Mapa_1']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico_1':
        # Título de la sección
        st.subheader("📊 Gráfico 1: Lluvia de palabras Harry Potter")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Gráfico de lluvia de palabras de un fragmento de Harry Potter.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "llluvia.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico_2':
        # Título de la sección
        st.subheader("📊 Gráfico 2: Familias lingüísticas")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "lengua_familia_GB.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico_3':
        # Título de la sección
        st.subheader("📊 Gráfico 2: Rendimiento Real Madrid Liga Española")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Rendimiento del Real Madrid en la Liga Española
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "gbrm.png",
                width=800
            )
    elif grafico_seleccionado == 'Mapa_1':
        # Título de la sección
        st.subheader("🗺️ Mapa 1: Distribución geográfica")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del mapa.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("mapa.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )
