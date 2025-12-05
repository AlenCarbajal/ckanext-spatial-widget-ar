from ckan.plugins import SingletonPlugin, implements, IConfigurer

class SpatialWidgetArPlugin(SingletonPlugin):
    implements(IConfigurer)

    def update_config(self, config):
        self.add_template_directory(config, 'templates')
