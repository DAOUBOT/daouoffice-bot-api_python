from setuptools import setup, find_packages


setup(
    name='daouoffice_chat_bot_python',
    version='0.0.2',
    license='MIT',
    description='daouoffice_chat_bot_python',
    author='JoJunHo',
    author_email='charm1109@naver.com',
    url = 'https://github.com/DAOUBOT/daouoffice-bot-api_python',
    # packages=["daouoffice_chat_bot_python"],
    packages = find_packages(exclude = ['flask', 'requests', 'json']),
    include_package_data=True,
    zip_safe=False,
    python_requires  = '>=3'

)