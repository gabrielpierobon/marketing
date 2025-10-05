"""
Iberdrola AI Marketing Suite - Plataforma SaaS
Sistema completo de IA para marketing digital en el sector energético
"""

from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from functools import wraps
from datetime import datetime, timedelta
import random
import json
import os

app = Flask(__name__)
app.secret_key = 'iberdrola-ai-suite-2025-secret-key-change-in-production'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)

# Cargar configuración del menú
def load_menu_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'menu_config.json')
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Configuración por defecto si no existe el archivo
        return {"categories": [], "dashboard": {}, "configuracion": {}}

MENU_CONFIG = load_menu_config()

# Función helper para obtener el título de página según el endpoint
def get_page_title(endpoint):
    # Buscar en dashboard
    if endpoint == 'dashboard':
        return MENU_CONFIG.get('dashboard', {}).get('page_title', 'Dashboard Principal')
    
    # Buscar en configuración
    if endpoint == 'configuracion':
        return MENU_CONFIG.get('configuracion', {}).get('page_title', 'Configuración')
    
    # Buscar en integración de datos
    if endpoint == 'integracion_datos':
        return MENU_CONFIG.get('integracion_datos', {}).get('page_title', 'Integración de Datos')
    
    # Buscar en integración de APIs
    if endpoint == 'integracion_apis':
        return MENU_CONFIG.get('integracion_apis', {}).get('page_title', 'Integración de APIs')
    
    # Buscar en laboratorio
    if endpoint == 'laboratorio':
        return MENU_CONFIG.get('laboratorio', {}).get('page_title', 'Laboratorio')
    
    # Buscar en monitorización
    if endpoint == 'monitorizacion':
        return MENU_CONFIG.get('monitorizacion', {}).get('page_title', 'Monitorización')
    
    # Buscar en introducción
    if endpoint == 'introduccion':
        return MENU_CONFIG.get('introduccion', {}).get('page_title', 'Introducción')
    
    # Buscar en categorías
    for category in MENU_CONFIG.get('categories', []):
        for item in category.get('menu_items', []):
            if item.get('endpoint') == endpoint:
                return item.get('page_title', '')
    
    return 'Iberdrola AI'

# Context processor para hacer disponible la configuración en todos los templates
@app.context_processor
def inject_menu_config():
    return {
        'menu_config': MENU_CONFIG,
        'get_page_title': get_page_title
    }

# Simulación de base de datos de usuarios
USERS_DB = {
    'admin@iberdrola.com': {
        'password': 'demo2025',
        'nombre': 'María García',
        'rol': 'Administrador',
        'empresa': 'Iberdrola España',
        'avatar': 'MG'
    },
    'marketing@iberdrola.com': {
        'password': 'demo2025',
        'nombre': 'Carlos Rodríguez',
        'rol': 'Director Marketing',
        'empresa': 'Iberdrola España',
        'avatar': 'CR'
    },
    'demo@iberdrola.com': {
        'password': 'demo2025',
        'nombre': 'Ana Martínez',
        'rol': 'Analista Marketing',
        'empresa': 'Iberdrola España',
        'avatar': 'AM'
    }
}

# Decorador para requerir login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            flash('Por favor, inicia sesión para acceder a la plataforma.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ==================== RUTAS DE AUTENTICACIÓN ====================

@app.route('/')
def index():
    if 'user_email' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email in USERS_DB and USERS_DB[email]['password'] == password:
            session.permanent = True
            session['user_email'] = email
            session['user_name'] = USERS_DB[email]['nombre']
            session['user_rol'] = USERS_DB[email]['rol']
            session['user_avatar'] = USERS_DB[email]['avatar']
            flash(f'¡Bienvenido/a, {USERS_DB[email]["nombre"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas. Intenta de nuevo.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('login'))

# ==================== DASHBOARD PRINCIPAL ====================

@app.route('/dashboard')
@login_required
def dashboard():
    # Métricas generales simuladas
    metrics = {
        'clientes_activos': 11_234_567,
        'campanas_activas': 47,
        'roi_promedio': 5.8,
        'ahorro_mensual': 142_580,
        'engagement_rate': 42.3,
        'churn_reduccion': 18.5,
        'leads_generados': 8_947,
        'conversion_rate': 34.2
    }
    
    # Actividad reciente
    actividades = [
        {'tipo': 'success', 'icono': '✅', 'titulo': 'Campaña Solar optimizada', 'descripcion': 'ROI aumentado +23% en últimas 48h', 'tiempo': 'Hace 15 min'},
        {'tipo': 'info', 'icono': '🤖', 'titulo': 'Chatbot procesó 1,247 consultas', 'descripcion': 'Satisfacción promedio: 4.8/5', 'tiempo': 'Hace 1 hora'},
        {'tipo': 'warning', 'icono': '⚠️', 'titulo': '12 clientes en riesgo alto detectados', 'descripcion': 'Campañas de retención activadas automáticamente', 'tiempo': 'Hace 2 horas'},
        {'tipo': 'success', 'icono': '📧', 'titulo': 'Email masivo enviado', 'descripcion': '45,230 emails personalizados - Open rate: 67%', 'tiempo': 'Hace 3 horas'},
        {'tipo': 'info', 'icono': '📊', 'titulo': 'Informe semanal generado', 'descripcion': 'Análisis de rendimiento disponible', 'tiempo': 'Hace 5 horas'}
    ]
    
    return render_template('dashboard.html', metrics=metrics, actividades=actividades)

# ==================== CASO DE USO 1: PERSONALIZACIÓN ====================

@app.route('/personalizacion')
@login_required
def personalizacion():
    return render_template('personalizacion.html')

@app.route('/api/generar-oferta', methods=['POST'])
@login_required
def generar_oferta():
    data = request.get_json()
    perfil = data.get('perfil', 'residencial')
    
    ofertas = {
        'residencial': {
            'cliente': {
                'nombre': 'María Rodríguez',
                'avatar': 'MR',
                'segmento': 'Residencial Alto Consumo',
                'consumo': '485 kWh/mes',
                'vivienda': 'Casa Unifamiliar',
                'potencial_solar': '8.5 kW',
                'ahorro_estimado': '€1,240/año'
            },
            'oferta': {
                'titulo': '🌞 Oferta Personalizada: Instalación Solar Premium',
                'descripcion': 'Hemos analizado tu consumo de los últimos 12 meses (promedio 485 kWh/mes) y tenemos excelentes noticias: tu vivienda es ideal para energía solar.',
                'beneficios': [
                    'Sistema solar 8.5 kW (25 paneles de alta eficiencia)',
                    'Ahorro estimado: €1,240/año (€103/mes)',
                    'ROI en 6.8 años - Batería de respaldo incluida',
                    'Financiación 0% durante 24 meses',
                    'Instalación en 3 días - Garantía 25 años'
                ],
                'cta': 'Solicitar Evaluación Gratuita',
                'validez': '15 de Noviembre 2025',
                'color': 'blue'
            }
        },
        'negocio': {
            'cliente': {
                'nombre': 'Restaurante Casa López',
                'avatar': 'RC',
                'segmento': 'PYME - Hostelería',
                'consumo': '2,450 kWh/mes',
                'sector': 'Restauración',
                'pico_consumo': '20:00-23:00h',
                'ahorro_potencial': '€420/mes'
            },
            'oferta': {
                'titulo': '⚡ Plan Optimización Energética PYME',
                'descripcion': 'Nuestro análisis IA detecta que su negocio podría reducir costes energéticos en €420/mes con nuestro plan de optimización para restaurantes.',
                'beneficios': [
                    'Tarifa flexible horaria optimizada para hostelería',
                    'Sistema de gestión energética inteligente',
                    'Iluminación LED profesional (cocina + sala)',
                    'Optimización climatización (reducción 30% consumo)',
                    'Monitorización consumo en tiempo real'
                ],
                'cta': 'Agendar Consultoría Gratuita',
                'validez': 'Inversión inicial: €0 - Ahorro desde el primer mes',
                'color': 'green'
            }
        },
        'alto-consumo': {
            'cliente': {
                'nombre': 'Familia Iglesias',
                'avatar': 'FI',
                'segmento': 'Residencial Alto Consumo Verano',
                'consumo': '780 kWh/mes (verano)',
                'equipamiento': 'A/C, Piscina',
                'patron': 'Picos diurnos',
                'ahorro_potencial': '€185/mes'
            },
            'oferta': {
                'titulo': '🏊 Paquete Confort Verano Inteligente',
                'descripcion': 'Hemos detectado picos de consumo en verano (hasta 780 kWh/mes) relacionados con climatización y piscina. Tenemos la solución perfecta para mantener su confort ahorrando €185/mes.',
                'beneficios': [
                    'Bomba de calor piscina eficiencia A+++ (ahorro 60%)',
                    'Sistema domótica control A/C por zonas',
                    'Tarifa super valle para cargar piscina (madrugada)',
                    'App móvil: control consumo en tiempo real',
                    'Alertas inteligentes de optimización'
                ],
                'cta': 'Activar Oferta Especial',
                'validez': 'Promoción: 40% descuento instalación',
                'color': 'orange'
            }
        }
    }
    
    return jsonify(ofertas.get(perfil, ofertas['residencial']))

# ==================== CASO DE USO 2: CONTENIDO GENAI ====================

@app.route('/contenido-genai')
@login_required
def contenido_genai():
    # Casos de uso de generación de contenido
    casos_uso = [
        {
            'id': 'email-campaigns',
            'nombre': 'Campañas de Email',
            'icono': '📧',
            'descripcion': 'Genera emails personalizados con subject lines optimizados',
            'uso_mensual': 3420,
            'tiempo_ahorro': '85%',
            'color': '#0078D4'
        },
        {
            'id': 'social-media',
            'nombre': 'Posts Redes Sociales',
            'icono': '📱',
            'descripcion': 'Crea posts para LinkedIn, Twitter, Facebook e Instagram',
            'uso_mensual': 5680,
            'tiempo_ahorro': '90%',
            'color': '#107C10'
        },
        {
            'id': 'landing-pages',
            'nombre': 'Landing Pages',
            'icono': '🌐',
            'descripcion': 'Copy persuasivo para landing pages de conversión',
            'uso_mensual': 890,
            'tiempo_ahorro': '80%',
            'color': '#FFB900'
        },
        {
            'id': 'blog-articles',
            'nombre': 'Artículos de Blog',
            'icono': '📝',
            'descripcion': 'Artículos SEO-optimizados de 1000-2000 palabras',
            'uso_mensual': 1240,
            'tiempo_ahorro': '75%',
            'color': '#D13438'
        },
        {
            'id': 'video-scripts',
            'nombre': 'Guiones para Video',
            'icono': '🎬',
            'descripcion': 'Scripts para spots publicitarios y videos corporativos',
            'uso_mensual': 450,
            'tiempo_ahorro': '70%',
            'color': '#8E24AA'
        },
        {
            'id': 'press-releases',
            'nombre': 'Notas de Prensa',
            'icono': '📰',
            'descripcion': 'Comunicados de prensa profesionales',
            'uso_mensual': 280,
            'tiempo_ahorro': '65%',
            'color': '#00B7C3'
        }
    ]
    
    # Métricas globales
    metricas = {
        'contenido_generado_mes': 12960,
        'tiempo_ahorro_horas': 2340,
        'coste_ahorro': 145000,
        'score_calidad': 91
    }
    
    return render_template('contenido_genai.html', 
                         casos_uso=casos_uso,
                         metricas=metricas)

@app.route('/api/generar-contenido', methods=['POST'])
@login_required
def generar_contenido():
    data = request.get_json()
    objetivo = data.get('objetivo', 'solar')
    tono = data.get('tono', 'profesional')
    
    contenidos = {
        'solar': {
            'asunto': '🌞 Descubre cuánto puedes ahorrar con energía solar' if tono == 'profesional' else '⚡ ÚLTIMOS DÍAS: Ahorra hasta €1,500/año con Solar',
            'cuerpo': '''Estimado cliente,

La energía solar nunca ha sido tan accesible. Nuestro sistema de última generación se adapta perfectamente a tu consumo actual, permitiéndote generar tu propia electricidad y reducir drásticamente tu factura.

Con nuestro análisis personalizado gratuito, descubrirás:
• El sistema solar ideal para tu hogar
• Tu ahorro exacto mes a mes
• Financiación sin entrada y a tu medida
• Instalación profesional en solo 3 días

Más de 50,000 familias ya están ahorrando con Iberdrola Solar.''',
            'cta': '👉 Calcula tu ahorro en 2 minutos - Sin compromiso',
            'variaciones': 5,
            'score_predicho': 94
        },
        'retencion': {
            'asunto': '💙 Te echamos de menos - Vuelve con ventajas exclusivas',
            'cuerpo': '''Hola,

Hemos notado que estás considerando otras opciones energéticas. Queremos asegurarnos de que estás recibiendo el mejor servicio posible.

Como cliente valorado, hemos preparado una oferta especial solo para ti:
• Revisión completa de tu tarifa actual
• Optimización personalizada de tu plan
• 3 meses con precio preferente
• Atención prioritaria 24/7

Tu satisfacción es nuestra prioridad. Déjanos demostrarte por qué miles de clientes confían en Iberdrola.''',
            'cta': '📞 Habla con tu gestor personal ahora',
            'variaciones': 8,
            'score_predicho': 87
        },
        'eficiencia': {
            'asunto': '💡 5 formas de reducir tu factura eléctrica este mes',
            'cuerpo': '''Hola,

¿Sabías que puedes reducir tu consumo energético hasta un 30% sin cambiar tus hábitos?

Te compartimos 5 consejos profesionales que marcan la diferencia:
1. Optimiza el uso de electrodomésticos en horas valle
2. Ajusta la temperatura del termostato 2°C
3. Aprovecha la luz natural al máximo
4. Desconecta dispositivos en standby
5. Considera cambiar a iluminación LED

Además, nuestra app te muestra tu consumo en tiempo real y te sugiere mejoras personalizadas cada semana.''',
            'cta': '📱 Descarga la app y empieza a ahorrar hoy',
            'variaciones': 12,
            'score_predicho': 91
        },
        'demand-response': {
            'asunto': '⚡ Gana dinero reduciendo tu consumo en horas pico',
            'cuerpo': '''Hola,

Te presentamos nuestro nuevo programa Demand Response: una forma inteligente de ahorrar dinero mientras ayudas al medio ambiente.

¿Cómo funciona?
• Recibes alertas cuando la red necesita reducir demanda
• Reduces consumo voluntariamente durante 1-2 horas
• Ganas recompensas por cada kWh reducido
• Todo automatizado con tu termostato inteligente

Clientes actuales están ganando €15-40/mes adicionales sin esfuerzo.''',
            'cta': '🎯 Únete al programa Demand Response',
            'variaciones': 6,
            'score_predicho': 89
        }
    }
    
    resultado = contenidos.get(objetivo, contenidos['solar'])
    resultado['tiempo_generacion'] = round(random.uniform(1.2, 2.8), 1)
    resultado['palabras'] = len(resultado['cuerpo'].split())
    
    return jsonify(resultado)

# ==================== CASO DE USO 3: CHATBOT ====================

@app.route('/chatbot')
@login_required
def chatbot():
    # Simulación de chatbots activos
    chatbots_activos = [
        {
            'id': 'CB-001',
            'nombre': 'Asistente Atención Cliente',
            'tipo': 'Asistente con IA Generativa',
            'tipo_corto': 'GenAI',
            'estado': 'activo',
            'conversaciones_mes': 45230,
            'satisfaccion': 4.7,
            'resolucion_automatica': 82,
            'tiempo_respuesta': '1.2s',
            'idiomas': ['ES', 'EN', 'PT'],
            'canales': ['Web', 'WhatsApp', 'App'],
            'fecha_creacion': '15 Ene 2024',
            'ultima_actualizacion': 'Hace 2 horas'
        },
        {
            'id': 'CB-002',
            'nombre': 'Consultas Facturación',
            'tipo': 'Chatbot Basado en Flujos',
            'tipo_corto': 'Flujos',
            'estado': 'activo',
            'conversaciones_mes': 28450,
            'satisfaccion': 4.3,
            'resolucion_automatica': 91,
            'tiempo_respuesta': '0.3s',
            'idiomas': ['ES'],
            'canales': ['Web', 'App'],
            'fecha_creacion': '03 Dic 2023',
            'ultima_actualizacion': 'Hace 1 día'
        },
        {
            'id': 'CB-003',
            'nombre': 'Asesor Energía Solar',
            'tipo': 'Agente',
            'tipo_corto': 'Agente',
            'estado': 'activo',
            'conversaciones_mes': 12890,
            'satisfaccion': 4.8,
            'resolucion_automatica': 76,
            'tiempo_respuesta': '2.1s',
            'idiomas': ['ES', 'EN'],
            'canales': ['Web', 'WhatsApp'],
            'fecha_creacion': '22 Feb 2024',
            'ultima_actualizacion': 'Hace 3 horas'
        },
        {
            'id': 'CB-004',
            'nombre': 'Sistema Soporte Técnico',
            'tipo': 'Sistema Multiagente',
            'tipo_corto': 'Multi-Agent',
            'estado': 'activo',
            'conversaciones_mes': 18670,
            'satisfaccion': 4.6,
            'resolucion_automatica': 68,
            'tiempo_respuesta': '3.5s',
            'idiomas': ['ES', 'EN', 'PT', 'FR'],
            'canales': ['Web', 'App', 'Telegram'],
            'fecha_creacion': '10 Mar 2024',
            'ultima_actualizacion': 'Hace 30 min'
        },
        {
            'id': 'CB-005',
            'nombre': 'Ventas B2B Empresas',
            'tipo': 'Sistema Multiagente con Orquestador',
            'tipo_corto': 'Orquestador',
            'estado': 'desarrollo',
            'conversaciones_mes': 2340,
            'satisfaccion': 4.5,
            'resolucion_automatica': 58,
            'tiempo_respuesta': '4.2s',
            'idiomas': ['ES', 'EN'],
            'canales': ['Web'],
            'fecha_creacion': '05 Abr 2024',
            'ultima_actualizacion': 'Hace 15 min'
        }
    ]
    
    # Métricas globales
    metricas_globales = {
        'total_conversaciones': 107580,
        'satisfaccion_promedio': 4.58,
        'resolucion_automatica': 75,
        'ahorro_mensual': 145000,
        'chatbots_activos': 4,
        'chatbots_desarrollo': 1
    }
    
    return render_template('chatbot.html', 
                         chatbots=chatbots_activos,
                         metricas=metricas_globales)

@app.route('/api/chatbot', methods=['POST'])
@login_required
def chatbot_respuesta():
    data = request.get_json()
    mensaje = data.get('mensaje', '').lower()
    
    respuestas = {
        'consumo': {
            'texto': '📊 Tu consumo este mes es de <strong>342 kWh</strong>, un 8% menos que el mes pasado. ¡Excelente trabajo! ¿Te gustaría ver consejos personalizados para reducirlo aún más?',
            'acciones': ['Ver desglose detallado', 'Consejos de ahorro', 'Comparar con vecinos']
        },
        'solar': {
            'texto': '🌞 ¡Excelente decisión! La instalación solar puede ahorrarte hasta <strong>€1,200/año</strong>. Te he enviado una simulación personalizada a tu email. ¿Quieres que te contacte un especialista?',
            'acciones': ['Agendar consulta', 'Ver simulación', 'Opciones de financiación']
        },
        'factura': {
            'texto': '📄 Tu última factura es de <strong>€89.50</strong> (periodo 1-30 Oct). Puedes descargarla desde tu área de cliente o te la envío por email. ¿Qué prefieres?',
            'acciones': ['Descargar PDF', 'Enviar por email', 'Ver histórico']
        },
        'averia': {
            'texto': '⚠️ Lamento el inconveniente. He registrado tu incidencia con el código <strong>#IB-2847</strong>. Un técnico te contactará en las próximas 2 horas. ¿Hay algo más que pueda ayudarte?',
            'acciones': ['Ver estado incidencia', 'Hablar con técnico', 'Reportar otra avería']
        },
        'ahorro': {
            'texto': '💡 Basándome en tu perfil, puedes ahorrar <strong>€45/mes</strong> cambiando a nuestra tarifa flexible y optimizando el uso de electrodomésticos. ¿Te genero un plan personalizado?',
            'acciones': ['Generar plan', 'Ver tarifas', 'Calcular ahorro']
        },
        'default': {
            'texto': '🤖 Entiendo tu consulta. Permíteme ayudarte con eso. Te recomiendo:<br><br>• Revisar tu área de cliente<br>• Contactar con atención al cliente: 900 123 456<br>• Visitar nuestras FAQs<br><br>¿Hay algo específico en lo que pueda ayudarte?',
            'acciones': ['Hablar con agente', 'Ver FAQs', 'Área de cliente']
        }
    }
    
    # Detectar intención
    respuesta = respuestas['default']
    if 'consumo' in mensaje:
        respuesta = respuestas['consumo']
    elif 'solar' in mensaje or 'paneles' in mensaje:
        respuesta = respuestas['solar']
    elif 'factura' in mensaje:
        respuesta = respuestas['factura']
    elif 'averia' in mensaje or 'incidencia' in mensaje or 'problema' in mensaje:
        respuesta = respuestas['averia']
    elif 'ahorrar' in mensaje or 'reducir' in mensaje:
        respuesta = respuestas['ahorro']
    
    return jsonify(respuesta)

# ==================== CASO DE USO 4: PREDICCIÓN CHURN ====================

@app.route('/prediccion-churn')
@login_required
def prediccion_churn():
    # Clientes en riesgo de churn
    clientes_riesgo = [
        {
            'id': 'CL-28492',
            'nombre': 'Juan Martínez García',
            'segmento': 'Familias Jóvenes',
            'score_churn': 87,
            'nivel_riesgo': 'alto',
            'ltv': 4280,
            'antiguedad': 2.3,
            'consumo_mensual': 245,
            'factores_riesgo': [
                {'factor': 'Quejas recientes', 'impacto': 35, 'descripcion': '2 quejas en último mes sobre facturación'},
                {'factor': 'Reducción consumo', 'impacto': 28, 'descripcion': '-15% consumo vs trimestre anterior'},
                {'factor': 'Competencia contactó', 'impacto': 24, 'descripcion': 'Llamada de Endesa detectada'}
            ],
            'acciones_recomendadas': [
                {'accion': 'Llamada retención urgente', 'prioridad': 'alta', 'probabilidad_exito': 68},
                {'accion': 'Descuento 15% próximos 3 meses', 'prioridad': 'alta', 'probabilidad_exito': 72},
                {'accion': 'Upgrade a plan premium sin coste', 'prioridad': 'media', 'probabilidad_exito': 58}
            ],
            'ultima_interaccion': 'Hace 45 días',
            'canal_preferido': 'Email',
            'satisfaccion': 4.2
        },
        {
            'id': 'CL-19283',
            'nombre': 'Ana Castro López',
            'segmento': 'PYME Eficiencia',
            'score_churn': 78,
            'nivel_riesgo': 'alto',
            'ltv': 12420,
            'antiguedad': 5.8,
            'consumo_mensual': 1150,
            'factores_riesgo': [
                {'factor': 'Precio competencia', 'impacto': 42, 'descripcion': 'Competencia ofrece -12% vs nuestra tarifa'},
                {'factor': 'Fin contrato próximo', 'impacto': 36, 'descripcion': 'Contrato vence en 45 días'}
            ],
            'acciones_recomendadas': [
                {'accion': 'Oferta renovación anticipada -10%', 'prioridad': 'alta', 'probabilidad_exito': 75},
                {'accion': 'Auditoría energética gratuita', 'prioridad': 'alta', 'probabilidad_exito': 68},
                {'accion': 'Account manager dedicado', 'prioridad': 'media', 'probabilidad_exito': 62}
            ],
            'ultima_interaccion': 'Hace 12 días',
            'canal_preferido': 'Teléfono',
            'satisfaccion': 6.8
        },
        {
            'id': 'CL-31847',
            'nombre': 'Pedro Sánchez Ruiz',
            'segmento': 'Eco-Conscious Premium',
            'score_churn': 65,
            'nivel_riesgo': 'medio',
            'ltv': 8890,
            'antiguedad': 4.2,
            'consumo_mensual': 380,
            'factores_riesgo': [
                {'factor': 'Interés en competencia', 'impacto': 38, 'descripcion': 'Visitó web de Naturgy 3 veces'},
                {'factor': 'Engagement bajo', 'impacto': 27, 'descripcion': 'No abre emails desde hace 2 meses'}
            ],
            'acciones_recomendadas': [
                {'accion': 'Oferta solar personalizada', 'prioridad': 'alta', 'probabilidad_exito': 71},
                {'accion': 'Invitación evento sostenibilidad', 'prioridad': 'media', 'probabilidad_exito': 64},
                {'accion': 'Certificado huella carbono gratis', 'prioridad': 'media', 'probabilidad_exito': 58}
            ],
            'ultima_interaccion': 'Hace 28 días',
            'canal_preferido': 'App móvil',
            'satisfaccion': 7.5
        },
        {
            'id': 'CL-24891',
            'nombre': 'Laura Fernández Díaz',
            'segmento': 'Familias Jóvenes',
            'score_churn': 52,
            'nivel_riesgo': 'medio',
            'ltv': 3120,
            'antiguedad': 1.8,
            'consumo_mensual': 210,
            'factores_riesgo': [
                {'factor': 'Precio sensible', 'impacto': 32, 'descripcion': 'Segmento con alta elasticidad precio'},
                {'factor': 'Baja antigüedad', 'impacto': 20, 'descripcion': 'Clientes <2 años tienen 2x churn'}
            ],
            'acciones_recomendadas': [
                {'accion': 'Plan ahorro familiar -8%', 'prioridad': 'media', 'probabilidad_exito': 66},
                {'accion': 'App gamificación ahorro', 'prioridad': 'media', 'probabilidad_exito': 59},
                {'accion': 'Programa referidos con bonus', 'prioridad': 'baja', 'probabilidad_exito': 48}
            ],
            'ultima_interaccion': 'Hace 8 días',
            'canal_preferido': 'WhatsApp',
            'satisfaccion': 7.1
        },
        {
            'id': 'CL-09471',
            'nombre': 'Carlos López Martín',
            'segmento': 'Propietarios Vehículo Eléctrico',
            'score_churn': 38,
            'nivel_riesgo': 'bajo',
            'ltv': 9850,
            'antiguedad': 3.5,
            'consumo_mensual': 520,
            'factores_riesgo': [
                {'factor': 'Tarifa no optimizada', 'impacto': 25, 'descripcion': 'No tiene tarifa específica EV'},
                {'factor': 'Competencia con mejor oferta', 'impacto': 13, 'descripcion': 'Endesa ofrece tarifa EV más competitiva'}
            ],
            'acciones_recomendadas': [
                {'accion': 'Migración a Tarifa Super Valle EV', 'prioridad': 'alta', 'probabilidad_exito': 82},
                {'accion': 'Oferta wallbox con descuento', 'prioridad': 'media', 'probabilidad_exito': 68},
                {'accion': 'Programa fidelización EV', 'prioridad': 'baja', 'probabilidad_exito': 54}
            ],
            'ultima_interaccion': 'Hace 5 días',
            'canal_preferido': 'App móvil',
            'satisfaccion': 8.2
        },
        {
            'id': 'CL-15678',
            'nombre': 'María González Pérez',
            'segmento': 'Seniors Tradicionales',
            'score_churn': 18,
            'nivel_riesgo': 'bajo',
            'ltv': 6200,
            'antiguedad': 18.5,
            'consumo_mensual': 195,
            'factores_riesgo': [
                {'factor': 'Edad avanzada', 'impacto': 12, 'descripcion': 'Posible cambio de residencia o fallecimiento'},
                {'factor': 'Consumo descendente', 'impacto': 6, 'descripcion': '-8% consumo anual'}
            ],
            'acciones_recomendadas': [
                {'accion': 'Llamada bienestar cliente', 'prioridad': 'baja', 'probabilidad_exito': 75},
                {'accion': 'Servicio atención premium', 'prioridad': 'baja', 'probabilidad_exito': 68},
                {'accion': 'Descuento fidelidad', 'prioridad': 'baja', 'probabilidad_exito': 62}
            ],
            'ultima_interaccion': 'Hace 3 días',
            'canal_preferido': 'Teléfono',
            'satisfaccion': 8.8
        }
    ]
    
    # Métricas globales
    metricas = {
        'clientes_riesgo_alto': 2340,
        'clientes_riesgo_medio': 8920,
        'clientes_riesgo_bajo': 12450,
        'tasa_churn_actual': 3.8,
        'tasa_churn_predicha': 4.2,
        'revenue_en_riesgo': 2840000,
        'precision_modelo': 89,
        'recall_modelo': 84,
        'clientes_salvados_mes': 1847
    }
    
    # Factores de churn más comunes
    factores_principales = [
        {'factor': 'Precio competencia', 'frecuencia': 42, 'impacto_promedio': 38},
        {'factor': 'Quejas no resueltas', 'frecuencia': 35, 'impacto_promedio': 45},
        {'factor': 'Fin de contrato', 'frecuencia': 28, 'impacto_promedio': 52},
        {'factor': 'Reducción consumo', 'frecuencia': 24, 'impacto_promedio': 28},
        {'factor': 'Baja satisfacción', 'frecuencia': 22, 'impacto_promedio': 41}
    ]
    
    return render_template('prediccion_churn.html',
                         clientes=clientes_riesgo,
                         metricas=metricas,
                         factores_principales=factores_principales)

@app.route('/api/analizar-churn/<cliente_id>')
@login_required
def analizar_churn(cliente_id):
    analisis = {
        'CL-28492': {
            'cliente': {
                'nombre': 'Juan Martínez',
                'avatar': 'JM',
                'antiguedad': '3 años',
                'id': 'CL-28492',
                'riesgo': 87,
                'nivel': 'alto'
            },
            'factores': [
                '3 contactos al servicio de atención en último mes',
                '2 quejas sobre facturación no resueltas',
                'Reducción consumo 35% últimos 2 meses',
                'No ha abierto últimos 5 emails',
                'Búsquedas web de competidores detectadas'
            ],
            'acciones': [
                'Contacto inmediato gestor personal (llamada programada 14:30 hoy)',
                'Oferta retención enviada (descuento 20% próximos 6 meses)',
                'Revisión gratuita instalación eléctrica programada',
                'Email personalizado CEO disculpándose por inconvenientes'
            ],
            'probabilidad_retencion': 73,
            'valor_lifetime': 4280,
            'coste_retencion': 145,
            'roi': '29:1'
        },
        'CL-19283': {
            'cliente': {
                'nombre': 'Ana Castro',
                'avatar': 'AC',
                'antiguedad': '5 años',
                'id': 'CL-19283',
                'riesgo': 42,
                'nivel': 'medio'
            },
            'factores': [
                'Engagement reducido - No interacción últimas 3 campañas',
                'Consumo estable pero no ha actualizado datos en 18 meses',
                'Tarifa subóptima - Pagaría €23/mes menos con plan flexible',
                'No usa app móvil ni área cliente online'
            ],
            'acciones': [
                'Email personalizado: "Ana, estás pagando de más - te mostramos cómo ahorrar €276/año"',
                'Incentivo: 3 meses descuento 15% al cambiar a tarifa optimizada',
                'Onboarding app: Tutorial personalizado + €10 primer uso',
                'Follow-up: Informe mensual ahorro conseguido'
            ],
            'probabilidad_retencion': 85,
            'valor_lifetime': 6420,
            'coste_retencion': 35,
            'roi': '183:1'
        },
        'CL-09471': {
            'cliente': {
                'nombre': 'Laura Gómez',
                'avatar': 'LG',
                'antiguedad': '8 años',
                'id': 'CL-09471',
                'riesgo': 12,
                'nivel': 'bajo'
            },
            'factores': [
                'NPS: 9/10 - Recomendó Iberdrola a 3 familiares',
                'Engagement alto - Abre 80% emails, usa app semanalmente',
                'Consumo creciente - Añadió carga coche eléctrico',
                'Tarifa óptima - Plan flexible ajustado a su perfil',
                'Sin incidencias - 0 contactos soporte en 12 meses'
            ],
            'acciones': [
                'Solar + Batería: Probabilidad conversión 68% (€18K potencial)',
                'Smart Home: Probabilidad 52% (termostato + enchufes inteligentes)',
                'Plan EV Premium: Probabilidad 78% (tarifa súper valle optimizada)',
                'Programa Referidos: Candidata ideal - incentivo €100 por referido'
            ],
            'probabilidad_retencion': 96,
            'valor_lifetime': 12850,
            'coste_retencion': 0,
            'roi': 'N/A - Cliente fidelizado'
        }
    }
    
    return jsonify(analisis.get(cliente_id, analisis['CL-28492']))

# ==================== CASO DE USO 5: OPTIMIZACIÓN PUBLICITARIA ====================

@app.route('/optimizacion-publicitaria')
@login_required
def optimizacion_publicitaria():
    # Campañas activas por plataforma
    campanas = [
        {
            'id': 'CAMP-001',
            'nombre': 'Solar Residencial Q4',
            'plataforma': 'Google Ads',
            'tipo': 'Search',
            'estado': 'activa',
            'presupuesto_diario': 500,
            'gasto_actual': 12450,
            'impresiones': 1247890,
            'clicks': 34521,
            'ctr': 2.77,
            'conversiones': 892,
            'cvr': 2.58,
            'cpa': 13.95,
            'roas': 4.8,
            'optimizaciones_aplicadas': 23,
            'ultima_optimizacion': 'Hace 2 horas'
        },
        {
            'id': 'CAMP-002',
            'nombre': 'Retención Clientes',
            'plataforma': 'Meta',
            'tipo': 'Facebook/Instagram',
            'estado': 'activa',
            'presupuesto_diario': 350,
            'gasto_actual': 8920,
            'impresiones': 892450,
            'clicks': 28934,
            'ctr': 3.24,
            'conversiones': 567,
            'cvr': 1.96,
            'cpa': 15.73,
            'roas': 3.6,
            'optimizaciones_aplicadas': 18,
            'ultima_optimizacion': 'Hace 4 horas'
        },
        {
            'id': 'CAMP-003',
            'nombre': 'PYME Eficiencia Energética',
            'plataforma': 'LinkedIn',
            'tipo': 'Sponsored Content',
            'estado': 'activa',
            'presupuesto_diario': 400,
            'gasto_actual': 10240,
            'impresiones': 456780,
            'clicks': 15678,
            'ctr': 3.43,
            'conversiones': 423,
            'cvr': 2.70,
            'cpa': 24.21,
            'roas': 5.2,
            'optimizaciones_aplicadas': 15,
            'ultima_optimizacion': 'Hace 1 hora'
        },
        {
            'id': 'CAMP-004',
            'nombre': 'EV Charging Awareness',
            'plataforma': 'Google Ads',
            'tipo': 'Display',
            'estado': 'activa',
            'presupuesto_diario': 300,
            'gasto_actual': 7680,
            'impresiones': 2345670,
            'clicks': 18920,
            'ctr': 0.81,
            'conversiones': 234,
            'cvr': 1.24,
            'cpa': 32.82,
            'roas': 2.9,
            'optimizaciones_aplicadas': 12,
            'ultima_optimizacion': 'Hace 6 horas'
        },
        {
            'id': 'CAMP-005',
            'nombre': 'Smart Home Bundle',
            'plataforma': 'Meta',
            'tipo': 'Facebook/Instagram',
            'estado': 'revision',
            'presupuesto_diario': 250,
            'gasto_actual': 6340,
            'impresiones': 567890,
            'clicks': 12456,
            'ctr': 2.19,
            'conversiones': 189,
            'cvr': 1.52,
            'cpa': 33.54,
            'roas': 2.1,
            'optimizaciones_aplicadas': 8,
            'ultima_optimizacion': 'Hace 12 horas'
        }
    ]
    
    # Recomendaciones de IA
    recomendaciones = [
        {
            'campana_id': 'CAMP-001',
            'tipo': 'Ajuste de Puja',
            'prioridad': 'alta',
            'descripcion': 'Aumentar puja en keywords de alta intención (+15%)',
            'impacto_estimado': '+12% conversiones',
            'ahorro_estimado': None,
            'accion': 'Aumentar CPC máximo de €2.50 a €2.88 en 15 keywords top'
        },
        {
            'campana_id': 'CAMP-004',
            'tipo': 'Optimización de Audiencia',
            'prioridad': 'alta',
            'descripcion': 'Excluir audiencias de bajo rendimiento',
            'impacto_estimado': None,
            'ahorro_estimado': '€450/semana',
            'accion': 'Excluir 3 segmentos con CVR < 0.5% y CPA > €50'
        },
        {
            'campana_id': 'CAMP-005',
            'tipo': 'Ajuste de Presupuesto',
            'prioridad': 'media',
            'descripcion': 'Reducir presupuesto por bajo ROAS',
            'impacto_estimado': None,
            'ahorro_estimado': '€75/día',
            'accion': 'Reducir presupuesto diario de €250 a €175 (-30%)'
        },
        {
            'campana_id': 'CAMP-002',
            'tipo': 'Expansión de Keywords',
            'prioridad': 'media',
            'descripcion': 'Añadir 12 keywords de cola larga con alta intención',
            'impacto_estimado': '+8% conversiones',
            'ahorro_estimado': None,
            'accion': 'Implementar keywords relacionadas con "ahorro energía hogar"'
        },
        {
            'campana_id': 'CAMP-003',
            'tipo': 'Optimización de Horario',
            'prioridad': 'baja',
            'descripcion': 'Concentrar presupuesto en horario laboral (9-18h)',
            'impacto_estimado': '+5% CVR',
            'ahorro_estimado': '€120/semana',
            'accion': 'Aplicar bid adjustment +30% en horario laboral, -50% noche'
        }
    ]
    
    # Métricas globales
    metricas = {
        'campanas_activas': 5,
        'presupuesto_total_mes': 45630,
        'gasto_actual': 45630,
        'impresiones_totales': 5510680,
        'clicks_totales': 110509,
        'conversiones_totales': 2305,
        'roas_promedio': 3.9,
        'cpa_promedio': 19.80,
        'optimizaciones_aplicadas_mes': 76,
        'ahorro_generado_mes': 8450
    }
    
    # Rendimiento por plataforma
    plataformas = [
        {
            'nombre': 'Google Ads',
            'campanas': 2,
            'gasto': 20130,
            'conversiones': 1126,
            'roas': 3.9,
            'cpa': 17.88
        },
        {
            'nombre': 'Meta (Facebook/Instagram)',
            'campanas': 2,
            'gasto': 15260,
            'conversiones': 756,
            'roas': 2.9,
            'cpa': 20.19
        },
        {
            'nombre': 'LinkedIn',
            'campanas': 1,
            'gasto': 10240,
            'conversiones': 423,
            'roas': 5.2,
            'cpa': 24.21
        }
    ]
    
    return render_template('optimizacion_publicitaria.html',
                         campanas=campanas,
                         recomendaciones=recomendaciones,
                         metricas=metricas,
                         plataformas=plataformas)

@app.route('/api/optimizar-campanas', methods=['POST'])
@login_required
def optimizar_campanas():
    campanas = [
        {'nombre': 'Google Search', 'antes': 42, 'despues': 78, 'presupuesto': 15000, 'leads': 342},
        {'nombre': 'Meta Ads', 'antes': 38, 'despues': 69, 'presupuesto': 12000, 'leads': 289},
        {'nombre': 'Display Network', 'antes': 25, 'despues': 51, 'presupuesto': 8000, 'leads': 156},
        {'nombre': 'YouTube', 'antes': 31, 'despues': 72, 'presupuesto': 10000, 'leads': 267},
        {'nombre': 'LinkedIn B2B', 'antes': 47, 'despues': 85, 'presupuesto': 18000, 'leads': 421}
    ]
    
    resumen = {
        'reduccion_cpl': -28,
        'aumento_conversiones': 65,
        'mejora_roas': 187,
        'ahorro_mensual': 8240,
        'ajustes_presupuesto': 23,
        'keywords_optimizadas': 148,
        'creatividades_pausadas': 12,
        'audiencias_nuevas': 5
    }
    
    return jsonify({'campanas': campanas, 'resumen': resumen})

# ==================== CASOS DE USO ADICIONALES ====================

@app.route('/segmentacion-avanzada')
@login_required
def segmentacion_avanzada():
    # Segmentos identificados por ML
    segmentos = [
        {
            'id': 'SEG-001',
            'nombre': 'Eco-Conscious Premium',
            'clientes': 45230,
            'porcentaje': 12.3,
            'color': '#107C10',
            'caracteristicas': {
                'edad_promedio': 42,
                'ingreso_promedio': 75000,
                'consumo_promedio': 380,
                'antiguedad_promedio': 6.2,
                'satisfaccion': 8.7
            },
            'comportamiento': [
                'Alto interés en energía renovable',
                'Dispuestos a pagar premium por sostenibilidad',
                'Alta tasa de adopción de productos smart home',
                'Engagement alto con contenido educativo'
            ],
            'productos_recomendados': [
                {'nombre': 'Plan 100% Renovable', 'adopcion': 68, 'revenue_potencial': 125000},
                {'nombre': 'Solar Residencial Premium', 'adopcion': 45, 'revenue_potencial': 890000},
                {'nombre': 'Smart Home Bundle', 'adopcion': 52, 'revenue_potencial': 234000}
            ],
            'estrategia': 'Enfoque en sostenibilidad y tecnología. Campañas educativas sobre impacto ambiental.',
            'ltv': 8450,
            'churn_risk': 12
        },
        {
            'id': 'SEG-002',
            'nombre': 'PYME Eficiencia',
            'clientes': 18920,
            'porcentaje': 5.1,
            'color': '#0078D4',
            'caracteristicas': {
                'edad_promedio': 48,
                'ingreso_promedio': 120000,
                'consumo_promedio': 1250,
                'antiguedad_promedio': 8.5,
                'satisfaccion': 7.9
            },
            'comportamiento': [
                'Sensibles al precio y ROI',
                'Buscan optimización de costes operativos',
                'Interés en auditorías energéticas',
                'Decisión de compra basada en datos'
            ],
            'productos_recomendados': [
                {'nombre': 'Plan Empresa Pro', 'adopcion': 72, 'revenue_potencial': 456000},
                {'nombre': 'Auditoría Energética', 'adopcion': 58, 'revenue_potencial': 189000},
                {'nombre': 'Sistema Monitorización', 'adopcion': 41, 'revenue_potencial': 145000}
            ],
            'estrategia': 'Enfoque en ROI y ahorro. Casos de éxito y testimoniales de otras PYMEs.',
            'ltv': 12800,
            'churn_risk': 18
        },
        {
            'id': 'SEG-003',
            'nombre': 'Familias Jóvenes',
            'clientes': 67840,
            'porcentaje': 18.4,
            'color': '#FFB900',
            'caracteristicas': {
                'edad_promedio': 35,
                'ingreso_promedio': 48000,
                'consumo_promedio': 290,
                'antiguedad_promedio': 2.8,
                'satisfaccion': 7.2
            },
            'comportamiento': [
                'Sensibles al precio',
                'Buscan planes flexibles',
                'Alta adopción de canales digitales',
                'Interés en ahorro a largo plazo'
            ],
            'productos_recomendados': [
                {'nombre': 'Plan Ahorro Familiar', 'adopcion': 61, 'revenue_potencial': 234000},
                {'nombre': 'Termostato Smart', 'adopcion': 38, 'revenue_potencial': 98000},
                {'nombre': 'App Control Consumo', 'adopcion': 74, 'revenue_potencial': 45000}
            ],
            'estrategia': 'Marketing digital, contenido en redes sociales, gamificación del ahorro.',
            'ltv': 4200,
            'churn_risk': 28
        },
        {
            'id': 'SEG-004',
            'nombre': 'Propietarios Vehículo Eléctrico',
            'clientes': 12450,
            'porcentaje': 3.4,
            'color': '#8E24AA',
            'caracteristicas': {
                'edad_promedio': 44,
                'ingreso_promedio': 68000,
                'consumo_promedio': 520,
                'antiguedad_promedio': 3.2,
                'satisfaccion': 8.9
            },
            'comportamiento': [
                'Early adopters tecnológicos',
                'Alto consumo nocturno',
                'Interés en tarifas especiales',
                'Conciencia ambiental alta'
            ],
            'productos_recomendados': [
                {'nombre': 'Tarifa Super Valle EV', 'adopcion': 82, 'revenue_potencial': 156000},
                {'nombre': 'Wallbox Instalación', 'adopcion': 67, 'revenue_potencial': 289000},
                {'nombre': 'Solar + Batería', 'adopcion': 34, 'revenue_potencial': 445000}
            ],
            'estrategia': 'Tarifas específicas para carga nocturna. Partnerships con fabricantes EV.',
            'ltv': 9200,
            'churn_risk': 8
        },
        {
            'id': 'SEG-005',
            'nombre': 'Seniors Tradicionales',
            'clientes': 89340,
            'porcentaje': 24.2,
            'color': '#D13438',
            'caracteristicas': {
                'edad_promedio': 68,
                'ingreso_promedio': 32000,
                'consumo_promedio': 210,
                'antiguedad_promedio': 15.6,
                'satisfaccion': 8.1
            },
            'comportamiento': [
                'Leales a la marca',
                'Prefieren atención telefónica',
                'Bajo uso de canales digitales',
                'Consumo estable y predecible'
            ],
            'productos_recomendados': [
                {'nombre': 'Plan Estabilidad', 'adopcion': 78, 'revenue_potencial': 167000},
                {'nombre': 'Servicio Atención Premium', 'adopcion': 56, 'revenue_potencial': 89000},
                {'nombre': 'Mantenimiento Caldera', 'adopcion': 44, 'revenue_potencial': 123000}
            ],
            'estrategia': 'Atención personalizada telefónica. Comunicación clara y simple.',
            'ltv': 6800,
            'churn_risk': 5
        },
        {
            'id': 'SEG-006',
            'nombre': 'Alto Consumo Industrial',
            'clientes': 3420,
            'porcentaje': 0.9,
            'color': '#00B7C3',
            'caracteristicas': {
                'edad_promedio': 52,
                'ingreso_promedio': 450000,
                'consumo_promedio': 8900,
                'antiguedad_promedio': 11.2,
                'satisfaccion': 7.5
            },
            'comportamiento': [
                'Contratos a largo plazo',
                'Negociación de tarifas personalizadas',
                'Necesidad de estabilidad de suministro',
                'Interés en eficiencia operativa'
            ],
            'productos_recomendados': [
                {'nombre': 'Contrato Industrial Custom', 'adopcion': 91, 'revenue_potencial': 2340000},
                {'nombre': 'Consultoría Eficiencia', 'adopcion': 68, 'revenue_potencial': 567000},
                {'nombre': 'Sistema Monitorización 24/7', 'adopcion': 85, 'revenue_potencial': 234000}
            ],
            'estrategia': 'Account management dedicado. Soluciones personalizadas.',
            'ltv': 145000,
            'churn_risk': 15
        }
    ]
    
    # Métricas globales
    metricas = {
        'clientes_totales': 368200,
        'segmentos_identificados': 6,
        'precision_modelo': 87,
        'revenue_potencial': 6780000,
        'ltv_promedio': 7850,
        'tasa_adopcion_promedio': 62
    }
    
    # Análisis de clustering
    clustering_info = {
        'algoritmo': 'K-Means + DBSCAN',
        'features_utilizadas': 15,
        'silhouette_score': 0.68,
        'ultima_actualizacion': 'Hace 2 días'
    }
    
    return render_template('segmentacion_avanzada.html',
                         segmentos=segmentos,
                         metricas=metricas,
                         clustering_info=clustering_info)

@app.route('/ab-testing')
@login_required
def ab_testing():
    # Tests en curso
    tests_en_curso = [
        {
            'id': 'TEST-001',
            'nombre': 'Email Subject: Solar vs Ahorro',
            'tipo': 'Email Subject',
            'variante_a': {
                'nombre': 'A: "Descubre Energía Solar"',
                'impresiones': 12450,
                'clicks': 1847,
                'conversiones': 234,
                'ctr': 14.8,
                'cvr': 12.7,
                'revenue': 42000
            },
            'variante_b': {
                'nombre': 'B: "Ahorra €1,200/año con Solar"',
                'impresiones': 12380,
                'clicks': 2156,
                'conversiones': 298,
                'ctr': 17.4,
                'cvr': 13.8,
                'revenue': 53000
            },
            'estado': 'en_curso',
            'progreso': 78,
            'significancia': 95,
            'ganador_actual': 'B',
            'mejora': 26,
            'dias_restantes': 3
        },
        {
            'id': 'TEST-002',
            'nombre': 'Landing Page: Hero Image',
            'tipo': 'Landing Page',
            'variante_a': {
                'nombre': 'A: Familia con Paneles',
                'impresiones': 8920,
                'clicks': 1245,
                'conversiones': 156,
                'ctr': 14.0,
                'cvr': 12.5,
                'revenue': 28000
            },
            'variante_b': {
                'nombre': 'B: Casa con Instalación',
                'impresiones': 8850,
                'clicks': 1398,
                'conversiones': 189,
                'ctr': 15.8,
                'cvr': 13.5,
                'revenue': 34000
            },
            'estado': 'en_curso',
            'progreso': 62,
            'significancia': 89,
            'ganador_actual': 'B',
            'mejora': 21,
            'dias_restantes': 5
        },
        {
            'id': 'TEST-003',
            'nombre': 'CTA Button: Texto',
            'tipo': 'CTA Button',
            'variante_a': {
                'nombre': 'A: "Solicitar Presupuesto"',
                'impresiones': 15680,
                'clicks': 2890,
                'conversiones': 445,
                'ctr': 18.4,
                'cvr': 15.4,
                'revenue': 78000
            },
            'variante_b': {
                'nombre': 'B: "Calcula tu Ahorro Gratis"',
                'impresiones': 15720,
                'clicks': 3245,
                'conversiones': 512,
                'ctr': 20.6,
                'cvr': 15.8,
                'revenue': 89000
            },
            'estado': 'en_curso',
            'progreso': 85,
            'significancia': 98,
            'ganador_actual': 'B',
            'mejora': 14,
            'dias_restantes': 2
        }
    ]
    
    # Tests completados
    tests_completados = [
        {
            'id': 'TEST-C-001',
            'nombre': 'Ad Copy: Beneficio Principal',
            'tipo': 'Ad Copy',
            'ganador': 'B: "Reduce tu Factura 70%"',
            'mejora': 34,
            'significancia': 99,
            'conversiones': 892,
            'revenue': 145000,
            'fecha': '15 Dic 2024',
            'insight': 'Los mensajes con beneficios cuantificables generan 34% más conversiones'
        },
        {
            'id': 'TEST-C-002',
            'nombre': 'Email Timing: Hora de Envío',
            'tipo': 'Email Timing',
            'ganador': 'B: 19:00 - 21:00',
            'mejora': 28,
            'significancia': 97,
            'conversiones': 567,
            'revenue': 98000,
            'fecha': '10 Dic 2024',
            'insight': 'Los emails enviados en horario nocturno tienen 28% más engagement'
        },
        {
            'id': 'TEST-C-003',
            'nombre': 'Landing Page: Form Length',
            'tipo': 'Landing Page',
            'ganador': 'A: Formulario Corto (3 campos)',
            'mejora': 42,
            'significancia': 99,
            'conversiones': 1234,
            'revenue': 210000,
            'fecha': '5 Dic 2024',
            'insight': 'Reducir campos del formulario de 7 a 3 aumenta conversiones 42%'
        },
        {
            'id': 'TEST-C-004',
            'nombre': 'Precio Display: Formato',
            'tipo': 'Pricing',
            'ganador': 'B: "€99/mes" vs "€1,188/año"',
            'mejora': 19,
            'significancia': 95,
            'conversiones': 445,
            'revenue': 76000,
            'fecha': '1 Dic 2024',
            'insight': 'Mostrar precio mensual aumenta conversiones 19% vs precio anual'
        }
    ]
    
    # Métricas globales
    metricas = {
        'tests_activos': len(tests_en_curso),
        'tests_completados_mes': 12,
        'lift_promedio': 27,
        'revenue_incremental': 245000,
        'significancia_promedio': 96,
        'velocidad_vs_manual': 6
    }
    
    return render_template('ab_testing.html',
                         tests_en_curso=tests_en_curso,
                         tests_completados=tests_completados,
                         metricas=metricas)

@app.route('/monitorizacion-marca')
@login_required
def monitorizacion_marca():
    # Menciones recientes con más detalles
    menciones = [
        {
            'id': 'M-001',
            'fuente': 'Twitter',
            'usuario': '@maria_garcia',
            'seguidores': 12500,
            'sentimiento': 'positivo',
            'score_sentimiento': 0.92,
            'texto': 'Excelente servicio de @Iberdrola, resolvieron mi problema en minutos. Atención al cliente de 10! 👏',
            'tiempo': '5 min',
            'engagement': 234,
            'alcance': 45000,
            'temas': ['Atención Cliente', 'Satisfacción']
        },
        {
            'id': 'M-002',
            'fuente': 'Facebook',
            'usuario': 'Carlos Ruiz',
            'seguidores': 890,
            'sentimiento': 'neutral',
            'score_sentimiento': 0.52,
            'texto': '¿Alguien tiene experiencia con paneles solares de Iberdrola? Estoy pensando en instalar pero tengo dudas sobre el ROI',
            'tiempo': '23 min',
            'engagement': 45,
            'alcance': 2300,
            'temas': ['Solar', 'Consulta']
        },
        {
            'id': 'M-003',
            'fuente': 'Instagram',
            'usuario': '@ana_sostenible',
            'seguidores': 34200,
            'sentimiento': 'positivo',
            'score_sentimiento': 0.95,
            'texto': 'Mi casa ahora funciona 100% con energía solar gracias a Iberdrola 🌞☀️ #EnergíaRenovable #Sostenibilidad',
            'tiempo': '1 hora',
            'engagement': 1847,
            'alcance': 128000,
            'temas': ['Solar', 'Sostenibilidad', 'Testimonial']
        },
        {
            'id': 'M-004',
            'fuente': 'Twitter',
            'usuario': '@cliente_molesto',
            'seguidores': 456,
            'sentimiento': 'negativo',
            'score_sentimiento': 0.15,
            'texto': 'Llevo 2 días esperando respuesta sobre mi factura @Iberdrola. Esto es inaceptable! 😡',
            'tiempo': '2 horas',
            'engagement': 89,
            'alcance': 12000,
            'temas': ['Facturación', 'Queja', 'Urgente']
        },
        {
            'id': 'M-005',
            'fuente': 'LinkedIn',
            'usuario': 'David López',
            'seguidores': 8900,
            'sentimiento': 'positivo',
            'score_sentimiento': 0.88,
            'texto': 'Iberdrola lidera la transición energética en España. Impresionante su compromiso con las renovables y la innovación.',
            'tiempo': '3 horas',
            'engagement': 567,
            'alcance': 67000,
            'temas': ['Renovables', 'Innovación', 'Liderazgo']
        },
        {
            'id': 'M-006',
            'fuente': 'Twitter',
            'usuario': '@eco_warrior',
            'seguidores': 23400,
            'sentimiento': 'neutral',
            'score_sentimiento': 0.48,
            'texto': 'Iberdrola anuncia nuevos parques eólicos. Bien por las renovables, pero ¿qué pasa con los precios para los consumidores?',
            'tiempo': '4 horas',
            'engagement': 345,
            'alcance': 89000,
            'temas': ['Renovables', 'Precios', 'Debate']
        }
    ]
    
    # Métricas globales
    metricas = {
        'menciones_hoy': 1847,
        'menciones_semana': 12450,
        'sentimiento_positivo': 72,
        'sentimiento_neutral': 21,
        'sentimiento_negativo': 7,
        'alcance_total': 2340000,
        'engagement_rate': 4.8,
        'tiempo_respuesta_promedio': 12,  # minutos
        'crisis_detectadas': 0,
        'oportunidades_detectadas': 8
    }
    
    # Tendencias de temas
    temas_trending = [
        {'tema': 'Energía Solar', 'menciones': 3420, 'crecimiento': 45, 'sentimiento': 0.85},
        {'tema': 'Atención Cliente', 'menciones': 2890, 'crecimiento': 12, 'sentimiento': 0.78},
        {'tema': 'Facturación', 'menciones': 1240, 'crecimiento': -8, 'sentimiento': 0.42},
        {'tema': 'Sostenibilidad', 'menciones': 2650, 'crecimiento': 67, 'sentimiento': 0.92},
        {'tema': 'Precios', 'menciones': 1980, 'crecimiento': 23, 'sentimiento': 0.38}
    ]
    
    # Competencia
    competencia = [
        {'empresa': 'Endesa', 'menciones': 8450, 'sentimiento': 0.68, 'share_of_voice': 28},
        {'empresa': 'Naturgy', 'menciones': 6230, 'sentimiento': 0.65, 'share_of_voice': 21},
        {'empresa': 'Repsol', 'menciones': 5890, 'sentimiento': 0.71, 'share_of_voice': 19},
        {'empresa': 'Iberdrola', 'menciones': 9670, 'sentimiento': 0.75, 'share_of_voice': 32}
    ]
    
    return render_template('monitorizacion_marca.html', 
                         menciones=menciones,
                         metricas=metricas,
                         temas_trending=temas_trending,
                         competencia=competencia)

@app.route('/motor-recomendaciones')
@login_required
def motor_recomendaciones():
    # Simulación de clientes con recomendaciones
    clientes_recomendaciones = [
        {
            'id': 'C-00234',
            'nombre': 'María González',
            'segmento': 'Premium',
            'consumo_actual': '450 kWh/mes',
            'recomendaciones': [
                {
                    'producto': 'Plan Solar Plus',
                    'tipo': 'Energía Solar',
                    'score': 0.94,
                    'ahorro_estimado': '€45/mes',
                    'razon': 'Alto consumo diurno + ubicación óptima',
                    'probabilidad': 94
                },
                {
                    'producto': 'Smart Home Pack',
                    'tipo': 'Domótica',
                    'score': 0.87,
                    'ahorro_estimado': '€25/mes',
                    'razon': 'Perfil tecnológico + consumo variable',
                    'probabilidad': 87
                },
                {
                    'producto': 'Coche Eléctrico - Tarifa Nocturna',
                    'tipo': 'Movilidad',
                    'score': 0.76,
                    'ahorro_estimado': '€60/mes',
                    'razon': 'Patrón de consumo compatible',
                    'probabilidad': 76
                }
            ]
        },
        {
            'id': 'C-00891',
            'nombre': 'Carlos Ruiz',
            'segmento': 'Estándar',
            'consumo_actual': '280 kWh/mes',
            'recomendaciones': [
                {
                    'producto': 'Plan Ahorro Inteligente',
                    'tipo': 'Tarifa Optimizada',
                    'score': 0.91,
                    'ahorro_estimado': '€18/mes',
                    'razon': 'Consumo estable + horario predecible',
                    'probabilidad': 91
                },
                {
                    'producto': 'Termostato Smart',
                    'tipo': 'Eficiencia',
                    'score': 0.82,
                    'ahorro_estimado': '€15/mes',
                    'razon': 'Alto consumo en calefacción',
                    'probabilidad': 82
                },
                {
                    'producto': 'Mantenimiento Caldera',
                    'tipo': 'Servicio',
                    'score': 0.68,
                    'ahorro_estimado': '€10/mes',
                    'razon': 'Equipo con +5 años antigüedad',
                    'probabilidad': 68
                }
            ]
        },
        {
            'id': 'C-01245',
            'nombre': 'Ana Martínez',
            'segmento': 'Eco-Conscious',
            'consumo_actual': '320 kWh/mes',
            'recomendaciones': [
                {
                    'producto': 'Energía 100% Renovable',
                    'tipo': 'Energía Verde',
                    'score': 0.96,
                    'ahorro_estimado': '€0/mes',
                    'razon': 'Perfil sostenible + valores ecológicos',
                    'probabilidad': 96
                },
                {
                    'producto': 'Batería Doméstica',
                    'tipo': 'Almacenamiento',
                    'score': 0.85,
                    'ahorro_estimado': '€35/mes',
                    'razon': 'Tiene paneles solares instalados',
                    'probabilidad': 85
                },
                {
                    'producto': 'Certificado Huella Carbono',
                    'tipo': 'Sostenibilidad',
                    'score': 0.79,
                    'ahorro_estimado': '€0/mes',
                    'razon': 'Interés en compensación CO₂',
                    'probabilidad': 79
                }
            ]
        },
        {
            'id': 'C-02156',
            'nombre': 'David López',
            'segmento': 'Business',
            'consumo_actual': '1,200 kWh/mes',
            'recomendaciones': [
                {
                    'producto': 'Plan Empresa Pro',
                    'tipo': 'Tarifa Business',
                    'score': 0.93,
                    'ahorro_estimado': '€120/mes',
                    'razon': 'Consumo comercial + horario oficina',
                    'probabilidad': 93
                },
                {
                    'producto': 'Auditoría Energética',
                    'tipo': 'Consultoría',
                    'score': 0.88,
                    'ahorro_estimado': '€200/mes',
                    'razon': 'Alto potencial de optimización',
                    'probabilidad': 88
                },
                {
                    'producto': 'Sistema Solar Comercial',
                    'tipo': 'Autoconsumo',
                    'score': 0.81,
                    'ahorro_estimado': '€180/mes',
                    'razon': 'ROI 4 años + subvenciones disponibles',
                    'probabilidad': 81
                }
            ]
        }
    ]
    
    # Métricas del motor
    metricas_motor = {
        'precision': 0.87,
        'recall': 0.82,
        'f1_score': 0.84,
        'auc_roc': 0.91,
        'cobertura': 0.95,
        'latencia_ms': 45,
        'recomendaciones_dia': 12500,
        'tasa_conversion': 0.34,
        'revenue_incremental': 285000
    }
    
    # Productos más recomendados
    top_productos = [
        {'nombre': 'Plan Solar Plus', 'recomendaciones': 3420, 'conversion': 0.42, 'revenue': '€156K'},
        {'nombre': 'Smart Home Pack', 'recomendaciones': 2890, 'conversion': 0.38, 'revenue': '€98K'},
        {'nombre': 'Energía 100% Renovable', 'recomendaciones': 2650, 'conversion': 0.51, 'revenue': '€67K'},
        {'nombre': 'Plan Ahorro Inteligente', 'recomendaciones': 2340, 'conversion': 0.29, 'revenue': '€45K'},
        {'nombre': 'Coche Eléctrico - Tarifa', 'recomendaciones': 1980, 'conversion': 0.24, 'revenue': '€89K'}
    ]
    
    return render_template('motor_recomendaciones.html', 
                         clientes=clientes_recomendaciones,
                         metricas=metricas_motor,
                         top_productos=top_productos)

@app.route('/attribution-marketing')
@login_required
def attribution_marketing():
    # Modelos de atribución comparados
    modelos_atribucion = [
        {
            'nombre': 'Data-Driven (IA)',
            'descripcion': 'Modelo basado en machine learning',
            'conversiones': 1847,
            'revenue': 285000,
            'roi': 4.8,
            'recomendado': True
        },
        {
            'nombre': 'Time Decay',
            'descripcion': 'Mayor peso a touchpoints recientes',
            'conversiones': 1623,
            'revenue': 248000,
            'roi': 4.2
        },
        {
            'nombre': 'Position Based',
            'descripcion': '40% primero, 40% último, 20% medio',
            'conversiones': 1756,
            'revenue': 267000,
            'roi': 4.5
        },
        {
            'nombre': 'Linear',
            'descripcion': 'Peso igual a todos los touchpoints',
            'conversiones': 1534,
            'revenue': 234000,
            'roi': 3.9
        },
        {
            'nombre': 'Last Click',
            'descripcion': '100% al último touchpoint',
            'conversiones': 1289,
            'revenue': 198000,
            'roi': 3.3
        },
        {
            'nombre': 'First Click',
            'descripcion': '100% al primer touchpoint',
            'conversiones': 1412,
            'revenue': 215000,
            'roi': 3.6
        }
    ]
    
    # Análisis por canal
    canales = [
        {
            'nombre': 'Paid Search',
            'icono': '🔍',
            'touchpoints': 12450,
            'conversiones': 892,
            'valor_atribuido': 142000,
            'porcentaje': 28,
            'cpa': 159,
            'tiempo_conversion': 12
        },
        {
            'nombre': 'Organic Search',
            'icono': '🌐',
            'touchpoints': 18920,
            'conversiones': 1240,
            'valor_atribuido': 98000,
            'porcentaje': 19,
            'cpa': 79,
            'tiempo_conversion': 18
        },
        {
            'nombre': 'Social Media',
            'icono': '📱',
            'touchpoints': 24560,
            'conversiones': 645,
            'valor_atribuido': 76000,
            'porcentaje': 15,
            'cpa': 118,
            'tiempo_conversion': 24
        },
        {
            'nombre': 'Email Marketing',
            'icono': '📧',
            'touchpoints': 15680,
            'conversiones': 1089,
            'valor_atribuido': 89000,
            'porcentaje': 18,
            'cpa': 82,
            'tiempo_conversion': 8
        },
        {
            'nombre': 'Display Ads',
            'icono': '🎨',
            'touchpoints': 8920,
            'conversiones': 423,
            'valor_atribuido': 51000,
            'porcentaje': 10,
            'cpa': 121,
            'tiempo_conversion': 21
        },
        {
            'nombre': 'Direct',
            'icono': '🎯',
            'touchpoints': 6780,
            'conversiones': 567,
            'valor_atribuido': 52000,
            'porcentaje': 10,
            'cpa': 92,
            'tiempo_conversion': 5
        }
    ]
    
    # Paths de conversión más comunes
    conversion_paths = [
        {
            'path': ['Social Media', 'Organic Search', 'Paid Search'],
            'conversiones': 342,
            'valor': 58000,
            'tiempo_promedio': 18
        },
        {
            'path': ['Paid Search', 'Email', 'Direct'],
            'conversiones': 289,
            'valor': 48000,
            'tiempo_promedio': 12
        },
        {
            'path': ['Organic Search', 'Social Media', 'Email', 'Paid Search'],
            'conversiones': 267,
            'valor': 45000,
            'tiempo_promedio': 24
        },
        {
            'path': ['Display', 'Organic Search', 'Direct'],
            'conversiones': 234,
            'valor': 39000,
            'tiempo_promedio': 15
        },
        {
            'path': ['Social Media', 'Email', 'Paid Search'],
            'conversiones': 198,
            'valor': 34000,
            'tiempo_promedio': 16
        }
    ]
    
    # Métricas globales
    metricas = {
        'conversiones_totales': 1847,
        'revenue_total': 508000,
        'touchpoints_totales': 87310,
        'tiempo_promedio_conversion': 15.8,
        'canales_promedio': 3.2,
        'mejora_vs_lastclick': 38
    }
    
    return render_template('attribution_marketing.html',
                         modelos=modelos_atribucion,
                         canales=canales,
                         conversion_paths=conversion_paths,
                         metricas=metricas)

# ==================== CONFIGURACIÓN Y PERFIL ====================

@app.route('/configuracion')
@login_required
def configuracion():
    return render_template('configuracion.html')

@app.route('/integracion-datos')
@login_required
def integracion_datos():
    # Definir las fuentes de datos disponibles
    fuentes_datos = [
        {
            'id': 'crm',
            'nombre': 'Salesforce CRM',
            'tipo': 'CRM',
            'estado': 'conectado',
            'registros': 2450000,
            'ultima_sync': 'Hace 5 min',
            'frecuencia': 'Tiempo real',
            'casos_uso': ['personalizacion', 'chatbot', 'motor_recomendaciones', 'prediccion_churn', 'segmentacion_avanzada']
        },
        {
            'id': 'erp',
            'nombre': 'SAP ERP',
            'tipo': 'ERP',
            'estado': 'conectado',
            'registros': 8900000,
            'ultima_sync': 'Hace 2 min',
            'frecuencia': 'Cada hora',
            'casos_uso': ['personalizacion', 'motor_recomendaciones', 'prediccion_churn']
        },
        {
            'id': 'smart_meters',
            'nombre': 'Smart Meters IoT',
            'tipo': 'IoT',
            'estado': 'conectado',
            'registros': 15000000,
            'ultima_sync': 'Hace 1 min',
            'frecuencia': 'Cada 15 min',
            'casos_uso': ['personalizacion', 'prediccion_churn', 'segmentacion_avanzada']
        },
        {
            'id': 'web_analytics',
            'nombre': 'Google Analytics',
            'tipo': 'Analytics',
            'estado': 'conectado',
            'registros': 45000000,
            'ultima_sync': 'Hace 3 min',
            'frecuencia': 'Cada hora',
            'casos_uso': ['personalizacion', 'contenido_genai', 'optimizacion_publicitaria', 'ab_testing']
        },
        {
            'id': 'social_media',
            'nombre': 'Social Media APIs',
            'tipo': 'Social',
            'estado': 'conectado',
            'registros': 2300000,
            'ultima_sync': 'Hace 10 min',
            'frecuencia': 'Cada 30 min',
            'casos_uso': ['monitorizacion_marca', 'contenido_genai']
        },
        {
            'id': 'ad_platforms',
            'nombre': 'Ad Platforms (Google/Meta/LinkedIn)',
            'tipo': 'Advertising',
            'estado': 'conectado',
            'registros': 1200000,
            'ultima_sync': 'Hace 1 hora',
            'frecuencia': 'Cada hora',
            'casos_uso': ['optimizacion_publicitaria', 'ab_testing', 'attribution_marketing']
        },
        {
            'id': 'email_platform',
            'nombre': 'Salesforce Marketing Cloud',
            'tipo': 'Marketing',
            'estado': 'conectado',
            'registros': 5600000,
            'ultima_sync': 'Hace 15 min',
            'frecuencia': 'Cada 30 min',
            'casos_uso': ['personalizacion', 'contenido_genai', 'ab_testing']
        },
        {
            'id': 'call_center',
            'nombre': 'Call Center Platform',
            'tipo': 'Support',
            'estado': 'conectado',
            'registros': 890000,
            'ultima_sync': 'Hace 5 min',
            'frecuencia': 'Tiempo real',
            'casos_uso': ['chatbot', 'prediccion_churn']
        },
        {
            'id': 'data_warehouse',
            'nombre': 'Azure Synapse Analytics',
            'tipo': 'Data Warehouse',
            'estado': 'conectado',
            'registros': 120000000,
            'ultima_sync': 'Hace 30 min',
            'frecuencia': 'Batch diario',
            'casos_uso': ['personalizacion', 'motor_recomendaciones', 'prediccion_churn', 'segmentacion_avanzada', 'attribution_marketing']
        }
    ]
    
    # Mapeo de casos de uso con sus datos necesarios
    casos_uso_datos = {
        'personalizacion': {
            'nombre': 'Personalización Hiperpersonalizada',
            'icon': '👤',
            'datos_necesarios': [
                {'fuente': 'CRM', 'tipo': 'Perfil de cliente, historial de interacciones, productos contratados'},
                {'fuente': 'Smart Meters', 'tipo': 'Consumo energético horario, patrones de uso'},
                {'fuente': 'Web Analytics', 'tipo': 'Comportamiento web, páginas visitadas, tiempo en sitio'},
                {'fuente': 'Email Platform', 'tipo': 'Apertura de emails, clicks, respuestas a campañas'},
                {'fuente': 'Data Warehouse', 'tipo': 'Datos históricos agregados, features pre-calculadas'}
            ]
        },
        'chatbot': {
            'nombre': 'Chatbot IA',
            'icon': '💬',
            'datos_necesarios': [
                {'fuente': 'CRM', 'tipo': 'Perfil de cliente, tickets, historial de soporte'},
                {'fuente': 'Call Center', 'tipo': 'Transcripciones de llamadas, FAQs, resoluciones'},
                {'fuente': 'Knowledge Base', 'tipo': 'Documentación, políticas, procedimientos'}
            ]
        },
        'motor_recomendaciones': {
            'nombre': 'Motor de Recomendaciones',
            'icon': '🎁',
            'datos_necesarios': [
                {'fuente': 'CRM', 'tipo': 'Productos contratados, upgrades, cancelaciones'},
                {'fuente': 'ERP', 'tipo': 'Catálogo de productos, precios, disponibilidad'},
                {'fuente': 'Data Warehouse', 'tipo': 'Matriz usuario-producto, interacciones históricas'}
            ]
        },
        'prediccion_churn': {
            'nombre': 'Predicción de Churn',
            'icon': '📈',
            'datos_necesarios': [
                {'fuente': 'CRM', 'tipo': 'Quejas, NPS, cambios de tarifa, antigüedad'},
                {'fuente': 'Smart Meters', 'tipo': 'Tendencia de consumo, variabilidad'},
                {'fuente': 'ERP', 'tipo': 'Historial de pagos, retrasos, facturación'},
                {'fuente': 'Call Center', 'tipo': 'Frecuencia de llamadas, motivos de contacto'},
                {'fuente': 'Data Warehouse', 'tipo': 'Features de churn pre-calculadas, histórico'}
            ]
        },
        'segmentacion_avanzada': {
            'nombre': 'Segmentación Avanzada',
            'icon': '🔍',
            'datos_necesarios': [
                {'fuente': 'CRM', 'tipo': 'Datos demográficos, productos, LTV'},
                {'fuente': 'Smart Meters', 'tipo': 'Patrones de consumo, estacionalidad'},
                {'fuente': 'Data Warehouse', 'tipo': 'Variables agregadas, comportamiento histórico'}
            ]
        },
        'contenido_genai': {
            'nombre': 'Generación de Contenido GenAI',
            'icon': '✍️',
            'datos_necesarios': [
                {'fuente': 'Web Analytics', 'tipo': 'Keywords, performance de contenido, SEO'},
                {'fuente': 'Social Media', 'tipo': 'Engagement, trending topics, competencia'},
                {'fuente': 'Email Platform', 'tipo': 'Performance de campañas, A/B tests'},
                {'fuente': 'Knowledge Base', 'tipo': 'Guías de estilo, contenido histórico, brand voice'}
            ]
        },
        'monitorizacion_marca': {
            'nombre': 'Monitorización de Marca',
            'icon': '📡',
            'datos_necesarios': [
                {'fuente': 'Social Media', 'tipo': 'Menciones, sentimiento, engagement, reach'},
                {'fuente': 'Web Analytics', 'tipo': 'Tráfico, brand searches, referrals'}
            ]
        },
        'optimizacion_publicitaria': {
            'nombre': 'Optimización Publicitaria',
            'icon': '🎯',
            'datos_necesarios': [
                {'fuente': 'Ad Platforms', 'tipo': 'Impresiones, clicks, conversiones, coste, CTR, CPA'},
                {'fuente': 'Web Analytics', 'tipo': 'Conversiones, revenue, funnel'},
                {'fuente': 'CRM', 'tipo': 'Atribución de conversiones, LTV de clientes adquiridos'}
            ]
        },
        'ab_testing': {
            'nombre': 'A/B Testing',
            'icon': '🧪',
            'datos_necesarios': [
                {'fuente': 'Web Analytics', 'tipo': 'Exposiciones, conversiones, métricas por variante'},
                {'fuente': 'Email Platform', 'tipo': 'Open rate, CTR, conversiones por variante'},
                {'fuente': 'Ad Platforms', 'tipo': 'Performance de creativos, A/B tests de ads'}
            ]
        },
        'attribution_marketing': {
            'nombre': 'Attribution Marketing',
            'icon': '🔗',
            'datos_necesarios': [
                {'fuente': 'Web Analytics', 'tipo': 'Customer journey, touchpoints, conversiones'},
                {'fuente': 'Ad Platforms', 'tipo': 'Clicks, impresiones, coste por canal'},
                {'fuente': 'Data Warehouse', 'tipo': 'Paths de conversión completos, multi-touch data'}
            ]
        }
    }
    
    # Métricas globales
    metricas = {
        'fuentes_conectadas': len([f for f in fuentes_datos if f['estado'] == 'conectado']),
        'total_fuentes': len(fuentes_datos),
        'registros_totales': sum(f['registros'] for f in fuentes_datos),
        'casos_uso_activos': len(casos_uso_datos),
        'latencia_promedio': 245,
        'uptime': 99.8
    }
    
    return render_template('integracion_datos.html',
                         fuentes_datos=fuentes_datos,
                         casos_uso_datos=casos_uso_datos,
                         metricas=metricas)

@app.route('/integracion-apis')
@login_required
def integracion_apis():
    # Definir los endpoints de IA disponibles
    endpoints_ia = [
        {
            'id': 'personalizacion_api',
            'nombre': 'Personalización API',
            'descripcion': 'Recomendaciones personalizadas en tiempo real',
            'metodo': 'POST',
            'endpoint': '/api/v1/personalizacion/recomendaciones',
            'latencia': '85ms',
            'requests_mes': 2450000,
            'uptime': 99.9,
            'integraciones': ['Salesforce', 'Adobe Experience Cloud', 'Web/App']
        },
        {
            'id': 'churn_api',
            'nombre': 'Churn Prediction API',
            'descripcion': 'Predicción de riesgo de abandono por cliente',
            'metodo': 'POST',
            'endpoint': '/api/v1/churn/predict',
            'latencia': '120ms',
            'requests_mes': 890000,
            'uptime': 99.8,
            'integraciones': ['Salesforce CRM', 'Zendesk', 'HubSpot']
        },
        {
            'id': 'chatbot_api',
            'nombre': 'Chatbot API',
            'descripcion': 'Procesamiento de lenguaje natural conversacional',
            'metodo': 'POST',
            'endpoint': '/api/v1/chatbot/conversation',
            'latencia': '450ms',
            'requests_mes': 5600000,
            'uptime': 99.7,
            'integraciones': ['WhatsApp', 'Web Widget', 'Telegram', 'MS Teams']
        },
        {
            'id': 'contenido_api',
            'nombre': 'Content Generation API',
            'descripcion': 'Generación de contenido con GenAI',
            'metodo': 'POST',
            'endpoint': '/api/v1/content/generate',
            'latencia': '2800ms',
            'requests_mes': 145000,
            'uptime': 99.5,
            'integraciones': ['Salesforce Marketing Cloud', 'WordPress', 'Contentful']
        },
        {
            'id': 'segmentacion_api',
            'nombre': 'Segmentation API',
            'descripcion': 'Asignación automática de segmentos de cliente',
            'metodo': 'POST',
            'endpoint': '/api/v1/segmentation/assign',
            'latencia': '95ms',
            'requests_mes': 450000,
            'uptime': 99.9,
            'integraciones': ['Salesforce', 'Google Analytics', 'Segment']
        },
        {
            'id': 'sentiment_api',
            'nombre': 'Sentiment Analysis API',
            'descripcion': 'Análisis de sentimiento en tiempo real',
            'metodo': 'POST',
            'endpoint': '/api/v1/sentiment/analyze',
            'latencia': '180ms',
            'requests_mes': 1200000,
            'uptime': 99.6,
            'integraciones': ['Brandwatch', 'Hootsuite', 'Sprinklr']
        }
    ]
    
    # Aplicaciones empresariales que se integran
    aplicaciones_empresariales = [
        {
            'nombre': 'Salesforce',
            'logo': '☁️',
            'categoria': 'CRM',
            'endpoints_conectados': ['personalizacion_api', 'churn_api', 'segmentacion_api'],
            'tipo_integracion': 'REST API + Webhooks',
            'estado': 'activo',
            'descripcion': 'Enriquecimiento de perfiles, alertas de churn, segmentación automática'
        },
        {
            'nombre': 'Adobe Experience Cloud',
            'logo': '🎨',
            'categoria': 'Marketing',
            'endpoints_conectados': ['personalizacion_api', 'contenido_api'],
            'tipo_integracion': 'REST API',
            'estado': 'activo',
            'descripcion': 'Personalización de experiencias web, generación de contenido dinámico'
        },
        {
            'nombre': 'WhatsApp Business',
            'logo': '💬',
            'categoria': 'Comunicación',
            'endpoints_conectados': ['chatbot_api', 'sentiment_api'],
            'tipo_integracion': 'WhatsApp API',
            'estado': 'activo',
            'descripcion': 'Bot conversacional 24/7, análisis de sentimiento de conversaciones'
        },
        {
            'nombre': 'Salesforce Marketing Cloud',
            'logo': '📧',
            'categoria': 'Marketing Automation',
            'endpoints_conectados': ['personalizacion_api', 'contenido_api', 'segmentacion_api'],
            'tipo_integracion': 'REST API + Journey Builder',
            'estado': 'activo',
            'descripcion': 'Campañas personalizadas, contenido generado por IA, segmentación dinámica'
        },
        {
            'nombre': 'Microsoft Teams',
            'logo': '👥',
            'categoria': 'Colaboración',
            'endpoints_conectados': ['chatbot_api'],
            'tipo_integracion': 'Bot Framework',
            'estado': 'activo',
            'descripcion': 'Asistente virtual interno para empleados'
        },
        {
            'nombre': 'Zendesk',
            'logo': '🎫',
            'categoria': 'Customer Support',
            'endpoints_conectados': ['churn_api', 'chatbot_api', 'sentiment_api'],
            'tipo_integracion': 'REST API + Webhooks',
            'estado': 'activo',
            'descripcion': 'Alertas de churn, bot de soporte, análisis de tickets'
        },
        {
            'nombre': 'Google Analytics',
            'logo': '📊',
            'categoria': 'Analytics',
            'endpoints_conectados': ['segmentacion_api', 'personalizacion_api'],
            'tipo_integracion': 'Measurement Protocol',
            'estado': 'activo',
            'descripcion': 'Tracking de segmentos, eventos de personalización'
        },
        {
            'nombre': 'Power BI',
            'logo': '📈',
            'categoria': 'Business Intelligence',
            'endpoints_conectados': ['churn_api', 'segmentacion_api'],
            'tipo_integracion': 'REST API + DirectQuery',
            'estado': 'activo',
            'descripcion': 'Dashboards con predicciones, análisis de segmentos'
        }
    ]
    
    # Métricas globales
    metricas = {
        'total_endpoints': len(endpoints_ia),
        'total_aplicaciones': len(aplicaciones_empresariales),
        'requests_totales': sum(ep['requests_mes'] for ep in endpoints_ia),
        'latencia_promedio': sum(int(ep['latencia'].replace('ms', '')) for ep in endpoints_ia) / len(endpoints_ia),
        'uptime_promedio': sum(ep['uptime'] for ep in endpoints_ia) / len(endpoints_ia),
        'integraciones_activas': sum(len(app['endpoints_conectados']) for app in aplicaciones_empresariales)
    }
    
    return render_template('integracion_apis.html',
                         endpoints_ia=endpoints_ia,
                         aplicaciones_empresariales=aplicaciones_empresariales,
                         metricas=metricas)

@app.route('/laboratorio')
@login_required
def laboratorio():
    # Notebooks de ejemplo predefinidos
    notebooks_ejemplos = [
        {
            'id': 'analisis_churn',
            'nombre': 'Análisis de Churn con Python',
            'descripcion': 'Explora patrones de abandono de clientes usando pandas y scikit-learn',
            'categoria': 'Customer Intelligence',
            'duracion': '15 min',
            'nivel': 'Intermedio'
        },
        {
            'id': 'segmentacion_rfm',
            'nombre': 'Segmentación RFM',
            'descripcion': 'Segmenta clientes por Recency, Frequency y Monetary value',
            'categoria': 'Customer Intelligence',
            'duracion': '10 min',
            'nivel': 'Básico'
        },
        {
            'id': 'analisis_campanas',
            'nombre': 'Performance de Campañas',
            'descripcion': 'Analiza métricas de campañas de email marketing',
            'categoria': 'Campaign Optimization',
            'duracion': '12 min',
            'nivel': 'Básico'
        },
        {
            'id': 'prediccion_ltv',
            'nombre': 'Predicción de LTV',
            'descripcion': 'Predice el valor de vida del cliente con modelos de ML',
            'categoria': 'Customer Intelligence',
            'duracion': '20 min',
            'nivel': 'Avanzado'
        }
    ]
    
    # Fuentes de datos disponibles
    fuentes_disponibles = [
        {'nombre': 'Salesforce CRM', 'registros': '2.45M', 'icon': '☁️'},
        {'nombre': 'Smart Meters IoT', 'registros': '15M', 'icon': '⚡'},
        {'nombre': 'Google Analytics', 'registros': '45M', 'icon': '📊'},
        {'nombre': 'Social Media APIs', 'registros': '2.3M', 'icon': '💬'},
        {'nombre': 'Email Platform', 'registros': '5.6M', 'icon': '📧'},
        {'nombre': 'Data Warehouse', 'registros': '120M', 'icon': '🗄️'}
    ]
    
    return render_template('laboratorio.html',
                         notebooks_ejemplos=notebooks_ejemplos,
                         fuentes_disponibles=fuentes_disponibles)

@app.route('/monitorizacion')
@login_required
def monitorizacion():
    from datetime import datetime, timedelta
    import random
    
    # Métricas generales del sistema
    metricas_sistema = {
        'usuarios_activos': 47,
        'sesiones_hoy': 312,
        'api_calls_hoy': '2.4M',
        'uptime': '99.7%',
        'latencia_promedio': '85ms',
        'errores_hoy': 23
    }
    
    # Actividad reciente (últimas 50 acciones)
    usuarios = [
        {'nombre': 'Ana Martínez', 'avatar': 'AM', 'rol': 'Analista Marketing'},
        {'nombre': 'Carlos Ruiz', 'avatar': 'CR', 'rol': 'Data Scientist'},
        {'nombre': 'Laura Sánchez', 'avatar': 'LS', 'rol': 'Marketing Manager'},
        {'nombre': 'Miguel Torres', 'avatar': 'MT', 'rol': 'Business Analyst'},
        {'nombre': 'Elena García', 'avatar': 'EG', 'rol': 'CMO'},
        {'nombre': 'David López', 'avatar': 'DL', 'rol': 'Product Manager'},
        {'nombre': 'Sara Fernández', 'avatar': 'SF', 'rol': 'Data Analyst'},
        {'nombre': 'Javier Moreno', 'avatar': 'JM', 'rol': 'Marketing Specialist'}
    ]
    
    acciones = [
        {'tipo': 'api_call', 'icono': '🔌', 'descripcion': 'llamó al endpoint de', 'objeto': 'Personalización API'},
        {'tipo': 'view', 'icono': '👁️', 'descripcion': 'visualizó', 'objeto': 'Dashboard de Churn'},
        {'tipo': 'export', 'icono': '📥', 'descripcion': 'exportó datos de', 'objeto': 'Segmentación de Clientes'},
        {'tipo': 'create', 'icono': '➕', 'descripcion': 'creó un nuevo', 'objeto': 'Notebook de Análisis'},
        {'tipo': 'update', 'icono': '✏️', 'descripcion': 'actualizó', 'objeto': 'Campaña de Email'},
        {'tipo': 'delete', 'icono': '🗑️', 'descripcion': 'eliminó', 'objeto': 'Test A/B antiguo'},
        {'tipo': 'login', 'icono': '🔐', 'descripcion': 'inició sesión en', 'objeto': 'la plataforma'},
        {'tipo': 'config', 'icono': '⚙️', 'descripcion': 'modificó configuración de', 'objeto': 'Integración Salesforce'},
        {'tipo': 'generate', 'icono': '✨', 'descripcion': 'generó contenido con', 'objeto': 'GenAI API'},
        {'tipo': 'train', 'icono': '🤖', 'descripcion': 'entrenó modelo de', 'objeto': 'Predicción de Churn'}
    ]
    
    actividad_reciente = []
    now = datetime.now()
    
    for i in range(50):
        usuario = random.choice(usuarios)
        accion = random.choice(acciones)
        minutos_atras = i * random.randint(2, 15)
        timestamp = now - timedelta(minutes=minutos_atras)
        
        actividad_reciente.append({
            'id': f'act_{i+1}',
            'usuario': usuario['nombre'],
            'avatar': usuario['avatar'],
            'rol': usuario['rol'],
            'tipo': accion['tipo'],
            'icono': accion['icono'],
            'descripcion': accion['descripcion'],
            'objeto': accion['objeto'],
            'timestamp': timestamp,
            'ip': f'192.168.{random.randint(1,255)}.{random.randint(1,255)}'
        })
    
    # Uso de APIs por endpoint
    uso_apis = [
        {'endpoint': 'Personalización API', 'calls': 2450000, 'errores': 12, 'latencia': 85},
        {'endpoint': 'Chatbot API', 'calls': 5600000, 'errores': 45, 'latencia': 450},
        {'endpoint': 'Churn Prediction API', 'calls': 890000, 'errores': 8, 'latencia': 120},
        {'endpoint': 'Content Generation API', 'calls': 145000, 'errores': 23, 'latencia': 2800},
        {'endpoint': 'Segmentation API', 'calls': 450000, 'errores': 5, 'latencia': 95},
        {'endpoint': 'Sentiment Analysis API', 'calls': 1200000, 'errores': 18, 'latencia': 180}
    ]
    
    # Eventos del sistema
    eventos_sistema = [
        {'tipo': 'success', 'mensaje': 'Backup automático completado', 'timestamp': now - timedelta(hours=2), 'severidad': 'info'},
        {'tipo': 'warning', 'mensaje': 'Latencia elevada en Content API (2800ms)', 'timestamp': now - timedelta(minutes=45), 'severidad': 'warning'},
        {'tipo': 'success', 'mensaje': 'Modelo de Churn actualizado (v2.3.1)', 'timestamp': now - timedelta(hours=5), 'severidad': 'success'},
        {'tipo': 'info', 'mensaje': 'Sincronización con Salesforce completada', 'timestamp': now - timedelta(minutes=15), 'severidad': 'info'},
        {'tipo': 'error', 'mensaje': 'Fallo temporal en conexión con Google Analytics', 'timestamp': now - timedelta(hours=1), 'severidad': 'error'},
        {'tipo': 'success', 'mensaje': 'Certificado SSL renovado automáticamente', 'timestamp': now - timedelta(hours=8), 'severidad': 'success'},
        {'tipo': 'info', 'mensaje': 'Nuevo usuario agregado: Sara Fernández', 'timestamp': now - timedelta(hours=3), 'severidad': 'info'},
        {'tipo': 'warning', 'mensaje': 'Uso de API cercano al límite (85%)', 'timestamp': now - timedelta(minutes=30), 'severidad': 'warning'}
    ]
    
    # Usuarios más activos
    usuarios_activos = [
        {'nombre': 'Ana Martínez', 'avatar': 'AM', 'acciones': 156, 'api_calls': 2340, 'ultimo_acceso': 'Hace 5 min'},
        {'nombre': 'Carlos Ruiz', 'avatar': 'CR', 'acciones': 142, 'api_calls': 1890, 'ultimo_acceso': 'Hace 12 min'},
        {'nombre': 'Laura Sánchez', 'avatar': 'LS', 'acciones': 128, 'api_calls': 1560, 'ultimo_acceso': 'Hace 8 min'},
        {'nombre': 'Miguel Torres', 'avatar': 'MT', 'acciones': 95, 'api_calls': 980, 'ultimo_acceso': 'Hace 25 min'},
        {'nombre': 'Elena García', 'avatar': 'EG', 'acciones': 87, 'api_calls': 750, 'ultimo_acceso': 'Hace 1 hora'}
    ]
    
    return render_template('monitorizacion.html',
                         metricas_sistema=metricas_sistema,
                         actividad_reciente=actividad_reciente,
                         uso_apis=uso_apis,
                         eventos_sistema=eventos_sistema,
                         usuarios_activos=usuarios_activos)

@app.route('/introduccion')
@login_required
def introduccion():
    # Estructura de documentación por categorías
    casos_uso_docs = [
        {
            'categoria': 'Customer Engagement',
            'casos': [
                {
                    'id': 'personalizacion',
                    'nombre': 'Personalización de Experiencias',
                    'icono': '👤',
                    'descripcion': 'Sistema de personalización basado en IA que adapta contenido, ofertas y experiencias a cada cliente individual.',
                    'enfoque_ia': 'Utiliza algoritmos de Collaborative Filtering y Deep Learning para analizar el comportamiento histórico del cliente y predecir sus preferencias futuras.',
                    'datos_entrada': 'Historial de navegación, transacciones pasadas, interacciones con campañas, datos demográficos, comportamiento en tiempo real.',
                    'procesamiento': 'Los datos se procesan mediante modelos de embeddings que capturan las relaciones entre usuarios y productos. Se aplican técnicas de Matrix Factorization y Neural Collaborative Filtering.',
                    'salida': 'Recomendaciones personalizadas de productos/servicios, contenido dinámico adaptado, ofertas específicas con scoring de propensión.',
                    'modelos': ['Collaborative Filtering', 'Matrix Factorization', 'Deep Learning (Neural CF)', 'Real-time Scoring']
                },
                {
                    'id': 'motor_recomendaciones',
                    'nombre': 'Motor de Recomendaciones',
                    'icono': '🎁',
                    'descripcion': 'Sistema de recomendaciones que sugiere productos y servicios relevantes basándose en patrones de comportamiento.',
                    'enfoque_ia': 'Combina filtrado colaborativo, content-based filtering y técnicas híbridas para generar recomendaciones precisas y diversas.',
                    'datos_entrada': 'Historial de compras, productos visualizados, ratings implícitos/explícitos, atributos de productos, contexto temporal.',
                    'procesamiento': 'Implementa algoritmos de factorización de matrices (SVD, ALS) y redes neuronales para capturar patrones complejos de preferencias.',
                    'salida': 'Top-N recomendaciones rankeadas por relevancia, explicaciones de por qué se recomienda cada ítem, diversidad controlada.',
                    'modelos': ['SVD', 'ALS', 'Item-based CF', 'Content-based', 'Hybrid Models']
                },
                {
                    'id': 'chatbot',
                    'nombre': 'Chatbot IA',
                    'icono': '💬',
                    'descripcion': 'Asistente conversacional inteligente que atiende consultas de clientes 24/7 con comprensión de lenguaje natural.',
                    'enfoque_ia': 'Utiliza Large Language Models (LLMs) con Retrieval-Augmented Generation (RAG) para respuestas contextuales y precisas.',
                    'datos_entrada': 'Consultas en lenguaje natural, historial de conversación, base de conocimiento corporativa, FAQs, documentación de productos.',
                    'procesamiento': 'El texto se procesa con NLU para extraer intención y entidades. RAG busca información relevante en la base de conocimiento y el LLM genera respuestas coherentes.',
                    'salida': 'Respuestas en lenguaje natural, acciones automatizadas (crear tickets, consultar estado), escalado a agente humano cuando necesario.',
                    'modelos': ['GPT-4', 'BERT (NLU)', 'Sentence Transformers', 'RAG', 'Intent Classification']
                }
            ]
        },
        {
            'categoria': 'Content & Creative',
            'casos': [
                {
                    'id': 'contenido_genai',
                    'nombre': 'Generación de Contenido con GenAI',
                    'icono': '✨',
                    'descripcion': 'Generación automatizada de contenido de marketing de alta calidad usando IA generativa.',
                    'enfoque_ia': 'Emplea modelos de lenguaje generativos (GPT-4, Claude) con prompts especializados y fine-tuning para mantener el tono de marca.',
                    'datos_entrada': 'Brief de campaña, tono de marca, audiencia objetivo, palabras clave, ejemplos de contenido previo, datos del producto/servicio.',
                    'procesamiento': 'Los prompts se estructuran con contexto de marca y objetivos. El modelo genera múltiples variantes que se filtran por calidad y coherencia.',
                    'salida': 'Emails de marketing, posts para redes sociales, artículos de blog, copy para landing pages, subject lines optimizados.',
                    'modelos': ['GPT-4', 'Claude 3', 'Llama 2', 'Fine-tuned Models', 'Content Quality Scoring']
                },
                {
                    'id': 'monitorizacion_marca',
                    'nombre': 'Monitorización de Marca',
                    'icono': '📢',
                    'descripcion': 'Seguimiento y análisis de menciones de marca en tiempo real con análisis de sentimiento.',
                    'enfoque_ia': 'Utiliza NLP avanzado para análisis de sentimiento multi-clase y detección de temas emergentes en redes sociales.',
                    'datos_entrada': 'Menciones en redes sociales (Twitter, Facebook, Instagram, LinkedIn), reviews, comentarios, artículos de prensa.',
                    'procesamiento': 'Text mining para extraer menciones relevantes, análisis de sentimiento con modelos transformer, clustering de temas, detección de tendencias.',
                    'salida': 'Score de sentimiento (positivo/neutral/negativo), temas trending, alertas de crisis, comparativa con competencia, insights accionables.',
                    'modelos': ['BERT Sentiment', 'RoBERTa', 'Topic Modeling (LDA)', 'Named Entity Recognition', 'Trend Detection']
                }
            ]
        },
        {
            'categoria': 'Campaign Optimization',
            'casos': [
                {
                    'id': 'optimizacion_publicitaria',
                    'nombre': 'Optimización Publicitaria',
                    'icono': '🎯',
                    'descripcion': 'Optimización automática de campañas publicitarias usando reinforcement learning y predicción de performance.',
                    'enfoque_ia': 'Implementa algoritmos de Reinforcement Learning (Multi-Armed Bandits) para optimización continua de bids y creatividades.',
                    'datos_entrada': 'Métricas de campañas (CTR, CPC, conversiones), datos de audiencia, creatividades, bids históricos, contexto temporal.',
                    'procesamiento': 'Modelos predictivos estiman el performance de cada combinación creatividad-audiencia-bid. RL ajusta la estrategia en tiempo real.',
                    'salida': 'Recomendaciones de ajuste de bids, pausar/activar campañas, cambios de segmentación, nuevas creatividades a testear.',
                    'modelos': ['Thompson Sampling', 'Contextual Bandits', 'Prophet (forecasting)', 'XGBoost', 'LSTM']
                },
                {
                    'id': 'ab_testing',
                    'nombre': 'A/B Testing Automatizado',
                    'icono': '🔬',
                    'descripcion': 'Sistema de experimentación automatizada con análisis estadístico riguroso y optimización bayesiana.',
                    'enfoque_ia': 'Utiliza inferencia bayesiana y Multi-Armed Bandits para balancear exploración y explotación durante los tests.',
                    'datos_entrada': 'Variantes a testear, métricas objetivo, tráfico disponible, restricciones de tiempo, priors históricos.',
                    'procesamiento': 'Cálculo de tamaño de muestra, asignación dinámica de tráfico con Thompson Sampling, análisis de significancia estadística continuo.',
                    'salida': 'Variante ganadora con nivel de confianza, lift estimado, momento óptimo para terminar el test, insights sobre segmentos.',
                    'modelos': ['Bayesian A/B Testing', 'Thompson Sampling', 'Sequential Testing', 'CUPED (variance reduction)']
                },
                {
                    'id': 'attribution_marketing',
                    'nombre': 'Modelos de Atribución',
                    'icono': '🔗',
                    'descripcion': 'Atribución multi-touch que determina la contribución real de cada canal al customer journey.',
                    'enfoque_ia': 'Implementa modelos algorítmicos (Shapley Value, Markov Chains) para atribución data-driven vs. reglas simples.',
                    'datos_entrada': 'Customer journeys completos, touchpoints en cada canal, timestamps, conversiones, valor de transacciones.',
                    'procesamiento': 'Construcción de grafos de transición entre canales, cálculo de Shapley Values para contribución marginal, simulaciones de Markov.',
                    'salida': 'Crédito de conversión por canal, ROI ajustado por atribución, recomendaciones de reasignación de presupuesto.',
                    'modelos': ['Shapley Value Attribution', 'Markov Chain Models', 'Time Decay', 'Position-based', 'Data-driven Attribution']
                }
            ]
        },
        {
            'categoria': 'Customer Intelligence',
            'casos': [
                {
                    'id': 'segmentacion_avanzada',
                    'nombre': 'Segmentación Avanzada de Clientes',
                    'icono': '🎯',
                    'descripcion': 'Segmentación automática de clientes basada en comportamiento, valor y propensión usando clustering avanzado.',
                    'enfoque_ia': 'Aplica algoritmos de clustering no supervisado (K-Means, DBSCAN) con reducción de dimensionalidad para identificar segmentos naturales.',
                    'datos_entrada': 'Datos transaccionales, comportamiento digital, datos demográficos, interacciones con servicio al cliente, engagement con campañas.',
                    'procesamiento': 'Feature engineering para crear variables significativas, PCA/t-SNE para reducción de dimensionalidad, clustering jerárquico y por densidad.',
                    'salida': 'Segmentos de clientes con perfiles detallados, tamaño y valor de cada segmento, estrategias de marketing personalizadas por segmento.',
                    'modelos': ['K-Means', 'DBSCAN', 'Hierarchical Clustering', 'PCA', 't-SNE', 'RFM Analysis']
                },
                {
                    'id': 'prediccion_churn',
                    'nombre': 'Predicción de Churn',
                    'icono': '📉',
                    'descripcion': 'Predicción temprana de abandono de clientes con análisis de factores de riesgo y recomendaciones de retención.',
                    'enfoque_ia': 'Utiliza modelos de clasificación supervisada (XGBoost, Random Forest) con técnicas de survival analysis para predecir probabilidad y timing de churn.',
                    'datos_entrada': 'Historial de uso del servicio, frecuencia de interacciones, tickets de soporte, cambios en patrones de consumo, datos de satisfacción.',
                    'procesamiento': 'Feature engineering de señales de riesgo, balanceo de clases (SMOTE), entrenamiento de ensemble models, calibración de probabilidades.',
                    'salida': 'Score de riesgo de churn (0-100), factores principales de riesgo, tiempo estimado hasta churn, acciones de retención recomendadas.',
                    'modelos': ['XGBoost', 'Random Forest', 'Survival Analysis', 'SHAP (explicabilidad)', 'Calibrated Classifiers']
                }
            ]
        }
    ]
    
    return render_template('introduccion.html', casos_uso_docs=casos_uso_docs)

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

# ==================== API ENDPOINTS ====================

@app.route('/api/save-menu-config', methods=['POST'])
@login_required
def save_menu_config():
    """Guarda la configuración del menú"""
    try:
        config = request.get_json()
        config_path = os.path.join(os.path.dirname(__file__), 'config', 'menu_config.json')
        
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        
        # Guardar configuración
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        # Recargar configuración
        global MENU_CONFIG
        MENU_CONFIG = load_menu_config()
        
        return jsonify({'success': True, 'message': 'Configuración guardada correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/reset-menu-config', methods=['POST'])
@login_required
def reset_menu_config():
    """Restaura la configuración del menú a los valores por defecto"""
    try:
        default_config = {
            "categories": [
                {
                    "id": "customer_engagement",
                    "title": "Customer Engagement",
                    "menu_items": [
                        {
                            "endpoint": "personalizacion",
                            "icon": "👤",
                            "menu_name": "Personalización",
                            "page_title": "Personalización Hiperpersonalizada"
                        },
                        {
                            "endpoint": "motor_recomendaciones",
                            "icon": "🎁",
                            "menu_name": "Recomendaciones",
                            "page_title": "Motor de Recomendaciones"
                        },
                        {
                            "endpoint": "chatbot",
                            "icon": "💬",
                            "menu_name": "Chatbot IA",
                            "page_title": "Chatbot IA Conversacional 24/7"
                        }
                    ]
                },
                {
                    "id": "content_creative",
                    "title": "Content & Creative",
                    "menu_items": [
                        {
                            "endpoint": "contenido_genai",
                            "icon": "✍️",
                            "menu_name": "Contenido GenAI",
                            "page_title": "Generación de Contenido con GenAI"
                        },
                        {
                            "endpoint": "monitorizacion_marca",
                            "icon": "📡",
                            "menu_name": "Monitorización",
                            "page_title": "Monitorización de Marca en Tiempo Real"
                        }
                    ]
                },
                {
                    "id": "campaign_optimization",
                    "title": "Campaign Optimization",
                    "menu_items": [
                        {
                            "endpoint": "optimizacion_publicitaria",
                            "icon": "🎯",
                            "menu_name": "Optimización Ads",
                            "page_title": "Optimización Publicitaria Autónoma"
                        },
                        {
                            "endpoint": "ab_testing",
                            "icon": "🧪",
                            "menu_name": "A/B Testing",
                            "page_title": "A/B Testing Automatizado con IA"
                        },
                        {
                            "endpoint": "attribution_marketing",
                            "icon": "🔗",
                            "menu_name": "Attribution",
                            "page_title": "Attribution Marketing Multi-Touch"
                        }
                    ]
                },
                {
                    "id": "customer_intelligence",
                    "title": "Customer Intelligence",
                    "menu_items": [
                        {
                            "endpoint": "segmentacion_avanzada",
                            "icon": "🔍",
                            "menu_name": "Segmentación",
                            "page_title": "Segmentación Avanzada de Clientes"
                        },
                        {
                            "endpoint": "prediccion_churn",
                            "icon": "📈",
                            "menu_name": "Predicción Churn",
                            "page_title": "Predicción y Prevención de Churn"
                        }
                    ]
                }
            ],
            "dashboard": {
                "icon": "📊",
                "menu_name": "Dashboard",
                "page_title": "Dashboard Principal"
            },
            "configuracion": {
                "icon": "⚙️",
                "menu_name": "Configuración",
                "page_title": "Configuración del Sistema"
            }
        }
        
        config_path = os.path.join(os.path.dirname(__file__), 'config', 'menu_config.json')
        
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        
        # Guardar configuración por defecto
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2, ensure_ascii=False)
        
        # Recargar configuración
        global MENU_CONFIG
        MENU_CONFIG = load_menu_config()
        
        return jsonify({'success': True, 'message': 'Configuración restaurada'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ==================== MANEJO DE ERRORES ====================

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

# ==================== FILTROS PERSONALIZADOS ====================

@app.template_filter('format_number')
def format_number(value):
    """Formatea números con separadores de miles"""
    try:
        return f"{int(value):,}".replace(',', '.')
    except:
        return value

@app.template_filter('format_currency')
def format_currency(value):
    """Formatea valores monetarios"""
    try:
        return f"€{int(value):,}".replace(',', '.')
    except:
        return value

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
