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
print("CORRIGIENDO CIERRE DE DOC-PANEL EN TEMPLATES")
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
    
    # Buscar el patrón problemático: doble salto de línea entre </div> y <div class="use-case-container">
    # y reemplazarlo por un solo salto
    pattern = r'(</div>\s*</div>\s*</div>\s*</div>)\s*\n\s*\n\s*\n+(<div class="use-case-container">)'
    replacement = r'\1\n\n\2'
    
    content_fixed = re.sub(pattern, replacement, content)
    
    if content_fixed != content:
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content_fixed)
        print(f"  [OK] Cierre corregido")
    else:
        print(f"  [INFO] No se encontraron problemas")

print()
print("=" * 80)
print("[COMPLETADO] Templates corregidos")
print("=" * 80)
