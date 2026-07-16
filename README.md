# ckanext-spatial-widget-ar

Complemento de [ckanext-spatial](https://github.com/ckan/ckanext-spatial)
para portales argentinos: los widgets de mapa con rótulos en español
rioplatense y la Argentina como extensión por defecto.

Funcionalidades:

* **Filtrar por ubicación**: mapa en el sidebar de la búsqueda de datasets
  para filtrar por recuadro (bbox), inicializado sobre la Argentina.
* **Extensión espacial**: mapa con la cobertura espacial del dataset en su
  página de detalle.

Requiere ckanext-spatial instalado, con los plugins `spatial_metadata` y
`spatial_query` activos y el índice espacial de Solr configurado.

Probado en CKAN 2.11.

## Instalación

```
pip install -e 'git+https://github.com/datosgobar/ckanext-spatial-widget-ar.git@main#egg=ckanext-spatial-widget-ar'
```

Agregá `spatial_widget_ar` a `ckan.plugins`, después de los plugins de
ckanext-spatial:

```
ckan.plugins = spatial_metadata spatial_query spatial_widget_ar
```

## Configuración

Ninguna propia — usa la configuración de mapas de ckanext-spatial
(`ckanext.spatial.common_map.*`).

## Tests

```
pytest --ckan-ini=test.ini
```

## Licencia

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
