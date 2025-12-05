from setuptools import setup

setup(
    name='ckanext-spatial-widget-ar',
    version='0.1',
    packages=['ckanext.spatial_widget_ar'],
    entry_points='''
        [ckan.plugins]
        spatial_widget_ar=ckanext.spatial_widget_ar.plugin:SpatialWidgetArPlugin
    ''',
)
