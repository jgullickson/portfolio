from setuptools import setup, find_packages

setup(
    name='portfolio_pkg',
    # packages=['portfolio_pkg'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=['libsass >= 0.6.0'],
    sass_manifests={
        'portfolio_pkg': ('static/sass', 'static/css', '/static/css')
    },
    install_requires=[
        'click>=7.1.2',
        'dnspython>=1.16.0',
        'email-validator>=1.1.1',
        'Flask>=1.1.2',
        'Flask-WTF>=0.14.3',
        'gunicorn>=20.0.4',
        'idna>=2.10',
        'itsdangerous>=1.1.0',
        'Jinja2>=2.11.2',
        'libsass>=0.20.0',
        'MarkupSafe>=1.1.1',
        'python-dotenv>=0.14.0',
        'six>=1.15.0',
        'Werkzeug>=1.0.1',
        'WTForms>=2.3.1',
    ]
)