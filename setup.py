from setuptools import setup

setup(name='CP467 Image Processing Project',
      version='1.0',
      description='Web app that implements filters, thinning and feature vectors',
      author='Chunxiao Li and Don Miguel',
      author_email='lixx8170@mylaurier.ca, migu0850@mylaurier.ca',
      install_requires=['Flask>=0.10.1', 'Pillow==2.6.1', 'numpy==1.10.1', 'flask-sqlalchemy==2.0', 'sqlalchemy==0.7.9',
                        'psycopg2==2.6.1', 'flask-migrate==1.6.0', 'flask-script==2.0.5'],
      )
