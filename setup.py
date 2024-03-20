from setuptools import find_packages, setup

setup(
    name = 'Medical Chat Bot',
    version = '0.0.0',
    author = 'Kushal Banda',
    author_email = 'kushalbanda265@gmail.com',
    install_requires = ['openai', 'langchain', 'streamlit', 'python-dotenv', 'PyPDF2'],
    packages = find_packages()
)

