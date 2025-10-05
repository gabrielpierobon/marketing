import os
import re

templates_to_fix = [
    "prediccion_churn.html",
    "segmentacion_avanzada.html",
    "ab_testing.html",
    "monitorizacion_marca.html",
    "motor_recomendaciones.html",
    "attribution_marketing.html"
]

templates_dir = "templates"

print("=" * 80)
print("CORRIGIENDO SECCION DE ARQUITECTURA TECNICA")
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
    
    # Buscar el patrón donde falta el div de doc-section-content después de Arquitectura Técnica
    pattern = r'(<!-- Arquitectura Técnica -->\s*<div class="doc-section">\s*<h3 class="doc-section-title">\s*<span class="icon">🏗️</span>\s*Arquitectura Técnica\s*</h3>)\s*\n\s*(<p>)'
    
    replacement = r'\1\n            <div class="doc-section-content">\n                \2'
    
    content_fixed = re.sub(pattern, replacement, content)
    
    if content_fixed != content:
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content_fixed)
        print(f"  [OK] Div doc-section-content anadido")
    else:
        print(f"  [INFO] No se encontraron cambios necesarios")

print()
print("=" * 80)
print("[COMPLETADO] Todos los templates corregidos")
print("=" * 80)
