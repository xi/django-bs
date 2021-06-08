from setuptools import find_packages, setup


setup(
    name='django-bs',
    description='simple bootstrap support for django',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xi/django-bs',
    author='Tobias Bengfort',
    author_email='tobias.bengfort@posteo.de',
    version='4.0.0',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
