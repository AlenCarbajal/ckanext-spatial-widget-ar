from setuptools import setup

setup(
    entry_points={
        'ckan.plugins': [
            'spatial_widget_ar=ckanext.spatial_widget_ar.plugin:SpatialWidgetArPlugin'
        ]
    }
)
