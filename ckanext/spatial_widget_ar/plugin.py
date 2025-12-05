cat > /srv/app/src/ckanext-spatial-widget-ar/ckanext/spatial_widget_ar/plugin.py << 'EOF'
from ckan.plugins import SingletonPlugin, implements, IConfigurer
from ckan.common import config
import ckan.plugins.toolkit as toolkit

class SpatialWidgetArPlugin(SingletonPlugin):
    implements(IConfigurer)
    
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'spatial_widget_ar')
EOF