# HealthTrack System – Evaluación Módulo 4

**Autor:** Victor Figueroa  
**Curso:** Módulo 4: *Automatización de Pruebas en una Plataforma de Salud*  
**Repositorio:** https://github.com/Victfigueroa/healthtrack-system  

---

## Descripción del Proyecto

Este repositorio corresponde a la evaluación práctica del Módulo 4, en la cual se desarrolló un sistema completo de pruebas automatizadas para una aplicación web de salud. La plataforma permite a los usuarios ingresar y actualizar su peso corporal, corrigiendo un bug crítico que originalmente restaba 1 kg en cada actualización.

El proyecto cubre todo el ciclo de aseguramiento de calidad: desde la identificación del error hasta la implementación de pruebas unitarias, funcionales, de regresión y de rendimiento, integradas en un pipeline CI/CD con GitHub Actions y SonarCloud.

---

## Tipos de Pruebas Implementadas

- **Pruebas unitarias** con `pytest`: Validan la lógica interna de la clase `Usuario`.
- **Pruebas funcionales** con `Selenium`: Simulan el flujo real del usuario en el formulario web.
- **Pruebas de regresión**: Agrupadas e integradas en el pipeline para validación continua.
- **Pruebas de rendimiento** con JMeter: Miden eficiencia bajo carga y tiempos de respuesta.

---

## Integración Continua y DevOps

El pipeline de CI/CD está configurado con [GitHub Actions](.github/workflows/ci-cd-healthtrack.yml), incluyendo:

- Instalación de dependencias.
- Servidor web para el formulario.
- Ejecución de pruebas unitarias y funcionales.
- Generación de reporte de cobertura con `pytest-cov`.
- Escaneo estático con SonarQube Cloud.

> ✅ Todas las etapas del pipeline se ejecutan automáticamente al hacer push o pull request sobre `main`.

---

## Enlaces Relevantes

### 🔗 [Simulación de Formulario Web](https://victfigueroa.github.io/healthtrack-system/)  
Visualización de la interfaz del formulario corregido. Permite simular la entrada del usuario y observar el flujo funcional con el bug ya resuelto.

### 🔗 [Reporte de Cobertura de Código](https://victfigueroa.github.io/healthtrack-system/coverage/)  
Informe HTML generado con `pytest-cov`. Muestra una cobertura del 83 % sobre el código principal (`usuario.py`), destacando las áreas completamente testeadas.

---

## Aprendizajes y Consideraciones

Este proyecto permitió aplicar principios clave de DevOps:

- Detección de errores lógicos mediante pruebas automatizadas.
- Uso de herramientas modernas como Selenium, JMeter, pytest y SonarCloud.
- Diseño de pipelines que aseguran calidad continua.
- Reportes de cobertura y análisis estático para mejorar mantenibilidad.

Gracias a este flujo de trabajo, se logró transformar una aplicación defectuosa en una solución confiable y validada automáticamente en cada actualización del repositorio.

---

© 2025 – Victor Figueroa
