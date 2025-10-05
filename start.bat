@echo off
echo ========================================
echo Iberdrola AI Marketing Suite
echo ========================================
echo.
echo Activando entorno virtual...
call venv\Scripts\activate.bat

echo Iniciando servidor Flask...
echo.
echo La aplicacion estara disponible en:
echo http://localhost:5555
echo.
echo Credenciales de demo:
echo - admin@iberdrola.com / demo2025
echo - marketing@iberdrola.com / demo2025
echo - demo@iberdrola.com / demo2025
echo.
echo Presiona Ctrl+C para detener el servidor
echo ========================================
echo.

python app.py
