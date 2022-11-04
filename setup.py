from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'EzMetrics',     
  packages = ['EzMetrics'],   
  version = '1.0', 
  license='MIT',  
  description = 'An easy package to use for to get metrics from your models',
  author = 'Jie Wu, Asier Marinero',                 
  author_email = 'jie.wu@alumni.mondragon.edu, asier.marinero@alumni.mondragon.edu', 
  url = 'https://github.com/JieWuu/EzMetrics',
  download_url = 'https://github.com/JieWuu/EzMetrics/archive/refs/tags/v_1.0.tar.gz',  
  keywords = ['Easy', 'Metrics', 'Model'], 
  long_description=long_description,
  long_description_content_type='text/markdown',
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',    
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',    
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)