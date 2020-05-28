from distutils.core import setup
setup(
  name = 'igbot',
  packages = ['igbot'],
  version = '0.1.3',
  license='MIT',
  description = 'This Package will help you to automate Instagram Tasks. It uses selenium.',
  author = 'Sanxchep Sharma',
  author_email = 'sanxchep@gmail.com',
  url = 'https://github.com/UncleJo/igbot',
  download_url = 'https://github.com/UncleJo/igbot/archive/v0.1.3.tar.gz',
  keywords = ['Instagram', 'Automation', 'Bot', 'Selenium'], 
  install_requires=[
          'selenium',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
