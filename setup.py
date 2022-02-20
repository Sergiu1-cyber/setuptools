from setuptools import setup, find_packages

setup(
    name="mytest",
    version="1.0",
    author="wangbm",
    author_email="wongbingming@163.com",
    description="Научиться упаковывать модуль Python -> общедоступная учетная запись: время программирования Python",
    
    # Домашняя страница проекта
    url="http://python-online.cn/", 
    
    # Пакеты, которые вы хотите установить, через setuptools.find_packages, чтобы найти, какие пакеты находятся в текущем каталоге
    # packages=find_packages(),
    # install_requires=['peppercorn'], - dependente
    py_modules=['main'],
)



