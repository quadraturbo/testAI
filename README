# 🚀 QuadraTurbo Test Generator

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![AI Powered](https://img.shields.io/badge/AI-Claude%204-purple.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**An intelligent, AI-powered quiz generator that creates interactive tests from your study materials**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Setup](#-api-setup) • [Contributing](#-contributing)

[🌐 Versión en Español](#-versión-en-español)

</div>

---

## 🎯 Overview

QuadraTurbo is a professional command-line tool that leverages Claude AI to automatically generate interactive multiple-choice quizzes from your study documents. Perfect for students, teachers, and lifelong learners who want to test their knowledge efficiently.

## ✨ Features

-  **AI-Powered Generation**: Uses Claude 4 Sonnet to create intelligent, context-aware questions
-  **Multiple Format Support**: PDF, TXT, and Markdown files
-  **4 Difficulty Levels**: Easy, Medium, Hard, and Mixed
-  **Results Tracking**: Persistent history with statistics and performance metrics
-  **Time Tracking**: Measures how long you take to complete each quiz
- **Beautiful CLI**: Colorful, intuitive terminal interface with ASCII art
- **Multiple Files**: Process multiple documents simultaneously
-  **Instant Feedback**: Get explanations for incorrect answers
-  **Grading System**: Automatic scoring with performance categories
-  **Robust Validation**: Extreme error handling and input validation

## 📋 Requirements

- Python 3.8 or higher
- Anthropic API Key (free tier available)
- Internet connection (for AI generation)

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/quadraturbo/quadraturbo-test-generator.git
cd quadraturbo-test-generator
```

2. **Install dependencies**
```bash
pip install anthropic PyPDF2
```

3. **Set up your API Key** (see [API Setup](#-api-setup) section below)

##  Usage

### Basic Usage

```bash
python quadraturbo.py
```

### Best Practices

⚠️ **Important**: For best results, run the script **in the same directory** as your study materials. Absolute paths can sometimes cause issues with file reading, especially on different operating systems.

```bash
# Recommended approach:
cd ~/Documents/my-study-materials/
python /path/to/quadraturbo.py

# Then use relative paths:
# Input: ./chapter1.pdf, notes.txt, summary.md
```

### Workflow

1. The program displays the QuadraTurbo banner
2. Main menu with options: New Test, View History, Exit
3. Enter file path(s) - separate multiple files with commas
4. Choose number of questions (1-50)
5. Select difficulty level
6. Wait for AI to generate questions
7. Answer interactively in the terminal
8. Review detailed results with explanations
9. Results are automatically saved to history

## 🔑 API Setup

### Getting Your Free API Key

1. **Create an Anthropic Account**
   - Visit: https://console.anthropic.com/
   - Sign up with your email

2. **Generate API Key**
   - Navigate to "API Keys" in the console
   - Click "Create Key"
   - Copy and save the key securely (shown only once)

3. **Set the API Key**

**Linux/Mac:**
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

**Windows (CMD):**
```cmd
set ANTHROPIC_API_KEY=your-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="your-api-key-here"
```

**Alternative**: The script will prompt you for the key if not found in environment variables.

### API Limitations & Cost

- **Free Tier**: $10 USD in credits per month
- **Cost per Test**: Approximately $0.05-$0.15 (depending on document size and question count)
- **Estimated Usage**: 60-200 quiz generations with free tier

**Tips to Maximize Free Credits:**
- Generate 5-10 questions per test instead of 50
- Use shorter documents or relevant excerpts
- Save and reuse generated questions
- Run tests locally from saved question sets

##  Supported File Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| PDF | `.pdf` | Automatic text extraction |
| Text | `.txt` | Multiple encoding support (UTF-8, Latin-1, etc.) |
| Markdown | `.md` | Full markdown support |

## 🎮 Interactive Features

- **Real-time Validation**: Immediate feedback on your answers
- **Smart Exit**: Type 'salir' during quiz to exit gracefully
- **Color-Coded Results**: Visual feedback with green (correct) and red (incorrect)
- **Performance Grades**: 
  - 90-100%: EXCELLENT 🏆
  - 80-89%: VERY GOOD 🌟
  - 70-79%: GOOD ✓
  - 60-69%: PASSED
  - 0-59%: NEEDS MORE STUDY 📚

##  History & Statistics

Results are automatically saved to `~/.quadraturbo_history.json` with:
- Date and time
- Score (correct/total)
- Percentage
- Time taken
- Last 10 results viewable from main menu

## 🛠️ Troubleshooting

**Problem**: "File not found" error
- **Solution**: Use relative paths and run script from the document directory

**Problem**: "Cannot read PDF"
- **Solution**: Ensure PyPDF2 is installed: `pip install PyPDF2`

**Problem**: "API Error"
- **Solution**: Check your API key is correctly set and you have remaining credits

**Problem**: Encoding errors with TXT files
- **Solution**: The script tries multiple encodings automatically. If issues persist, save file as UTF-8

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created by [@quadraturbo](https://github.com/quadraturbo)

## 🙏 Acknowledgments

- Powered by [Anthropic's Claude AI](https://www.anthropic.com/)
- Inspired by the need for better study tools

---
---
---

# 🌐 Versión en Español

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Licencia](https://img.shields.io/badge/licencia-MIT-green.svg)
![AI Powered](https://img.shields.io/badge/AI-Claude%204-purple.svg)
![Estado](https://img.shields.io/badge/estado-activo-success.svg)

**Un generador de tests inteligente impulsado por IA que crea pruebas interactivas desde tus materiales de estudio**

[Características](#-características) • [Instalación](#-instalación) • [Uso](#-uso) • [Configuración API](#-configuración-de-api) • [Contribuir](#-contribuir)

</div>

---

## 🎯 Descripción General

QuadraTurbo es una herramienta profesional de línea de comandos que utiliza Claude AI para generar automáticamente cuestionarios interactivos de opción múltiple a partir de tus materiales de estudio. Perfecto para estudiantes, profesores y aprendices de por vida que quieren evaluar sus conocimientos de manera eficiente.

##  Características

-  **Generación con IA**: Usa Claude 4 Sonnet para crear preguntas inteligentes y contextuales
-  **Múltiples Formatos**: Archivos PDF, TXT y Markdown
-  **4 Niveles de Dificultad**: Fácil, Medio, Difícil y Mixto
-  **Seguimiento de Resultados**: Historial persistente con estadísticas y métricas de rendimiento
-  **Medición de Tiempo**: Mide cuánto tardas en completar cada test
-  **CLI Hermosa**: Interfaz de terminal colorida e intuitiva con arte ASCII
-  **Múltiples Archivos**: Procesa varios documentos simultáneamente
-  **Retroalimentación Instantánea**: Obtén explicaciones para respuestas incorrectas
-  **Sistema de Calificación**: Puntuación automática con categorías de rendimiento
-  **Validación Robusta**: Manejo extremo de errores y validación de entradas

##  Requisitos

- Python 3.8 o superior
- Clave API de Anthropic (tier gratuito disponible)
- Conexión a Internet (para generación con IA)

## 🔧 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/quadraturbo/quadraturbo-test-generator.git
cd quadraturbo-test-generator
```

2. **Instalar dependencias**
```bash
pip install anthropic PyPDF2
```

3. **Configurar tu API Key** (ver sección [Configuración de API](#-configuración-de-api) más abajo)

##  Uso

### Uso Básico

```bash
python quadraturbo.py
```

### Mejores Prácticas

⚠️ **Importante**: Para mejores resultados, ejecuta el script **en el mismo directorio** que tus materiales de estudio. Las rutas absolutas pueden causar problemas con la lectura de archivos, especialmente en diferentes sistemas operativos.

```bash
# Enfoque recomendado:
cd ~/Documentos/mis-materiales-de-estudio/
python /ruta/al/quadraturbo.py

# Luego usa rutas relativas:
# Entrada: ./capitulo1.pdf, notas.txt, resumen.md
```

### Flujo de Trabajo

1. El programa muestra el banner de QuadraTurbo
2. Menú principal con opciones: Nuevo Test, Ver Historial, Salir
3. Ingresa ruta(s) de archivo(s) - separa múltiples archivos con comas
4. Elige número de preguntas (1-50)
5. Selecciona nivel de dificultad
6. Espera a que la IA genere las preguntas
7. Responde interactivamente en la terminal
8. Revisa resultados detallados con explicaciones
9. Los resultados se guardan automáticamente en el historial

## 🔑 Configuración de API

### Obtener tu API Key Gratuita

1. **Crear una Cuenta en Anthropic**
   - Visita: https://console.anthropic.com/
   - Regístrate con tu email

2. **Generar API Key**
   - Navega a "API Keys" en la consola
   - Haz clic en "Create Key"
   - Copia y guarda la clave de forma segura (se muestra solo una vez)

3. **Configurar la API Key**

**Linux/Mac:**
```bash
export ANTHROPIC_API_KEY="tu-clave-api-aqui"
```

**Windows (CMD):**
```cmd
set ANTHROPIC_API_KEY=tu-clave-api-aqui
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="tu-clave-api-aqui"
```

**Alternativa**: El script te pedirá la clave si no la encuentra en las variables de entorno.

### Limitaciones y Costos de la API

- **Tier Gratuito**: $10 USD en créditos por mes
- **Costo por Test**: Aproximadamente $0.05-$0.15 (dependiendo del tamaño del documento y cantidad de preguntas)
- **Uso Estimado**: 60-200 generaciones de tests con el tier gratuito

**Consejos para Maximizar Créditos Gratuitos:**
- Genera 5-10 preguntas por test en lugar de 50
- Usa documentos más cortos o extractos relevantes
- Guarda y reutiliza preguntas generadas
- Ejecuta tests localmente desde conjuntos de preguntas guardados

##  Formatos de Archivo Soportados

| Formato | Extensión | Notas |
|---------|-----------|-------|
| PDF | `.pdf` | Extracción automática de texto |
| Texto | `.txt` | Soporte para múltiples codificaciones (UTF-8, Latin-1, etc.) |
| Markdown | `.md` | Soporte completo de markdown |

## 🎮 Características Interactivas

- **Validación en Tiempo Real**: Retroalimentación inmediata sobre tus respuestas
- **Salida Inteligente**: Escribe 'salir' durante el test para salir limpiamente
- **Resultados con Código de Colores**: Retroalimentación visual con verde (correcto) y rojo (incorrecto)
- **Calificaciones de Rendimiento**: 
  - 90-100%: EXCELENTE 🏆
  - 80-89%: MUY BIEN 🌟
  - 70-79%: BIEN ✓
  - 60-69%: APROBADO
  - 0-59%: NECESITAS ESTUDIAR MÁS 📚

##  Historial y Estadísticas

Los resultados se guardan automáticamente en `~/.quadraturbo_history.json` con:
- Fecha y hora
- Puntuación (correctas/total)
- Porcentaje
- Tiempo empleado
- Últimos 10 resultados visibles desde el menú principal

## 🛠️ Solución de Problemas

**Problema**: Error "Archivo no encontrado"
- **Solución**: Usa rutas relativas y ejecuta el script desde el directorio de documentos

**Problema**: "No se puede leer PDF"
- **Solución**: Asegúrate de que PyPDF2 está instalado: `pip install PyPDF2`

**Problema**: "Error de API"
- **Solución**: Verifica que tu API key esté correctamente configurada y tengas créditos restantes

**Problema**: Errores de codificación con archivos TXT
- **Solución**: El script prueba múltiples codificaciones automáticamente. Si persisten problemas, guarda el archivo como UTF-8

##  Contribuir

¡Las contribuciones son bienvenidas! Por favor, siéntete libre de enviar un Pull Request. Para cambios importantes, abre primero un issue para discutir qué te gustaría cambiar.

##  Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## 👨‍💻 Autor

Creado por [@quadraturbo](https://github.com/quadraturbo)

## 🙏 Agradecimientos

- Powered by [Claude AI de Anthropic](https://www.anthropic.com/)
- Inspirado por la necesidad de mejores herramientas de estudio

---

<div align="center">

**⭐ Si este proyecto te resultó útil, considera darle una estrella en GitHub ⭐**

Made with ❤️ and ☕ by quadraturbo

</div>
