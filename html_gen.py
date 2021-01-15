#!/usr/bin/python3
import os, os.path
ru = f'{os.getcwd()}/html'
text =f"""
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <meta charset="utf-8">
        <meta name="description" content="">
        <meta name="keywords" content=""> 
        <link rel="icon" href="" type="{ru}/images/">
        <link rel="stylesheet" href="{ru}/css/styles.css">
    </head>
    <body>
    </body>
</html>
"""
try:
    route = f'{os.getcwd()}/html'
    path = os.mkdir(route, mode=0o777)
    path2 = os.mkdir(f'{ru}/css')
    path3 = os.mkdir(f'{ru}/tempates')
    path4 = os.mkdir(f'{ru}/images')
    path5 = os.mkdir(f'{ru}/scripts')
    with open(ru + '/index.html', 'w') as index:
        index.write(text)
        index.close()
    with open(f'{ru}/css/styles.css', 'w') as styles:
        styles.close()
except Exception as e:
    print('[!!]no se pudo crear el directorio ', e)

print('[**]se han creado las carpetas basicas para el website')
