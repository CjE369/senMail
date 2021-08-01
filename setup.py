from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Email sending package'
LONG_DESCRIPTION = 'Email sending in easy way with python and use custom services like sendgrid'

# Setting up
setup(
    name= "senMail",
    version= VERSION,
    author= "Chandira Jananath(CjE)",
    author_email= "dhdevcj@gmail.com",
    description= DESCRIPTION,
    long_description_content_type= "text/markdown",
    long_description= LONG_DESCRIPTION,
    packages= find_packages(),
    install_requires= ['yagmail', 'sendgrid', 'ssl', 'smtplib', 'email'],
    keywords= ['python', 'email', 'networking', 'sendmail', 'api', 'cje', 'pythoneasy'],
    classifiers= [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)