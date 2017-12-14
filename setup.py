from setuptools import setup

with open('README.md', 'r') as f:
	long_description = f.read()
	
setup(
	name='Curseforge-CMDL',
	version='pre-alpha-0.1',
	description='Simple downloader for Minecraft mods from CurseForge',
	long_description=long_description,
	license='MIT',
	author='Angelin01, Kabbah',
	url='https://github.com/Angelin01/Curseforge-MCDL',
	install_requires=[
		'beautifulsoup4',
	]
	include_package_data=True
)