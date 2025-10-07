# AI Marketing Suite

Plataforma SaaS completa de Inteligencia Artificial para Marketing Digital.

## 🚀 Características Principales

- **Casos de Uso de IA** completamente funcionales y demo-ready
- **Autenticación de usuarios** con sesiones seguras
- **Dashboard interactivo** con métricas en tiempo real
- **Interfaz moderna y responsive** con sidebar de navegación
- **Demos interactivos** para cada funcionalidad
- **Backend Management** con MLOps y Agent Gallery
- **Knowledge Base** con RAG y Knowledge Graphs
- **100% en Español** - Interfaz completamente localizada

## 📋 Arquitectura de la Plataforma

### Casos de Uso por Categoría

#### 🔍 Benchmark
- **Monitorización de Marca** - Análisis de sentimiento en tiempo real
- **Inteligencia Competitiva GenAI** - Análisis competitivo con IA

#### 📊 Insights y Aprendizajes
- **Predicción de Abandonos** - Identificación de clientes en riesgo
- **Segmentación Avanzada** - Agrupación inteligente de clientes
- **Attribution Marketing** - Optimización de inversión multi-touch

#### 🎨 Estudio Creativo
- **Generación de Contenido GenAI** - Creación automática de campañas y videos

#### 🤖 Content Automation Tool
- **Personalización de Experiencias** - Ofertas únicas por cliente
- **Motor de Recomendaciones** - Sugerencias personalizadas
- **A/B Testing Automatizado** - Experimentación continua

#### 🛡️ Brand Guardian
- **Agentes Conversacionales** - Chatbots IA 24/7
- **Optimización Publicitaria** - Mejora automática de campañas

### Backend Infrastructure

#### ⚙️ Backend
- **MLOps** - Gestión del ciclo de vida de modelos ML (12 modelos en producción)
- **Agent Gallery** - 18 agentes especializados de IA con soporte para MCP servers y sistemas multi-agent

### Data & Integración

- **Integración de Datos** - Conectores con CRM, ERP, Analytics
- **APIs & Conectores** - Endpoints REST para integración empresarial
- **Knowledge Base** - RAG (Vector DBs) y Knowledge Graphs para alimentar agentes
- **Laboratorio de Datos** - Notebooks Python para análisis exploratorio
- **Monitorización & Auditoría** - Seguimiento del sistema en producción

## 🛠️ Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio:**
```bash
git clone <repository-url>
cd marketing-ai-suite
```

2. **Crear y activar el entorno virtual:**
```bash
python -m venv venv

# En Windows:
.\venv\Scripts\Activate.ps1

# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación:**
```bash
python app.py
```

5. **Abrir en el navegador:**
```
http://localhost:5555
```

## 🔐 Credenciales de Demo

Utiliza cualquiera de estas credenciales para acceder a la plataforma:

| Email | Contraseña | Rol |
|-------|-----------|-----|
| admin@company.com | demo2025 | Administrador |
| marketing@company.com | demo2025 | Director Marketing |
| demo@company.com | demo2025 | Analista Marketing |

## 📁 Estructura del Proyecto

```
marketing-ai-suite/
├── app.py                          # Aplicación Flask principal
├── requirements.txt                # Dependencias Python
├── README.md                       # Este archivo
├── config/
│   └── menu_config.json           # Configuración del menú
├── templates/                      # Plantillas HTML
│   ├── base.html                  # Template base con sidebar
│   ├── login.html                 # Página de login
│   ├── home.html                  # Home con 6 botones principales
│   ├── dashboard.html             # Dashboard principal (Torre de Control)
│   ├── introduccion.html          # Documentación técnica editable
│   │
│   ├── # Casos de Uso
│   ├── personalizacion.html       
│   ├── contenido_genai.html       # Incluye generador de videos con Google ViGenAiR
│   ├── chatbot.html               
│   ├── prediccion_churn.html      
│   ├── optimizacion_publicitaria.html
│   ├── segmentacion_avanzada.html 
│   ├── ab_testing.html            
│   ├── monitorizacion_marca.html  
│   ├── motor_recomendaciones.html 
│   ├── attribution_marketing.html 
│   ├── inteligencia_competitiva.html  # Competitive Intelligence Copilot
│   │
│   ├── # Backend
│   ├── mlops.html                 # Gestión de modelos ML
│   ├── agent_gallery.html         # Galería de agentes de IA
│   │
│   ├── # Data & Integración
│   ├── integracion_datos.html     
│   ├── integracion_apis.html      
│   ├── knowledge_base.html        # RAG & Knowledge Graphs
│   ├── laboratorio.html           
│   ├── monitorizacion.html        
│   │
│   ├── # Sistema
│   ├── configuracion.html         # Configuración (vista de menú)
│   ├── asistente_panel_fijo.html  # Asistente virtual contextual
│   ├── 404.html                   # Error 404
│   └── 500.html                   # Error 500
│
└── static/                         # Archivos estáticos
    └── css/
        └── style.css              # Estilos CSS centralizados
```

## 🎯 Características Técnicas

### Backend (Flask)
- **Autenticación basada en sesiones** con Flask sessions
- **Rutas RESTful** para cada funcionalidad
- **APIs JSON** para interacciones dinámicas
- **Configuración dinámica del menú** con menu_config.json
- **Simulación de datos** realista sin necesidad de base de datos
- **Manejo de errores** con páginas 404 y 500 personalizadas

### Frontend
- **Diseño responsive** que funciona en móviles, tablets y desktop
- **Sidebar fijo colapsable** con navegación intuitiva
- **Menú configurable** con vistas por categoría o roadmap (Quick Wins vs Año 2+)
- **Animaciones suaves** con CSS transitions
- **Componentes interactivos** con JavaScript vanilla
- **Asistente virtual contextual** en páginas clave
- **Paneles de documentación técnica** editables con persistencia en localStorage

### Knowledge Management
- **RAG (Retrieval Augmented Generation)**:
  - 3 colecciones vectoriales simuladas (Pinecone, Weaviate, Chroma)
  - 2,847 documentos indexados
  - 1.2M chunks vectorizados
  - Playground de búsqueda semántica
  
- **Knowledge Graphs**:
  - 2 grafos Neo4j simulados
  - 45K nodos y 129K relaciones
  - Cypher Query Playground
  - Visualización de schema

### Backend Infrastructure
- **MLOps**:
  - 12 modelos en producción
  - 8 modelos en desarrollo
  - Métricas de rendimiento en tiempo real
  - Modal para crear nuevos modelos
  
- **Agent Gallery**:
  - 18 agentes especializados
  - Conexión a MCP servers
  - Sistemas multi-agent con orquestación
  - Frameworks: CrewAI, AutoGen, LangGraph

### Seguridad
- **Sesiones seguras** con secret key
- **Decorador @login_required** para proteger rutas
- **Validación de formularios** en cliente y servidor

## 📊 Métricas y KPIs Simulados

La plataforma simula métricas realistas basadas en investigación del sector:

- **ROI esperado:** 4:1 a 6:1
- **Payback:** 18-24 meses
- **Reducción de churn:** 15-25%
- **Aumento de conversión:** 25-320%
- **Mejora de engagement:** 25-50%

## 🔧 Personalización

### Cambiar el Puerto

Edita `app.py` línea final:
```python
app.run(host='0.0.0.0', port=5555, debug=True)  # Cambia 5555 por tu puerto
```

### Agregar Nuevos Usuarios

Edita el diccionario `USERS_DB` en `app.py`:
```python
USERS_DB = {
    'nuevo@company.com': {
        'password': 'contraseña',
        'nombre': 'Nombre Completo',
        'rol': 'Rol del Usuario',
        'empresa': 'Tu Empresa',
        'avatar': 'NC'
    }
}
```

### Configurar el Menú

Edita `config/menu_config.json` para:
- Cambiar la vista del menú (categoría vs roadmap)
- Agregar/eliminar casos de uso
- Modificar categorías
- Ajustar grupos de roadmap (Quick Wins vs Año 2+)

### Modificar Estilos

Los estilos están centralizados en `static/css/style.css`. Las variables CSS están al inicio del archivo:

```css
:root {
    --primary-color: #00cf4f;
    --secondary-color: #009fe3;
    --text-color: #1a1a1a;
    /* ... más variables */
}
```

## 🚀 Despliegue en Producción

### Consideraciones Importantes

1. **Cambiar la SECRET_KEY:**
```python
app.secret_key = 'tu-clave-secreta-muy-segura-aqui'
```

2. **Desactivar el modo DEBUG:**
```python
app.run(debug=False)
```

3. **Usar un servidor WSGI** como Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5555 app:app
```

4. **Configurar HTTPS** con certificados SSL

5. **Implementar base de datos real** (PostgreSQL, MySQL, MongoDB)

6. **Agregar autenticación robusta** (OAuth, SAML, 2FA)

7. **Integrar APIs reales de IA**:
   - OpenAI GPT-4 / Claude / Gemini para agentes
   - Vector databases reales (Pinecone, Weaviate)
   - Neo4j para Knowledge Graphs

## 📈 Roadmap de Funcionalidades

### Quick Wins (Implementables en Año 1)
- Monitorización de Marca
- Inteligencia Competitiva GenAI
- Generación de Contenido GenAI
- A/B Testing Automatizado
- Agentes Conversacionales

### Año 2+ Wins (Visión a Largo Plazo)
- Predicción de Abandonos
- Segmentación Avanzada
- Attribution Marketing
- Personalización de Experiencias
- Motor de Recomendaciones
- Optimización Publicitaria

## 🏗️ Stack Tecnológico

- **Backend:** Python + Flask
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Simulaciones de IA:**
  - GPT-4, Claude 3.5, Gemini 1.5 (simulados)
  - XGBoost, Random Forest, Neural Networks (simulados)
  - RAG con Pinecone, Weaviate, Chroma (simulados)
  - Knowledge Graphs con Neo4j (simulados)
  - MCP (Model Context Protocol)
  - Multi-Agent Systems (CrewAI, AutoGen)

## 📝 Licencia

Este proyecto es una demostración para fines educativos y de presentación.

## 👥 Soporte

Para más información sobre la implementación de soluciones de IA en marketing digital, contacta con tu equipo técnico.

---

**Versión:** 2.0  
**Última actualización:** Octubre 2024
