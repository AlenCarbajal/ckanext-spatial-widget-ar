from ckan.plugins import SingletonPlugin, implements, IConfigurer
import os

class SpatialWidgetArPlugin(SingletonPlugin):
    implements(IConfigurer)

    def update_config(self, config):
        # Ruta absoluta al directorio de templates dentro del plugin
        here = os.path.dirname(__file__)
        template_dir = os.path.join(here, 'templates')

        # CKAN 2.11 → agregar a ckan.template_directories (NOTA: plural)
        dirs = config.get('ckan.template_directories', '').split()
        if template_dir not in dirs:
            dirs.append(template_dir)
        config['ckan.template_directories'] = ' '.join(dirs)
