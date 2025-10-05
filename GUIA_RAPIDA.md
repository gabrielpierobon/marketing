# 🚀 Guía Rápida - Iberdrola AI Marketing Suite

## Inicio Rápido (3 pasos)

### 1. Ejecutar la Aplicación

**Opción A - Usando el archivo start.bat (Recomendado):**
```bash
start.bat
```

**Opción B - Manual:**
```bash
.\venv\Scripts\Activate.ps1
python app.py
```

### 2. Abrir en el Navegador

Navega a: **http://localhost:5555**

### 3. Iniciar Sesión

Usa cualquiera de estas credenciales:
- **Email:** `admin@iberdrola.com` | **Contraseña:** `demo2025`
- **Email:** `marketing@iberdrola.com` | **Contraseña:** `demo2025`
- **Email:** `demo@iberdrola.com` | **Contraseña:** `demo2025`

---

## 📱 Navegación de la Plataforma

### Dashboard Principal
- Vista general de métricas clave
- Actividad reciente
- Accesos rápidos a casos de uso
- Alertas IA en tiempo real

### Casos de Uso Disponibles

#### 1. 👤 Personalización Hiperpersonalizada
- Genera ofertas personalizadas por perfil de cliente
- **Demo:** Selecciona tipo de cliente (Residencial, Negocio, Alto Consumo)
- **Resultado:** Oferta completa con datos del cliente y propuesta personalizada

#### 2. ✍️ Generación de Contenido GenAI
- Crea campañas de email automáticamente
- **Demo:** Selecciona objetivo y tono de campaña
- **Resultado:** Email completo con asunto, cuerpo y CTA optimizado

#### 3. 💬 Chatbot IA Conversacional
- Asistente virtual 24/7
- **Demo:** Escribe preguntas o usa botones rápidos
- **Resultado:** Respuestas inteligentes con acciones sugeridas

#### 4. 📈 Predicción de Churn
- Identifica clientes en riesgo
- **Demo:** Click en cualquier cliente de la lista
- **Resultado:** Análisis completo con factores de riesgo y acciones recomendadas

#### 5. 🎯 Optimización Publicitaria
- Mejora automática de campañas
- **Demo:** Click en "Ejecutar Optimización IA"
- **Resultado:** Comparativa antes/después con métricas de mejora

#### 6. 🔍 Segmentación Avanzada
- Agrupa clientes inteligentemente
- **Vista:** Segmentos identificados con potencial de cada uno

#### 7. 🧪 A/B Testing Automatizado
- Tests continuos de optimización
- **Vista:** Resultados de tests activos con ganadores

#### 8. 📡 Monitorización de Marca
- Análisis de sentimiento en tiempo real
- **Vista:** Menciones recientes en redes sociales con clasificación

#### 9. 🎁 Motor de Recomendaciones
- Sugerencias personalizadas de productos
- **Vista:** Métricas de adopción y engagement

#### 10. 🔗 Attribution Marketing
- Optimización de inversión multi-touch
- **Vista:** Análisis de ROI por canal

---

## 🎨 Características de la Interfaz

### Sidebar de Navegación
- **Fijo a la izquierda** - Siempre visible
- **Organizado por secciones** - Dashboard, Casos de Uso, Configuración
- **Indicador visual** - Página activa resaltada
- **Perfil de usuario** - En la parte inferior con opción de logout

### Elementos Interactivos
- **Botones de acción** - Ejecutan demos en tiempo real
- **Animaciones suaves** - Feedback visual de acciones
- **Loading states** - Indicadores de procesamiento
- **Mensajes flash** - Notificaciones de éxito/error

### Responsive Design
- ✅ Desktop (1920px+)
- ✅ Laptop (1366px+)
- ✅ Tablet (768px+)
- ✅ Mobile (320px+)

---

## 💡 Tips de Uso

### Para Demos Efectivas

1. **Dashboard Primero**
   - Muestra las métricas generales
   - Explica el ROI esperado (4:1 a 6:1)
   - Destaca las alertas IA

2. **Personalización**
   - Empieza con cliente residencial
   - Muestra cómo la IA analiza consumo
   - Destaca el ahorro específico calculado

3. **Contenido GenAI**
   - Genera varios contenidos diferentes
   - Muestra la velocidad (2-3 segundos)
   - Resalta el score de calidad predicho

4. **Chatbot**
   - Usa las preguntas rápidas primero
   - Muestra respuestas con acciones
   - Destaca la disponibilidad 24/7

5. **Predicción Churn**
   - Analiza un cliente de alto riesgo
   - Muestra factores detectados
   - Explica acciones automatizadas

### Datos de Impacto para Presentaciones

- **11.2M+ clientes activos** en la plataforma
- **ROI 5.8:1** promedio actual
- **€142K ahorro mensual** en marketing
- **42.3% engagement rate** (vs 15-20% industria)
- **18.5% reducción churn** lograda
- **67% open rate** emails (vs 20-25% industria)

---

## 🔧 Personalización Rápida

### Cambiar Colores de Marca

Edita `static/css/style.css` líneas 2-10:
```css
:root {
    --primary: #0078D4;      /* Color principal */
    --success: #107C10;      /* Verde éxito */
    --warning: #FFB900;      /* Amarillo alerta */
    --danger: #D13438;       /* Rojo peligro */
}
```

### Agregar Nuevo Usuario

Edita `app.py` líneas 16-38, agrega:
```python
'nuevo@iberdrola.com': {
    'password': 'contraseña',
    'nombre': 'Nombre Completo',
    'rol': 'Rol',
    'empresa': 'Iberdrola España',
    'avatar': 'NC'
}
```

### Modificar Métricas del Dashboard

Edita `app.py` función `dashboard()` líneas 71-82

---

## 🐛 Solución de Problemas

### La aplicación no inicia
```bash
# Verifica que el venv esté activado
.\venv\Scripts\Activate.ps1

# Reinstala dependencias
pip install -r requirements.txt

# Verifica el puerto
# Si 5555 está ocupado, cambia en app.py línea final
```

### Error de importación Flask
```bash
# Asegúrate de estar en el venv
.\venv\Scripts\Activate.ps1

# Reinstala Flask
pip install Flask==3.0.0
```

### Estilos no se cargan
```bash
# Verifica que exista la carpeta static/css/
# Limpia caché del navegador (Ctrl + F5)
```

### Sesión expira rápido
```python
# Edita app.py línea 15
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
```

---

## 📊 Estructura de Datos Simulados

### Clientes (Predicción Churn)
- 5 clientes de ejemplo con diferentes niveles de riesgo
- Datos: ID, nombre, antigüedad, riesgo %, valor lifetime

### Campañas (Optimización)
- 5 campañas activas con métricas reales
- Datos: presupuesto, impresiones, clicks, conversiones, ROAS

### Segmentos (Segmentación)
- 5 segmentos identificados por IA
- Datos: nombre, tamaño, potencial, valor promedio

### Tests A/B
- 4 tests activos con resultados
- Datos: variantes, ganador, mejora porcentual

---

## 🚀 Próximos Pasos

### Para Desarrollo
1. Integrar APIs reales de IA (OpenAI, Claude, Gemini)
2. Conectar base de datos PostgreSQL
3. Implementar autenticación OAuth
4. Agregar gráficos con Chart.js
5. Exportación de reportes PDF

### Para Producción
1. Cambiar SECRET_KEY
2. Configurar HTTPS
3. Usar Gunicorn/uWSGI
4. Configurar reverse proxy (Nginx)
5. Implementar rate limiting

---

## 📞 Soporte

Para preguntas o problemas:
1. Revisa el README.md completo
2. Verifica la sección de solución de problemas
3. Contacta al equipo de desarrollo

---

**¡Disfruta explorando la plataforma!** 🎉
