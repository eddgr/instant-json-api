from setuptools import setup


setup(
    name='Instant JSON API',
    version='1.0',
    url='https://github.com/eddgr/instant-json-api',
    author='Edgar Ong',
    author_email='emailedgar@gmail.com',
    description='Create instant API endpoints for your JSON files.',
    py_modules=['instant_json_api'],
    install_requires=['Flask', 'Flask-CORS'],
    license='MIT'
)
