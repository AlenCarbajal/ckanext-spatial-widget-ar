from setuptools import setup, find_packages

setup(
    name='ckanext-spatial_widget_ar',
    packages=find_packages(),
    entry_points={
        'ckan.plugins': [
            'spatial_widget_ar=ckanext.spatial_widget_ar.plugin:SpatialWidgetArPlugin'
        ]
    },
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.html', 'jinja2', None),
        ]
    },
    i18n_domain='ckanext-spatial_widget_ar',
)
