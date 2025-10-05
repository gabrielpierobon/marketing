import os
import re

templates_to_fix = [
    "optimizacion_publicitaria.html",
    "segmentacion_avanzada.html",
    "ab_testing.html",
    "monitorizacion_marca.html",
    "motor_recomendaciones.html",
    "attribution_marketing.html"
]

templates_dir = "templates"

print("=" * 80)
print("CORRIGIENDO ESTRUCTURA DE DOC-PANEL (3 SALTOS DE LINEA)")
print("=" * 80)
print()

for template_file in templates_to_fix:
    template_path = os.path.join(templates_dir, template_file)
    
    if not os.path.exists(template_path):
        print(f"[SKIP] {template_file} - No encontrado")
        continue
    
    print(f"[PROCESANDO] {template_file}")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar el patrón: cierre de doc-panel seguido de apertura de use-case-container
    # Debe haber exactamente 3 saltos de línea (2 líneas vacías)
    
    # Primero, normalizar cualquier cantidad de saltos de línea a exactamente 3
    pattern = r'(</div>\s*</div>\s*</div>\s*</div>)\s*\n+(<div class="use-case-container">)'
    replacement = r'\1\n\n\n\n<div class="use-case-container">'
    
    content_fixed = re.sub(pattern, replacement, content)
    
    if content_fixed != content:
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content_fixed)
        print(f"  [OK] Estructura corregida - 3 saltos de linea")
    else:
        print(f"  [INFO] No se encontraron cambios necesarios")

print()
print("=" * 80)
print("[COMPLETADO] Todos los templates corregidos")
print("=" * 80)
