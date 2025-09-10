"""
Paquete de pruebas estadísticas para verificar aleatoriedad.
Incluye: Prueba de medias, varianza y uniformidad.
"""

from .prueba_medias import prueba_medias
from .prueba_varianza import prueba_varianza
from .prueba_uniformidad import prueba_uniformidad

__all__ = ["prueba_medias", "prueba_varianza", "prueba_uniformidad"]
