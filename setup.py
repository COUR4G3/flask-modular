from setuptools import find_packages, setup

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='flask-modular',
    description='Create modular and extensible Flask applications',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Michael de Villiers',
    author_email='michael@devilears.co.za',
    url='https://github.com/cour4g3/flask-modular',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Framework :: Flask',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='flask, modular, module, modules',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'flask',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/cour4g3/flask-modular/issues',
    },
)
