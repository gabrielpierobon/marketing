#!/usr/bin/env python3
"""
Script para aplicar paneles de documentación a los templates
"""
import os

# Mapeo de archivos de paneles a templates
mappings = {
    "doc_panel_prediccion_churn.html": "templates/prediccion_churn.html",
    "doc_panel_chatbot.html": "templates/chatbot.html",
    "doc_panel_optimizacion_publicitaria.html": "templates/optimizacion_publicitaria.html",
    "doc_panel_segmentacion_avanzada.html": "templates/segmentacion_avanzada.html",
    "doc_panel_ab_testing.html": "templates/ab_testing.html",
    "doc_panel_monitorizacion_marca.html": "templates/monitorizacion_marca.html",
    "doc_panel_motor_recomendaciones.html": "templates/motor_recomendaciones.html",
    "doc_panel_attribution_marketing.html": "templates/attribution_marketing.html"
}

def apply_panel_to_template(panel_file, template_file):
    """Aplica un panel de documentación a un template"""
    
    # Leer el panel
    with open(panel_file, 'r', encoding='utf-8') as f:
        panel_content = f.read()
    
    # Leer el template
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Buscar la línea {% block content %}
    search_str = "{% block content %}"
    
    if search_str not in template_content:
        print(f"  [ERROR] No se encontró '{{%% block content %%}}' en {template_file}")
        return False
    
    # Insertar el panel justo después de {% block content %}
    parts = template_content.split(search_str, 1)
    
    if len(parts) != 2:
        print(f"  [ERROR] No se pudo dividir el template {template_file}")
        return False
    
    # Construir el nuevo contenido
    new_content = parts[0] + search_str + "\n" + panel_content + "\n" + parts[1]
    
    # Guardar el template actualizado
    with open(template_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

if __name__ == "__main__":
    print("Aplicando paneles de documentación a templates...\n")
    
    success_count = 0
    error_count = 0
    
    for panel_file, template_file in mappings.items():
        if not os.path.exists(panel_file):
            print(f"[SKIP] {panel_file} no existe")
            error_count += 1
            continue
        
        if not os.path.exists(template_file):
            print(f"[SKIP] {template_file} no existe")
            error_count += 1
            continue
        
        print(f"Procesando: {template_file}")
        
        if apply_panel_to_template(panel_file, template_file):
            print(f"  [OK] Panel aplicado exitosamente\n")
            success_count += 1
        else:
            print(f"  [ERROR] Fallo al aplicar panel\n")
            error_count += 1
    
    print(f"\n{'='*50}")
    print(f"[SUCCESS] {success_count} paneles aplicados correctamente")
    if error_count > 0:
        print(f"[ERROR] {error_count} paneles fallaron")
    print(f"{'='*50}")
