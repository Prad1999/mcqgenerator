from setuptools import find_packages,setup


setup(
    name='mcqgenerator',
    version='0.0.1',
    author='prad jay',
    author_email='prad10@hotmail.co.uk',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)