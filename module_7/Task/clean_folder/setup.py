from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:sort_folders',
        ],
    },
)