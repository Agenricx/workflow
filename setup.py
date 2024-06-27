
"""Alfred-Workflow library with Python for building Alfred 3.x 4.x 5.x workflows."""

from distutils.core import setup

setup(
    name='workflow',
    version='1.40.0',
    description='Alfred-Workflow library with Python for building Alfred 3.x 4.x 5.x workflows.',
    author='Agenric',
    author_email='AgenricWon@gmail.com',
    url='https://github.com/agenricx/Workflow',
    packages = ['workflow'],
    include_package_data=True,
    package_data = {'workflow': ['version', 'Notify.tgz']}
)
