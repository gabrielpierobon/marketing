# Iberdrola AI Marketing Suite

Plataforma SaaS completa de Inteligencia Artificial para Marketing Digital en el Sector Energético.

## 🚀 Características

- **10 Casos de Uso de IA** completamente funcionales
- **Autenticación de usuarios** con sesiones seguras
- **Dashboard interactivo** con métricas en tiempo real
- **Interfaz moderna** con sidebar de navegación
- **Demos interactivos** para cada caso de uso
- **Simulación de datos realistas** sin necesidad de backend complejo
- **100% en Español** - Interfaz completamente localizada

## 📋 Casos de Uso Implementados

1. **Personalización Hiperpersonalizada** - Ofertas únicas por cliente
2. **Generación de Contenido GenAI** - Creación automática de campañas
3. **Chatbot IA Conversacional** - Asistente virtual 24/7
4. **Predicción de Churn** - Identificación de clientes en riesgo
5. **Optimización Publicitaria** - Mejora automática de campañas
6. **Segmentación Avanzada** - Agrupación inteligente de clientes
7. **A/B Testing Automatizado** - Experimentación continua
8. **Monitorización de Marca** - Análisis de sentimiento en tiempo real
9. **Motor de Recomendaciones** - Sugerencias personalizadas
10. **Attribution Marketing** - Optimización de inversión multi-touch

## 🛠️ Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o navegar al directorio del proyecto:**
```bash
cd iberdrola
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
| admin@iberdrola.com | demo2025 | Administrador |
| marketing@iberdrola.com | demo2025 | Director Marketing |
| demo@iberdrola.com | demo2025 | Analista Marketing |

## 📁 Estructura del Proyecto

```
iberdrola/
├── app.py                          # Aplicación Flask principal
├── requirements.txt                # Dependencias Python
├── README.md                       # Este archivo
├── templates/                      # Plantillas HTML
│   ├── base.html                  # Template base
│   ├── login.html                 # Página de login
│   ├── dashboard.html             # Dashboard principal
│   ├── personalizacion.html       # Caso de uso 1
│   ├── contenido_genai.html       # Caso de uso 2
│   ├── chatbot.html               # Caso de uso 3
│   ├── prediccion_churn.html      # Caso de uso 4
│   ├── optimizacion_publicitaria.html  # Caso de uso 5
│   ├── segmentacion_avanzada.html # Caso de uso 6
│   ├── ab_testing.html            # Caso de uso 7
│   ├── monitorizacion_marca.html  # Caso de uso 8
│   ├── motor_recomendaciones.html # Caso de uso 9
│   ├── attribution_marketing.html # Caso de uso 10
│   ├── configuracion.html         # Configuración
│   ├── 404.html                   # Error 404
│   └── 500.html                   # Error 500
└── static/                         # Archivos estáticos
    ├── css/
    │   └── style.css              # Estilos CSS
    ├── js/
    │   └── main.js                # JavaScript principal
    └── img/                        # Imágenes (vacío por ahora)
```

## 🎯 Características Técnicas

### Backend (Flask)
- **Autenticación basada en sesiones** con Flask sessions
- **Rutas RESTful** para cada caso de uso
- **APIs JSON** para interacciones dinámicas
- **Simulación de datos** realista sin necesidad de base de datos
- **Manejo de errores** con páginas 404 y 500 personalizadas

### Frontend
- **Diseño responsive** que funciona en móviles, tablets y desktop
- **Sidebar fijo** con navegación intuitiva
- **Animaciones suaves** con CSS transitions
- **Componentes interactivos** con JavaScript vanilla
- **Interfaz moderna** inspirada en Microsoft Fluent Design

### Seguridad
- **Sesiones seguras** con secret key
- **Decorador @login_required** para proteger rutas
- **Validación de formularios** en cliente y servidor
- **Preparado para ISO/IEC 42001** (mencionado en la interfaz)

## 📊 Métricas y KPIs

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
    'nuevo@iberdrola.com': {
        'password': 'contraseña',
        'nombre': 'Nombre Completo',
        'rol': 'Rol del Usuario',
        'empresa': 'Iberdrola España',
        'avatar': 'NC'
    }
}
```

### Modificar Estilos

Los estilos están centralizados en `static/css/style.css`. Las variables CSS están al inicio del archivo:

```css
:root {
    --primary: #0078D4;
    --success: #107C10;
    --warning: #FFB900;
    --danger: #D13438;
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

5. **Implementar base de datos real** (PostgreSQL, MySQL, etc.)

6. **Agregar autenticación robusta** (OAuth, 2FA, etc.)

## 📈 Próximas Mejoras

- [ ] Integración con base de datos real
- [ ] APIs reales de IA (OpenAI, Claude, Gemini)
- [ ] Exportación de reportes en PDF
- [ ] Gráficos interactivos con Chart.js
- [ ] Notificaciones en tiempo real con WebSockets
- [ ] Multi-idioma (English, Português)
- [ ] Modo oscuro
- [ ] Panel de administración avanzado

## 📝 Licencia

Este proyecto es una demostración para fines educativos y de presentación.

## 👥 Contacto

Para más información sobre la implementación de soluciones de IA en marketing digital para el sector energético, contacta con el equipo de Capgemini.

---

**© 2025 Iberdrola AI Marketing Suite**  
*Powered by Azure AI, Google Vertex AI & Salesforce Agentforce*
