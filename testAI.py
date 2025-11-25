#!/usr/bin/env python3

import os
import sys
import json
import time
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

try:
    import anthropic
except ImportError:
    anthropic = None


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class QuadraTurboTest:
    
    BANNER = f"""{Colors.CYAN}
    ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗  █████╗ ████████╗██╗   ██╗██████╗ ██████╗  ██████╗ 
   ██╔═══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗
   ██║   ██║██║   ██║███████║██║  ██║██████╔╝███████║   ██║   ██║   ██║██████╔╝██████╔╝██║   ██║
   ██║▄▄ ██║██║   ██║██╔══██║██║  ██║██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗██╔══██╗██║   ██║
   ╚██████╔╝╚██████╔╝██║  ██║██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║██████╔╝╚██████╔╝
    ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ 
{Colors.ENDC}
{Colors.BOLD}                           Sistema Generador de Tests Inteligente{Colors.ENDC}
{Colors.YELLOW}                                    powered by Claude AI{Colors.ENDC}
"""
    
    def __init__(self):
        self.questions: List[Dict] = []
        self.answers: List[int] = []
        self.results_history: List[Dict] = []
        self.api_key = os.environ.get('ANTHROPIC_API_KEY', '')
        self.client = None
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_banner(self):
        self.clear_screen()
        print(self.BANNER)
        
    def validate_file_path(self, path: str) -> Tuple[bool, str]:
        if not path or path.strip() == '':
            return False, "Ruta vacía"
        
        path = path.strip().strip('"').strip("'")
        
        if not os.path.exists(path):
            return False, f"El archivo no existe: {path}"
        
        if not os.path.isfile(path):
            return False, f"La ruta no es un archivo: {path}"
        
        ext = Path(path).suffix.lower()
        if ext not in ['.pdf', '.txt', '.md']:
            return False, f"Extensión no soportada: {ext}. Use .pdf, .txt o .md"
        
        if not os.access(path, os.R_OK):
            return False, f"No hay permisos de lectura: {path}"
        
        return True, path
    
    def read_txt_file(self, path: str) -> Optional[str]:
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        
        for encoding in encodings:
            try:
                with open(path, 'r', encoding=encoding) as f:
                    content = f.read()
                    if content.strip():
                        return content
            except (UnicodeDecodeError, Exception):
                continue
        
        return None
    
    def read_md_file(self, path: str) -> Optional[str]:
        return self.read_txt_file(path)
    
    def read_pdf_file(self, path: str) -> Optional[str]:
        if PyPDF2 is None:
            print(f"{Colors.RED}Error: PyPDF2 no instalado. Instala con: pip install PyPDF2{Colors.ENDC}")
            return None
        
        try:
            with open(path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                
                if len(reader.pages) == 0:
                    return None
                
                content = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        content += text + "\n"
                
                return content.strip() if content.strip() else None
                
        except Exception as e:
            print(f"{Colors.RED}Error leyendo PDF: {str(e)}{Colors.ENDC}")
            return None
    
    def read_file_content(self, path: str) -> Optional[str]:
        ext = Path(path).suffix.lower()
        
        if ext == '.pdf':
            return self.read_pdf_file(path)
        elif ext == '.txt':
            return self.read_txt_file(path)
        elif ext == '.md':
            return self.read_md_file(path)
        
        return None
    
    def get_file_paths(self) -> List[str]:
        print(f"\n{Colors.BOLD}📁 Ingreso de Archivos{Colors.ENDC}")
        print(f"{Colors.CYAN}Puedes ingresar múltiples archivos separados por comas{Colors.ENDC}")
        print(f"{Colors.YELLOW}Formatos soportados: PDF, TXT, MD{Colors.ENDC}\n")
        
        while True:
            user_input = input(f"{Colors.GREEN}Rutas de archivos: {Colors.ENDC}").strip()
            
            if not user_input:
                print(f"{Colors.RED}⚠ Debes ingresar al menos un archivo{Colors.ENDC}")
                continue
            
            paths = [p.strip() for p in user_input.split(',')]
            valid_paths = []
            
            for path in paths:
                is_valid, result = self.validate_file_path(path)
                if is_valid:
                    valid_paths.append(result)
                    print(f"{Colors.GREEN}✓ Archivo válido: {Path(result).name}{Colors.ENDC}")
                else:
                    print(f"{Colors.RED}✗ {result}{Colors.ENDC}")
            
            if valid_paths:
                return valid_paths
            else:
                print(f"{Colors.RED}⚠ No se encontraron archivos válidos. Intenta nuevamente.{Colors.ENDC}\n")
    
    def get_question_count(self) -> int:
        print(f"\n{Colors.BOLD}❓ Configuración del Test{Colors.ENDC}")
        
        while True:
            try:
                count = input(f"{Colors.GREEN}Cantidad de preguntas a generar (1-50): {Colors.ENDC}").strip()
                
                if not count:
                    print(f"{Colors.RED}⚠ Debes ingresar un número{Colors.ENDC}")
                    continue
                
                count = int(count)
                
                if count < 1 or count > 50:
                    print(f"{Colors.RED}⚠ El número debe estar entre 1 y 50{Colors.ENDC}")
                    continue
                
                return count
                
            except ValueError:
                print(f"{Colors.RED}⚠ Entrada inválida. Ingresa un número válido{Colors.ENDC}")
    
    def get_difficulty(self) -> str:
        print(f"\n{Colors.BOLD}🎯 Nivel de Dificultad{Colors.ENDC}")
        print(f"{Colors.CYAN}1.{Colors.ENDC} Fácil")
        print(f"{Colors.CYAN}2.{Colors.ENDC} Medio")
        print(f"{Colors.CYAN}3.{Colors.ENDC} Difícil")
        print(f"{Colors.CYAN}4.{Colors.ENDC} Mixto")
        
        while True:
            choice = input(f"\n{Colors.GREEN}Selecciona dificultad (1-4): {Colors.ENDC}").strip()
            
            if choice == '1':
                return 'facil'
            elif choice == '2':
                return 'medio'
            elif choice == '3':
                return 'dificil'
            elif choice == '4':
                return 'mixto'
            else:
                print(f"{Colors.RED}⚠ Opción inválida{Colors.ENDC}")
    
    def initialize_api_client(self) -> bool:
        if anthropic is None:
            print(f"\n{Colors.RED}Error: Librería anthropic no instalada{Colors.ENDC}")
            print(f"{Colors.YELLOW}Instala con: pip install anthropic{Colors.ENDC}")
            return False
        
        if not self.api_key:
            print(f"\n{Colors.YELLOW}⚠ No se encontró ANTHROPIC_API_KEY en variables de entorno{Colors.ENDC}")
            self.api_key = input(f"{Colors.GREEN}Ingresa tu API Key de Anthropic: {Colors.ENDC}").strip()
            
            if not self.api_key:
                print(f"{Colors.RED}API Key requerida para generar preguntas{Colors.ENDC}")
                return False
        
        try:
            self.client = anthropic.Anthropic(api_key=self.api_key)
            return True
        except Exception as e:
            print(f"{Colors.RED}Error inicializando cliente: {str(e)}{Colors.ENDC}")
            return False
    
    def generate_questions(self, content: str, count: int, difficulty: str) -> bool:
        if not self.initialize_api_client():
            return False
        
        print(f"\n{Colors.CYAN}🤖 Generando {count} preguntas con IA...{Colors.ENDC}")
        
        difficulty_map = {
            'facil': 'básico, conceptos fundamentales',
            'medio': 'intermedio, requiere comprensión',
            'dificil': 'avanzado, análisis profundo',
            'mixto': 'variado, mezclando todos los niveles'
        }
        
        prompt = f"""Analiza el siguiente contenido y genera exactamente {count} preguntas de opción múltiple de nivel {difficulty_map[difficulty]}.

CONTENIDO:
{content[:15000]}

INSTRUCCIONES CRÍTICAS:
1. Genera EXACTAMENTE {count} preguntas relevantes sobre el contenido
2. Cada pregunta debe tener 4 opciones (A, B, C, D)
3. Solo UNA opción es correcta
4. Las opciones incorrectas deben ser plausibles pero claramente incorrectas
5. Varía la posición de la respuesta correcta
6. Incluye una explicación breve de por qué la respuesta es correcta

FORMATO JSON ESTRICTO:
{{
  "preguntas": [
    {{
      "pregunta": "¿Texto de la pregunta?",
      "opciones": {{
        "A": "Primera opción",
        "B": "Segunda opción",
        "C": "Tercera opción",
        "D": "Cuarta opción"
      }},
      "respuesta_correcta": "A",
      "explicacion": "Explicación de por qué A es correcta"
    }}
  ]
}}

Responde ÚNICAMENTE con el JSON, sin texto adicional."""

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=8000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = message.content[0].text.strip()
            
            response_text = re.sub(r'^```json\s*', '', response_text)
            response_text = re.sub(r'\s*```$', '', response_text)
            response_text = response_text.strip()
            
            data = json.loads(response_text)
            
            if 'preguntas' not in data or not isinstance(data['preguntas'], list):
                print(f"{Colors.RED}Error: Formato de respuesta inválido{Colors.ENDC}")
                return False
            
            self.questions = data['preguntas']
            
            if len(self.questions) != count:
                print(f"{Colors.YELLOW}⚠ Se generaron {len(self.questions)} preguntas (esperadas: {count}){Colors.ENDC}")
            
            for i, q in enumerate(self.questions):
                if not all(key in q for key in ['pregunta', 'opciones', 'respuesta_correcta']):
                    print(f"{Colors.RED}Error: Pregunta {i+1} con formato incorrecto{Colors.ENDC}")
                    return False
                
                if not isinstance(q['opciones'], dict) or len(q['opciones']) != 4:
                    print(f"{Colors.RED}Error: Pregunta {i+1} no tiene 4 opciones{Colors.ENDC}")
                    return False
                
                if q['respuesta_correcta'] not in q['opciones']:
                    print(f"{Colors.RED}Error: Respuesta correcta inválida en pregunta {i+1}{Colors.ENDC}")
                    return False
            
            print(f"{Colors.GREEN}✓ {len(self.questions)} preguntas generadas exitosamente{Colors.ENDC}")
            return True
            
        except json.JSONDecodeError as e:
            print(f"{Colors.RED}Error decodificando respuesta JSON: {str(e)}{Colors.ENDC}")
            return False
        except Exception as e:
            print(f"{Colors.RED}Error generando preguntas: {str(e)}{Colors.ENDC}")
            return False
    
    def run_test(self):
        self.answers = []
        start_time = time.time()
        
        print(f"\n{Colors.BOLD}{'='*80}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.CYAN}🎓 INICIANDO TEST{Colors.ENDC}")
        print(f"{Colors.BOLD}{'='*80}{Colors.ENDC}\n")
        
        for i, question in enumerate(self.questions, 1):
            print(f"{Colors.BOLD}{Colors.BLUE}Pregunta {i}/{len(self.questions)}{Colors.ENDC}")
            print(f"{Colors.YELLOW}{question['pregunta']}{Colors.ENDC}\n")
            
            for key in sorted(question['opciones'].keys()):
                print(f"  {Colors.CYAN}{key}.{Colors.ENDC} {question['opciones'][key]}")
            
            while True:
                answer = input(f"\n{Colors.GREEN}Tu respuesta (A/B/C/D) o 'salir': {Colors.ENDC}").strip().upper()
                
                if answer == 'SALIR':
                    print(f"\n{Colors.YELLOW}Test cancelado por el usuario{Colors.ENDC}")
                    return False
                
                if answer in question['opciones']:
                    self.answers.append(answer)
                    break
                else:
                    print(f"{Colors.RED}⚠ Respuesta inválida. Usa A, B, C o D{Colors.ENDC}")
            
            print(f"\n{Colors.BOLD}{'─'*80}{Colors.ENDC}\n")
        
        elapsed_time = time.time() - start_time
        self.show_results(elapsed_time)
        return True
    
    def show_results(self, elapsed_time: float):
        self.clear_screen()
        print(f"\n{Colors.BOLD}{'='*80}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.CYAN}📊 RESULTADOS DEL TEST{Colors.ENDC}")
        print(f"{Colors.BOLD}{'='*80}{Colors.ENDC}\n")
        
        correct = 0
        total = len(self.questions)
        
        for i, (question, user_answer) in enumerate(zip(self.questions, self.answers), 1):
            correct_answer = question['respuesta_correcta']
            is_correct = user_answer == correct_answer
            
            if is_correct:
                correct += 1
                status = f"{Colors.GREEN}✓ CORRECTO{Colors.ENDC}"
            else:
                status = f"{Colors.RED}✗ INCORRECTO{Colors.ENDC}"
            
            print(f"{Colors.BOLD}Pregunta {i}:{Colors.ENDC} {question['pregunta']}")
            print(f"Tu respuesta: {Colors.CYAN}{user_answer}{Colors.ENDC} | Correcta: {Colors.GREEN}{correct_answer}{Colors.ENDC} | {status}")
            
            if not is_correct and 'explicacion' in question:
                print(f"{Colors.YELLOW}💡 {question['explicacion']}{Colors.ENDC}")
            
            print(f"{Colors.BOLD}{'─'*80}{Colors.ENDC}\n")
        
        percentage = (correct / total) * 100
        
        print(f"{Colors.BOLD}{'='*80}{Colors.ENDC}")
        print(f"{Colors.BOLD}Preguntas correctas: {Colors.GREEN}{correct}/{total}{Colors.ENDC}")
        print(f"{Colors.BOLD}Porcentaje: {self.get_grade_color(percentage)}{percentage:.1f}%{Colors.ENDC}")
        print(f"{Colors.BOLD}Tiempo total: {Colors.CYAN}{self.format_time(elapsed_time)}{Colors.ENDC}")
        print(f"{Colors.BOLD}Calificación: {self.get_grade_text(percentage)}{Colors.ENDC}")
        print(f"{Colors.BOLD}{'='*80}{Colors.ENDC}\n")
        
        self.save_result(correct, total, percentage, elapsed_time)
    
    def get_grade_color(self, percentage: float) -> str:
        if percentage >= 90:
            return Colors.GREEN
        elif percentage >= 70:
            return Colors.YELLOW
        else:
            return Colors.RED
    
    def get_grade_text(self, percentage: float) -> str:
        if percentage >= 90:
            return f"{Colors.GREEN}EXCELENTE 🏆{Colors.ENDC}"
        elif percentage >= 80:
            return f"{Colors.GREEN}MUY BIEN 🌟{Colors.ENDC}"
        elif percentage >= 70:
            return f"{Colors.YELLOW}BIEN ✓{Colors.ENDC}"
        elif percentage >= 60:
            return f"{Colors.YELLOW}APROBADO{Colors.ENDC}"
        else:
            return f"{Colors.RED}NECESITAS ESTUDIAR MÁS 📚{Colors.ENDC}"
    
    def format_time(self, seconds: float) -> str:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes}m {secs}s"
    
    def save_result(self, correct: int, total: int, percentage: float, time: float):
        result = {
            'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'correctas': correct,
            'total': total,
            'porcentaje': round(percentage, 2),
            'tiempo': round(time, 2)
        }
        
        self.results_history.append(result)
        
        try:
            history_file = Path.home() / '.quadraturbo_history.json'
            
            existing_history = []
            if history_file.exists():
                with open(history_file, 'r', encoding='utf-8') as f:
                    existing_history = json.load(f)
            
            existing_history.append(result)
            
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(existing_history, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f"{Colors.YELLOW}⚠ No se pudo guardar el historial: {str(e)}{Colors.ENDC}")
    
    def show_history(self):
        try:
            history_file = Path.home() / '.quadraturbo_history.json'
            
            if not history_file.exists():
                print(f"\n{Colors.YELLOW}No hay historial previo{Colors.ENDC}")
                return
            
            with open(history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
            
            if not history:
                print(f"\n{Colors.YELLOW}El historial está vacío{Colors.ENDC}")
                return
            
            self.clear_screen()
            print(f"\n{Colors.BOLD}{'='*80}{Colors.ENDC}")
            print(f"{Colors.BOLD}{Colors.CYAN}📈 HISTORIAL DE RESULTADOS{Colors.ENDC}")
            print(f"{Colors.BOLD}{'='*80}{Colors.ENDC}\n")
            
            for i, result in enumerate(history[-10:], 1):
                percentage = result['porcentaje']
                color = self.get_grade_color(percentage)
                
                print(f"{Colors.BOLD}Test #{i}{Colors.ENDC}")
                print(f"Fecha: {Colors.CYAN}{result['fecha']}{Colors.ENDC}")
                print(f"Resultado: {Colors.GREEN}{result['correctas']}/{result['total']}{Colors.ENDC} ({color}{percentage}%{Colors.ENDC})")
                print(f"Tiempo: {Colors.CYAN}{self.format_time(result['tiempo'])}{Colors.ENDC}")
                print(f"{Colors.BOLD}{'─'*80}{Colors.ENDC}\n")
            
            if len(history) > 10:
                print(f"{Colors.YELLOW}Mostrando últimos 10 resultados de {len(history)} totales{Colors.ENDC}\n")
                
        except Exception as e:
            print(f"{Colors.RED}Error cargando historial: {str(e)}{Colors.ENDC}")
    
    def main_menu(self):
        while True:
            print(f"\n{Colors.BOLD}{'='*80}{Colors.ENDC}")
            print(f"{Colors.BOLD}{Colors.CYAN}MENÚ PRINCIPAL{Colors.ENDC}")
            print(f"{Colors.BOLD}{'='*80}{Colors.ENDC}\n")
            print(f"{Colors.CYAN}1.{Colors.ENDC} Nuevo Test")
            print(f"{Colors.CYAN}2.{Colors.ENDC} Ver Historial")
            print(f"{Colors.CYAN}3.{Colors.ENDC} Salir")
            
            choice = input(f"\n{Colors.GREEN}Selecciona una opción (1-3): {Colors.ENDC}").strip()
            
            if choice == '1':
                return True
            elif choice == '2':
                self.show_history()
                input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.ENDC}")
                self.clear_screen()
                self.print_banner()
            elif choice == '3':
                print(f"\n{Colors.GREEN}¡Hasta luego! 👋{Colors.ENDC}\n")
                return False
            else:
                print(f"{Colors.RED}⚠ Opción inválida{Colors.ENDC}")
    
    def run(self):
        self.print_banner()
        
        if not self.main_menu():
            return
        
        file_paths = self.get_file_paths()
        
        print(f"\n{Colors.CYAN}📖 Leyendo archivos...{Colors.ENDC}")
        
        all_content = []
        for path in file_paths:
            content = self.read_file_content(path)
            if content:
                all_content.append(content)
                print(f"{Colors.GREEN}✓ Contenido extraído de: {Path(path).name}{Colors.ENDC}")
            else:
                print(f"{Colors.RED}✗ No se pudo leer: {Path(path).name}{Colors.ENDC}")
        
        if not all_content:
            print(f"\n{Colors.RED}Error: No se pudo extraer contenido de ningún archivo{Colors.ENDC}")
            return
        
        combined_content = "\n\n".join(all_content)
        
        if len(combined_content) < 100:
            print(f"\n{Colors.RED}Error: Contenido insuficiente para generar preguntas{Colors.ENDC}")
            return
        
        question_count = self.get_question_count()
        difficulty = self.get_difficulty()
        
        if not self.generate_questions(combined_content, question_count, difficulty):
            print(f"\n{Colors.RED}No se pudieron generar las preguntas{Colors.ENDC}")
            return
        
        input(f"\n{Colors.CYAN}Presiona Enter para comenzar el test...{Colors.ENDC}")
        self.clear_screen()
        
        if self.run_test():
            while True:
                choice = input(f"\n{Colors.GREEN}¿Realizar otro test? (s/n): {Colors.ENDC}").strip().lower()
                
                if choice == 's':
                    self.run()
                    break
                elif choice == 'n':
                    print(f"\n{Colors.GREEN}¡Hasta luego! 👋{Colors.ENDC}\n")
                    break
                else:
                    print(f"{Colors.RED}⚠ Respuesta inválida{Colors.ENDC}")


def main():
    try:
        app = QuadraTurboTest()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Programa interrumpido por el usuario{Colors.ENDC}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}Error fatal: {str(e)}{Colors.ENDC}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
