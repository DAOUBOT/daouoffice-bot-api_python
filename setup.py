from setuptools import setup, find_packages

setup(
    name             = 'daou_chat_bot',
    version          = '0.0.6',
    description      = 'Python wrapper for daouoffice_chat_bot_python',
    author           = 'JoJunHo',
    author_email     = 'charm1109@naver.com',
    url              = 'https://github.com/DAOUBOT/daouoffice-bot-api_python',
    download_url     = 'https://githur.com/rampart81/pyquibase/archive/1.2.tar.gz',
    install_requires = [ ],
    packages         = find_packages(exclude = ['docs', 'daouoffice_chat_bot_python*']),
    keywords         = ['daou','daouoffice'],
    python_requires  = '>=3',
    package_data     =  {
        'pyquibase' : [
            'db-connectors/sqlite-jdbc-3.18.0.jar',
            'db-connectors/mysql-connector-java-5.1.42-bin.jar',
            'db-connectors/postgresql-42.1.3.jar',
            'liquibase/liquibase.jar'
    ]},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)