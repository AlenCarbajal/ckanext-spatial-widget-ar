from ckan.plugins import SingletonPlugin, implements, IConfigurer

class SpatialWidgetArPlugin(SingletonPlugin):
    implements(IConfigurer)

    def update_config(self, config):
        # Add our templates directory
        config['ckan.template_directory'] = 'templates'