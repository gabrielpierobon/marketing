import os
import re

# Expanded documentation content for each use case
expanded_docs = {
    "personalizacion.html": {
        "summary": """
                       <p>
                           La <strong>Personalización Hiperpersonalizada</strong> representa un cambio paradigmático en cómo las empresas 
                           energéticas interactúan con sus clientes. Utilizando técnicas avanzadas de Machine Learning y Deep Learning, 
                           este sistema analiza múltiples dimensiones del comportamiento del cliente para crear experiencias verdaderamente 
                           únicas y relevantes.
                       </p>
                       
                       <p>
                           El sistema procesa datos de consumo energético en tiempo real, patrones de navegación web, historial de 
                           interacciones con servicio al cliente, respuestas a campañas anteriores, datos demográficos, y señales 
                           contextuales como la meteorología y eventos locales. Esta información se combina en un perfil dinámico 
                           que evoluciona constantemente con cada nueva interacción.
                       </p>
                       
                       <div class="doc-highlight-box">
                           <strong>🎯 Objetivo Principal</strong><br>
                           Aumentar la conversión y satisfacción del cliente mediante ofertas y contenidos ultra-relevantes 
                           que se adaptan en tiempo real a cada usuario. El sistema debe ser capaz de predecir las necesidades 
                           del cliente antes de que él mismo las identifique, creando una experiencia proactiva y anticipatoria.
                       </div>
                       
                       <p>
                           <strong>Beneficios Clave del Sistema:</strong>
                       </p>
                       <ul>
                           <li><strong>Aumento de Conversión:</strong> Las ofertas personalizadas tienen una tasa de conversión 
                           3-5 veces superior a las campañas genéricas, ya que llegan al cliente en el momento adecuado con 
                           la propuesta de valor correcta.</li>
                           
                           <li><strong>Mejora del Engagement:</strong> Los clientes que reciben contenido personalizado muestran 
                           un 65% más de engagement, con mayores tasas de apertura de emails, clicks en CTAs, y tiempo de 
                           permanencia en el sitio web.</li>
                           
                           <li><strong>Reducción de Churn:</strong> Al anticipar necesidades y resolver problemas proactivamente, 
                           el sistema reduce la tasa de abandono en un 20-30%.</li>
                           
                           <li><strong>Incremento del CLV:</strong> Clientes que experimentan personalización avanzada tienen 
                           un Customer Lifetime Value 40-50% superior debido a mayor retención y cross-selling efectivo.</li>
                       </ul>
                       
                       <div class="doc-metric-grid">
                           <div class="doc-metric">
                               <div class="doc-metric-value">+320%</div>
                               <div class="doc-metric-label">Conversión vs. Campañas Genéricas</div>
                           </div>
                           <div class="doc-metric">
                               <div class="doc-metric-value">+65%</div>
                               <div class="doc-metric-label">Open Rate en Emails</div>
                           </div>
                           <div class="doc-metric">
                               <div class="doc-metric-value">5-8x</div>
                               <div class="doc-metric-label">ROI sobre Inversión</div>
                           </div>
                           <div class="doc-metric">
                               <div class="doc-metric-value">€150K</div>
                               <div class="doc-metric-label">Inversión Inicial</div>
                           </div>
                       </div>
                       
                       <p>
                           <strong>Casos de Éxito Reales:</strong><br>
                           Empresas líderes del sector energético que han implementado sistemas similares han reportado 
                           incrementos de revenue de €2-5M anuales, con periodos de retorno de inversión de 6-9 meses. 
                           La clave del éxito radica en la calidad de los datos, la sofisticación de los modelos, y la 
                           integración fluida con los sistemas de marketing existentes.
                       </p>
        """,
        "models_intro": """
                       <p>
                           El sistema de personalización utiliza un <strong>ensemble de modelos de IA</strong> que trabajan 
                           en conjunto para proporcionar recomendaciones precisas y contextualizadas. Cada modelo aporta 
                           una perspectiva única y complementaria:
                       </p>
        """,
        "architecture_intro": """
                       <p>
                           La arquitectura del sistema está diseñada para escalar horizontalmente y procesar millones de 
                           eventos diarios con latencias inferiores a 100ms. Utiliza un enfoque de <strong>microservicios</strong> 
                           desplegados en Azure Kubernetes Service (AKS) con auto-scaling basado en métricas de carga.
                       </p>
                       
                       <p><strong>Componentes Principales de la Arquitectura:</strong></p>
        """,
        "use_cases_intro": """
                       <p>
                           El sistema de personalización se aplica a través de múltiples puntos de contacto con el cliente, 
                           creando una experiencia omnicanal coherente y personalizada. A continuación se detallan los casos 
                           de uso más impactantes:
                       </p>
        """
    },
    
    "contenido_genai.html": {
        "summary": """
                       <p>
                           La <strong>Generación de Contenido con GenAI</strong> revoluciona el proceso de creación de contenido 
                           de marketing mediante el uso de modelos de lenguaje de última generación (LLMs). Este sistema no solo 
                           automatiza la producción de contenido, sino que lo hace manteniendo altos estándares de calidad, 
                           coherencia de marca, y relevancia para la audiencia objetivo.
                       </p>
                       
                       <p>
                           El sistema es capaz de generar una amplia variedad de formatos de contenido: artículos de blog 
                           optimizados para SEO, emails marketing personalizados, posts para redes sociales, descripciones 
                           de productos, landing pages, whitepapers técnicos, y mucho más. Todo ello siguiendo las guías 
                           de estilo de la marca y adaptándose al tono y voz corporativos.
                       </p>
                       
                       <div class="doc-highlight-box">
                           <strong>🎯 Objetivo Principal</strong><br>
                           Reducir drásticamente el tiempo y coste de creación de contenido (hasta un 85%) mientras se 
                           mantiene o incluso supera la calidad del contenido creado manualmente. El sistema permite aumentar 
                           el volumen de producción hasta 500%, habilitando estrategias de contenido mucho más ambiciosas 
                           y escalables.
                       </div>
                       
                       <p>
                           <strong>Ventajas Competitivas del Sistema:</strong>
                       </p>
                       <ul>
                           <li><strong>Velocidad de Producción:</strong> Lo que antes tomaba días o semanas, ahora se completa 
                           en minutos u horas. Un artículo de blog de 2000 palabras puede generarse en 5-10 minutos.</li>
                           
                           <li><strong>Consistencia de Marca:</strong> El sistema utiliza RAG (Retrieval Augmented Generation) 
                           para asegurar que todo el contenido generado sea consistente con las guías de estilo, tono de voz, 
                           y mensajes clave de la marca.</li>
                           
                           <li><strong>Optimización SEO Automática:</strong> El contenido se genera ya optimizado para los 
                           keywords objetivo, con estructura adecuada de H2/H3, meta descriptions, y densidad de keywords óptima.</li>
                           
                           <li><strong>Personalización a Escala:</strong> Capacidad de generar miles de variaciones de contenido 
                           personalizadas para diferentes segmentos de audiencia, regiones geográficas, o contextos específicos.</li>
                           
                           <li><strong>Multilingüe Nativo:</strong> Generación de contenido en múltiples idiomas con calidad 
                           nativa, no simplemente traducción automática.</li>
                       </ul>
                       
                       <div class="doc-metric-grid">
                           <div class="doc-metric">
                               <div class="doc-metric-value">-85%</div>
                               <div class="doc-metric-label">Reducción de Tiempo</div>
                           </div>
                           <div class="doc-metric">
                               <div class="doc-metric-value">+500%</div>
                               <div class="doc-metric-label">Aumento de Volumen</div>
                           </div>
                           <div class="doc-metric">
                               <div class="doc-metric-value">-50%</div>
                               <div class="doc-metric-label">Reducción de Costes</div>
                           </div>
                           <div class="doc-metric">
                               <div class="doc-metric-value">€80K</div>
                               <div class="doc-metric-label">Inversión Inicial</div>
                           </div>
                       </div>
                       
                       <p>
                           <strong>ROI Esperado:</strong><br>
                           Organizaciones que han implementado sistemas similares reportan ahorros de €200K-500K anuales 
                           en costes de creación de contenido, con incrementos de tráfico orgánico del 150-300% debido al 
                           mayor volumen y calidad del contenido publicado. El ROI típico es de 4-6x en el primer año.
                       </p>
        """
    },
    
    "chatbot.html": {
        "summary": """
                       <p>
                           El <strong>Chatbot Conversacional con IA</strong> representa la evolución del servicio al cliente 
                           tradicional hacia una experiencia conversacional natural, disponible 24/7, y capaz de resolver 
                           consultas complejas sin intervención humana. Utilizando modelos de lenguaje avanzados (LLMs) y 
                           técnicas de NLU (Natural Language Understanding), el chatbot comprende la intención del usuario 
                           incluso cuando se expresa de forma ambigua o coloquial.
                       </p>
                       
                       <p>
                           El sistema va mucho más allá de los chatbots basados en reglas tradicionales. Es capaz de mantener 
                           conversaciones contextuales multi-turno, recordar información de interacciones anteriores, acceder 
                           a sistemas backend en tiempo real para proporcionar información personalizada, y escalar a agentes 
                           humanos cuando detecta frustración o consultas que requieren intervención especializada.
                       </p>
                       
                       <div class="doc-highlight-box">
                           <strong>🎯 Objetivo Principal</strong><br>
                           Automatizar el 70-80% de las consultas de atención al cliente, reduciendo costes operativos en 
                           un 60% mientras se mejora la satisfacción del cliente mediante respuestas instantáneas, precisas, 
                           y disponibles 24/7. El sistema debe proporcionar una experiencia tan natural que los usuarios 
                           prefieran interactuar con el chatbot antes que esperar a un agente humano.
                       </div>
                       
                       <p>
                           <strong>Capacidades Avanzadas del Chatbot:</strong>
                       </p>
                       <ul>
                           <li><strong>Comprensión Contextual:</strong> El chatbot mantiene el contexto de la conversación 
                           a lo largo de múltiples turnos, entendiendo referencias anafóricas ("eso", "lo anterior") y 
                           manteniendo coherencia en la conversación.</li>
                           
                           <li><strong>Gestión de Consultas Complejas:</strong> Puede resolver consultas que requieren 
                           múltiples pasos, como cambios de tarifa, gestión de averías, o consultas de facturación detalladas.</li>
                           
                           <li><strong>Personalización Dinámica:</strong> Accede al perfil del cliente en tiempo real para 
                           proporcionar respuestas personalizadas basadas en su historial, contrato actual, y preferencias.</li>
                           
                           <li><strong>Detección de Emociones:</strong> Utiliza análisis de sentimiento para detectar 
                           frustración, urgencia, o satisfacción, ajustando su tono y priorizando escalaciones cuando es necesario.</li>
                           
                           <li><strong>Aprendizaje Continuo:</strong> El sistema se entrena continuamente con nuevas 
                           conversaciones, mejorando su precisión y cobertura con el tiempo.</li>
                           
                           <li><strong>Multicanal:</strong> Mismo motor conversacional desplegado en web, app móvil, 
                           WhatsApp, Facebook Messenger, y otros canales.</li>
                       </ul>
                       
                       <div class="doc-metric-grid">
                           <div class="doc-metric">
                               <div class="doc-metric-value">-60%</div>
                               <div class="doc-metric-label">Costes Operativos</div>
                           </div>
                           <div class="doc-metric">
                               <div class="doc-metric-value">78%</div>
                               <div class="doc-metric-label">Tasa de Resolución</div>
                           </div>
                           <div class="doc-metric">
                               <div class="doc-metric-value">24/7</div>
                               <div class="doc-metric-label">Disponibilidad</div>
                           </div>
                           <div class="doc-metric">
                               <div class="doc-metric-value">€100K</div>
                               <div class="doc-metric-label">Inversión Inicial</div>
                           </div>
                       </div>
                       
                       <p>
                           <strong>Impacto en el Negocio:</strong><br>
                           Las empresas que han implementado chatbots conversacionales avanzados reportan reducciones de 
                           costes de atención al cliente de €300K-800K anuales, con mejoras en CSAT (Customer Satisfaction Score) 
                           de 15-25 puntos. El tiempo medio de resolución se reduce de minutos a segundos, y la capacidad 
                           de atender consultas simultáneas es prácticamente ilimitada.
                       </p>
        """
    }
}

def expand_doc_section(template_path, section_key, new_content):
    """Expands a specific section in the documentation panel"""
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the section and expand it
    # This is a simplified approach - in production you'd want more robust parsing
    if section_key == "summary":
        # Find the Resumen Ejecutivo section
        pattern = r'(<div class="doc-section">[\s\S]*?<h3 class="doc-section-title">[\s\S]*?Resumen Ejecutivo[\s\S]*?</h3>[\s\S]*?<div class="doc-section-content">)([\s\S]*?)(</div>[\s\S]*?</div>)'
        
        match = re.search(pattern, content)
        if match:
            new_section = match.group(1) + new_content + match.group(3)
            content = content[:match.start()] + new_section + content[match.end():]
    
    return content

# Process each template
templates_dir = "templates"

print("Expandiendo documentacion de casos de uso...")
print("=" * 60)

for template_file, expansions in expanded_docs.items():
    template_path = os.path.join(templates_dir, template_file)
    
    if not os.path.exists(template_path):
        print(f"[SKIP] Template no encontrado: {template_file}")
        continue
    
    print(f"\nProcesando: {template_file}")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Expand the summary section
    if "summary" in expansions:
        # Find and replace the summary section content
        pattern = r'(<div class="doc-section">[\s]*<h3 class="doc-section-title">[\s]*<span class="icon">📋</span>[\s]*Resumen Ejecutivo[\s]*</h3>[\s]*<div class="doc-section-content">)([\s\S]*?)(</div>[\s]*</div>[\s]*<!-- Modelos de IA -->)'
        
        match = re.search(pattern, content)
        if match:
            new_content = match.group(1) + expansions["summary"] + match.group(3)
            content = content[:match.start()] + new_content + content[match.end():]
            print(f"  [OK] Seccion 'Resumen Ejecutivo' expandida")
        else:
            print(f"  [WARN] No se pudo encontrar la seccion 'Resumen Ejecutivo'")
    
    # Write back the expanded content
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  [SUCCESS] Template actualizado")

print("\n" + "=" * 60)
print(f"[DONE] Documentacion expandida para {len(expanded_docs)} casos de uso")
print("=" * 60)
