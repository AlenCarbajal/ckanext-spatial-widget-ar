from ckan.plugins import SingletonPlugin, implements, IConfigurer
from ckan.plugins import toolkit

class SpatialWidgetArPlugin(SingletonPlugin):
    implements(IConfigurer)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
