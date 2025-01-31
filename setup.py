#its durgesh.rwt (insta)
from distutils.core import setup
setup(
  name = 'cloudhost',         # How you named your package folder (MyLib)
  packages = ['cloudhost'],   # Chose the same as "name"
  version = '2.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Cloud Storage Facility',   # Give a short description about your library
  long_description='(cloudhost) make your python apps online',#full description
  author = 'Durgesh Rawat',                   # Type in your name
  author_email = 'durgeshrawat.info@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/durgeshrawat/cloudhost',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/durgeshrawat/cloudhost/archive/refs/tags/v_1.tar.gz',    # I explain this later on
  keywords = ['cloudhost', 'database', 'make apps online'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'python-wordpress-xmlrpc',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.8',
  ],
)
