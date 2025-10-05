"""
Iberdrola AI Marketing Suite - Plataforma SaaS
Sistema completo de IA para marketing digital en el sector energético
"""

from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from functools import wraps
from datetime import datetime, timedelta
import random
import json

app = Flask(__name__)
app.secret_key = 'iberdrola-ai-suite-2025-secret-key-change-in-production'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)

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
    return render_template('contenido_genai.html')

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
    return render_template('chatbot.html')

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
    # Lista de clientes con riesgo
    clientes_riesgo = [
        {'id': 'CL-28492', 'nombre': 'Juan Martínez', 'riesgo': 87, 'nivel': 'alto', 'valor': 4280},
        {'id': 'CL-19283', 'nombre': 'Ana Castro', 'riesgo': 42, 'nivel': 'medio', 'valor': 6420},
        {'id': 'CL-31847', 'nombre': 'Pedro Sánchez', 'riesgo': 78, 'nivel': 'alto', 'valor': 3890},
        {'id': 'CL-24891', 'nombre': 'Laura Fernández', 'riesgo': 35, 'nivel': 'medio', 'valor': 5120},
        {'id': 'CL-09471', 'nombre': 'Laura Gómez', 'riesgo': 12, 'nivel': 'bajo', 'valor': 12850}
    ]
    
    return render_template('prediccion_churn.html', clientes=clientes_riesgo)

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
    return render_template('optimizacion_publicitaria.html')

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
    segmentos = [
        {'nombre': 'Alto Consumo Verano', 'clientes': 45230, 'potencial': 'Solar + Piscina', 'valor': '€185/mes'},
        {'nombre': 'PYME Hostelería', 'clientes': 12847, 'potencial': 'Optimización Energética', 'valor': '€420/mes'},
        {'nombre': 'Propietarios EV', 'clientes': 8934, 'potencial': 'Tarifa Super Valle', 'valor': '€95/mes'},
        {'nombre': 'Casas Antiguas', 'clientes': 34521, 'potencial': 'Auditoría Energética', 'valor': '€145/mes'},
        {'nombre': 'Familias Numerosas', 'clientes': 23456, 'potencial': 'Plan Familiar Plus', 'valor': '€78/mes'}
    ]
    return render_template('segmentacion_avanzada.html', segmentos=segmentos)

@app.route('/ab-testing')
@login_required
def ab_testing():
    tests = [
        {'nombre': 'Subject Line Solar', 'variante_a': 'Ahorra con Solar', 'variante_b': 'URGENTE: Solar', 'ganador': 'B', 'mejora': '+34%'},
        {'nombre': 'CTA Button Color', 'variante_a': 'Azul', 'variante_b': 'Verde', 'ganador': 'A', 'mejora': '+12%'},
        {'nombre': 'Landing Page Layout', 'variante_a': 'Formulario Arriba', 'variante_b': 'Video Arriba', 'ganador': 'B', 'mejora': '+28%'},
        {'nombre': 'Email Timing', 'variante_a': '9:00 AM', 'variante_b': '7:00 PM', 'ganador': 'B', 'mejora': '+19%'}
    ]
    return render_template('ab_testing.html', tests=tests)

@app.route('/monitorizacion-marca')
@login_required
def monitorizacion_marca():
    menciones = [
        {'fuente': 'Twitter', 'sentimiento': 'positivo', 'texto': 'Excelente servicio de @Iberdrola, resolvieron mi problema en minutos', 'tiempo': '5 min'},
        {'fuente': 'Facebook', 'sentimiento': 'neutral', 'texto': '¿Alguien tiene experiencia con paneles solares de Iberdrola?', 'tiempo': '23 min'},
        {'fuente': 'Instagram', 'sentimiento': 'positivo', 'texto': 'Mi casa ahora funciona 100% con energía solar gracias a Iberdrola 🌞', 'tiempo': '1 hora'},
        {'fuente': 'Twitter', 'sentimiento': 'negativo', 'texto': 'Llevo 2 días esperando respuesta sobre mi factura @Iberdrola', 'tiempo': '2 horas'}
    ]
    return render_template('monitorizacion_marca.html', menciones=menciones)

@app.route('/motor-recomendaciones')
@login_required
def motor_recomendaciones():
    return render_template('motor_recomendaciones.html')

@app.route('/attribution-marketing')
@login_required
def attribution_marketing():
    return render_template('attribution_marketing.html')

# ==================== CONFIGURACIÓN Y PERFIL ====================

@app.route('/configuracion')
@login_required
def configuracion():
    return render_template('configuracion.html')

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

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
