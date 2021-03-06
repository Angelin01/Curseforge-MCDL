from setuptools import setup

with open('README.md', 'r') as f:
	long_description = f.read()
	
setup(
	name='Curseforge-CMDL',
	version='1.0',
	description='Simple downloader for Minecraft mods from CurseForge',
	long_description=long_description,
	license='MIT',
	author='Angelin01, Kabbah',
	url='https://github.com/Angelin01/Curseforge-MCDL',
	python_requires='>=3.5',
	install_requires=[
		'beautifulsoup4',
		'PyQt5',
		'requests',
	],
	include_package_data=True
)