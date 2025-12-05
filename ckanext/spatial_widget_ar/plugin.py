from ckan.plugins import SingletonPlugin, ITemplateHelpers

class SpatialWidgetArPlugin(SingletonPlugin, ITemplateHelpers):
    def get_helpers(self):
        return {
            'spatial_widget_ar': lambda: True
        }