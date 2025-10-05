#!/usr/bin/env python3
"""
Script para generar paneles de documentación para todos los casos de uso
"""

# Definición de casos de uso con su documentación
use_cases = {
    "prediccion_churn.html": {
        "icon": "📈",
        "title": "Predicción y Prevención de Churn",
        "description": "Sistema de ML para identificar clientes en riesgo",
        "metrics": [
            ("-25%", "Churn Rate"),
            ("+40%", "CLV"),
            ("92%", "Precisión"),
            ("€120K", "Inversión")
        ],
        "models": [
            {
                "name": "🌲 Gradient Boosting (XGBoost / LightGBM)",
                "desc": "Modelo principal para predicción de churn con alta precisión y capacidad de manejar features complejas.",
                "tech": [("XGBoost", "⚡"), ("LightGBM", "💡")]
            },
            {
                "name": "🧠 Random Forest",
                "desc": "Modelo ensemble para identificar patrones de comportamiento y feature importance.",
                "tech": [("Scikit-learn", "🔬"), ("Feature Importance", "📊")]
            },
            {
                "name": "📊 Survival Analysis (Cox PH)",
                "desc": "Análisis de supervivencia para estimar tiempo hasta el churn y factores de riesgo.",
                "tech": [("Lifelines", "⏱️"), ("Cox Model", "📈")]
            }
        ]
    },
    
    "chatbot.html": {
        "icon": "💬",
        "title": "Chatbot Inteligente con IA",
        "description": "Asistente virtual con NLP avanzado",
        "metrics": [
            ("24/7", "Disponibilidad"),
            ("-60%", "Tickets Soporte"),
            ("92%", "Satisfacción"),
            ("€90K", "Inversión")
        ],
        "models": [
            {
                "name": "🦜 GPT-4 / Claude 3",
                "desc": "LLM para comprensión y generación de respuestas naturales y contextuales.",
                "tech": [("OpenAI API", "🔷"), ("Anthropic", "🔶")]
            },
            {
                "name": "🔍 Embeddings + Semantic Search",
                "desc": "Búsqueda semántica en base de conocimiento para respuestas precisas.",
                "tech": [("Azure AI Search", "🔎"), ("Vector DB", "📚")]
            },
            {
                "name": "🎯 Intent Classification",
                "desc": "Clasificación de intenciones del usuario para routing inteligente.",
                "tech": [("BERT", "🤗"), ("Custom Models", "⚙️")]
            }
        ]
    },
    
    "optimizacion_publicitaria.html": {
        "icon": "📊",
        "title": "Optimización Publicitaria con IA",
        "description": "Optimización automática de campañas publicitarias",
        "metrics": [
            ("+180%", "ROAS"),
            ("-45%", "CPA"),
            ("+65%", "CTR"),
            ("€100K", "Inversión")
        ],
        "models": [
            {
                "name": "🎯 Multi-Armed Bandit",
                "desc": "Algoritmo para optimización en tiempo real de bids y creatividades.",
                "tech": [("Thompson Sampling", "🎲"), ("UCB", "📈")]
            },
            {
                "name": "📊 Propensity Modeling",
                "desc": "Predicción de probabilidad de conversión por usuario y anuncio.",
                "tech": [("XGBoost", "⚡"), ("Neural Networks", "🧠")]
            },
            {
                "name": "💰 Bid Optimization",
                "desc": "Optimización automática de pujas basada en objetivos de negocio.",
                "tech": [("Reinforcement Learning", "🤖"), ("AutoML", "🔧")]
            }
        ]
    },
    
    "segmentacion_avanzada.html": {
        "icon": "🎯",
        "title": "Segmentación Avanzada con ML",
        "description": "Segmentación inteligente de clientes",
        "metrics": [
            ("+250%", "Relevancia"),
            ("15-20", "Segmentos"),
            ("+85%", "Conversión"),
            ("€70K", "Inversión")
        ],
        "models": [
            {
                "name": "🔷 K-Means / DBSCAN",
                "desc": "Clustering no supervisado para identificar grupos naturales de clientes.",
                "tech": [("Scikit-learn", "🔬"), ("PCA", "📊")]
            },
            {
                "name": "🧠 Deep Clustering (Autoencoders)",
                "desc": "Aprendizaje de representaciones latentes para segmentación avanzada.",
                "tech": [("TensorFlow", "🔷"), ("PyTorch", "🔶")]
            },
            {
                "name": "📈 RFM + Behavioral Scoring",
                "desc": "Segmentación basada en Recency, Frequency, Monetary y comportamiento.",
                "tech": [("Custom Scoring", "⚙️"), ("SQL Analytics", "📊")]
            }
        ]
    },
    
    "ab_testing.html": {
        "icon": "🧪",
        "title": "A/B Testing Inteligente",
        "description": "Experimentación y optimización continua",
        "metrics": [
            ("+120%", "Velocidad Tests"),
            ("95%", "Confianza"),
            ("+45%", "Conversión"),
            ("€60K", "Inversión")
        ],
        "models": [
            {
                "name": "📊 Bayesian A/B Testing",
                "desc": "Análisis bayesiano para decisiones más rápidas y confiables.",
                "tech": [("PyMC3", "🔬"), ("Stan", "📈")]
            },
            {
                "name": "🎯 Multi-Armed Bandit",
                "desc": "Optimización continua que balancea exploración y explotación.",
                "tech": [("Thompson Sampling", "🎲"), ("Epsilon-Greedy", "⚡")]
            },
            {
                "name": "🤖 Sequential Testing",
                "desc": "Tests secuenciales que permiten parar antes con resultados concluyentes.",
                "tech": [("SPRT", "📊"), ("mSPRT", "🔍")]
            }
        ]
    },
    
    "monitorizacion_marca.html": {
        "icon": "👁️",
        "title": "Monitorización de Marca con IA",
        "description": "Análisis de sentimiento y reputación online",
        "metrics": [
            ("24/7", "Monitoreo"),
            ("+300%", "Cobertura"),
            ("90%", "Precisión"),
            ("€85K", "Inversión")
        ],
        "models": [
            {
                "name": "💬 Sentiment Analysis (BERT / RoBERTa)",
                "desc": "Análisis de sentimiento avanzado en múltiples idiomas y contextos.",
                "tech": [("BERT", "🤗"), ("RoBERTa", "🔷")]
            },
            {
                "name": "🔍 Named Entity Recognition (NER)",
                "desc": "Extracción de entidades (marcas, productos, personas) de textos.",
                "tech": [("spaCy", "🚀"), ("Custom NER", "⚙️")]
            },
            {
                "name": "📊 Topic Modeling",
                "desc": "Identificación automática de temas y tendencias en conversaciones.",
                "tech": [("LDA", "📈"), ("BERTopic", "🎯")]
            }
        ]
    },
    
    "motor_recomendaciones.html": {
        "icon": "🎁",
        "title": "Motor de Recomendaciones",
        "description": "Sistema de recomendaciones personalizado",
        "metrics": [
            ("+280%", "Cross-sell"),
            ("+55%", "AOV"),
            ("4-6x", "ROI"),
            ("€110K", "Inversión")
        ],
        "models": [
            {
                "name": "🧠 Collaborative Filtering",
                "desc": "Recomendaciones basadas en similitud entre usuarios y productos.",
                "tech": [("ALS", "⚡"), ("SVD++", "📊")]
            },
            {
                "name": "🎯 Content-Based Filtering",
                "desc": "Recomendaciones basadas en características de productos y preferencias.",
                "tech": [("TF-IDF", "📝"), ("Embeddings", "🔷")]
            },
            {
                "name": "🤖 Deep Learning (Neural CF)",
                "desc": "Redes neuronales para capturar patrones complejos de preferencias.",
                "tech": [("TensorFlow", "🔷"), ("PyTorch", "🔶")]
            }
        ]
    },
    
    "attribution_marketing.html": {
        "icon": "🔗",
        "title": "Attribution Marketing con ML",
        "description": "Atribución multi-touch con algoritmos avanzados",
        "metrics": [
            ("+150%", "Precisión"),
            ("+40%", "ROI"),
            ("100%", "Visibilidad"),
            ("€95K", "Inversión")
        ],
        "models": [
            {
                "name": "📊 Markov Chain Attribution",
                "desc": "Modelo probabilístico para atribuir valor a cada touchpoint del customer journey.",
                "tech": [("Markov Models", "🔗"), ("Transition Matrix", "📈")]
            },
            {
                "name": "🎯 Shapley Value",
                "desc": "Teoría de juegos para distribución justa del valor de conversión.",
                "tech": [("Game Theory", "🎮"), ("SHAP", "🔍")]
            },
            {
                "name": "🧠 Deep Learning Attribution",
                "desc": "LSTM/Transformers para modelar secuencias complejas de touchpoints.",
                "tech": [("LSTM", "🔷"), ("Transformers", "🤖")]
            }
        ]
    }
}

# Template HTML para el panel de documentación
def generate_panel_html(use_case_data):
    icon = use_case_data["icon"]
    title = use_case_data["title"]
    description = use_case_data["description"]
    metrics = use_case_data["metrics"]
    models = use_case_data["models"]
    
    # Generar HTML de métricas
    metrics_html = ""
    for value, label in metrics:
        metrics_html += f"""
                    <div class="doc-metric">
                        <div class="doc-metric-value">{value}</div>
                        <div class="doc-metric-label">{label}</div>
                    </div>"""
    
    # Generar HTML de modelos
    models_html = ""
    for model in models:
        tech_html = ""
        for tech_name, tech_icon in model["tech"]:
            tech_html += f"""
                        <div class="doc-tech-item">
                            <div class="doc-tech-icon">{tech_icon}</div>
                            <div class="doc-tech-name">{tech_name}</div>
                        </div>"""
        
        models_html += f"""
                <div class="doc-model-card">
                    <div class="doc-model-name">
                        {model["name"]}
                    </div>
                    <div class="doc-model-desc">
                        {model["desc"]}
                    </div>
                    <div class="doc-tech-stack">{tech_html}
                    </div>
                </div>
                """
    
    panel_html = f"""<!-- Documentation Panel Toggle -->
<button class="doc-panel-toggle" aria-label="Ocultar documentación">
    <span class="icon">📚</span>
    <span>Ocultar Panel</span>
</button>

<!-- Documentation Panel -->
<div class="doc-panel">
    <div class="doc-panel-header">
        <div class="doc-panel-title">
            <h2>{icon} {title}</h2>
            <p>Guía técnica completa del caso de uso</p>
        </div>
        <div class="doc-panel-header-actions">
            <button class="doc-edit-btn" aria-label="Editar documentación">
                <span>✏️</span> Editar
            </button>
            <button class="doc-panel-close" aria-label="Cerrar">×</button>
        </div>
    </div>
    
    <div class="doc-panel-content">
        <!-- Resumen -->
        <div class="doc-section">
            <h3 class="doc-section-title">
                <span class="icon">📋</span>
                Resumen Ejecutivo
            </h3>
            <div class="doc-section-content">
                <p>
                    <strong>{title}</strong>: {description}
                </p>
                
                <div class="doc-metric-grid">{metrics_html}
                </div>
            </div>
        </div>
        
        <!-- Modelos de IA -->
        <div class="doc-section">
            <h3 class="doc-section-title">
                <span class="icon">🤖</span>
                Modelos de IA Aplicados
            </h3>
            <div class="doc-section-content">{models_html}
            </div>
        </div>
        
        <!-- Arquitectura Técnica -->
        <div class="doc-section">
            <h3 class="doc-section-title">
                <span class="icon">🏗️</span>
                Arquitectura Técnica
            </h3>
            <div class="doc-section-content">
                <p><strong>Stack Tecnológico:</strong></p>
                <ul>
                    <li>Azure Machine Learning para entrenamiento y deployment</li>
                    <li>Azure Databricks para procesamiento de datos</li>
                    <li>Azure Synapse Analytics para data warehousing</li>
                    <li>Power BI para visualización y reporting</li>
                    <li>Azure DevOps para CI/CD de modelos</li>
                </ul>
                
                <p><strong>Flujo de Datos:</strong></p>
                <ol class="doc-steps">
                    <li>
                        <strong>Ingesta de Datos</strong><br>
                        Recopilación de datos desde múltiples fuentes (CRM, web, transaccional).
                    </li>
                    <li>
                        <strong>Procesamiento y Feature Engineering</strong><br>
                        Limpieza, transformación y creación de variables predictivas.
                    </li>
                    <li>
                        <strong>Entrenamiento de Modelos</strong><br>
                        Entrenamiento y validación de modelos con MLOps.
                    </li>
                    <li>
                        <strong>Deployment y Scoring</strong><br>
                        Despliegue de modelos como APIs REST para inferencia en tiempo real.
                    </li>
                    <li>
                        <strong>Monitorización y Reentrenamiento</strong><br>
                        Seguimiento de performance y reentrenamiento automático.
                    </li>
                </ol>
            </div>
        </div>
        
        <!-- KPIs -->
        <div class="doc-section">
            <h3 class="doc-section-title">
                <span class="icon">📊</span>
                KPIs y Métricas de Éxito
            </h3>
            <div class="doc-section-content">
                <p><strong>Métricas Técnicas:</strong></p>
                <ul>
                    <li>Precisión, Recall, F1-Score del modelo</li>
                    <li>AUC-ROC y AUC-PR para clasificación</li>
                    <li>Latencia de inferencia (p50, p95, p99)</li>
                    <li>Cobertura de predicciones</li>
                </ul>
                
                <p><strong>Métricas de Negocio:</strong></p>
                <ul>
                    <li>ROI del caso de uso</li>
                    <li>Impacto en KPIs clave de negocio</li>
                    <li>Adopción por usuarios finales</li>
                    <li>Satisfacción del cliente</li>
                </ul>
            </div>
        </div>
    </div>
</div>

"""
    return panel_html


# Generar archivos
if __name__ == "__main__":
    print("Generando paneles de documentación...")
    
    for filename, data in use_cases.items():
        panel_html = generate_panel_html(data)
        
        # Guardar en archivo temporal
        output_file = f"doc_panel_{filename}"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(panel_html)
        
        print(f"[OK] Generado: {output_file}")
    
    print(f"\n[SUCCESS] {len(use_cases)} paneles generados exitosamente!")
    print("\nAhora debes copiar manualmente cada panel al inicio de su template correspondiente.")
