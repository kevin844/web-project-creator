#!/usr/bin/python3
import os, os.path, base64

try:

    project_path = f'{os.getcwd()}/html'
    path = os.mkdir(project_path, mode=0o777)

    css = os.mkdir(f'{project_path}/css')
    templates = os.mkdir(f'{project_path}/tempates')
    images = os.mkdir(f'{project_path}/images')
    scripts = os.mkdir(f'{project_path}/scripts')

    html_encoded = """
PCFET0NUWVBFIGh0bWw+CjxodG1sPgogICAgPGhlYWQ+CiAgICAgICAgPHRpdGxlPjwvdGl0bGU+CiAgICAgICAgPG1ldGEgY2hhcnNldD0idXRmLTgiPgogICAgICAgIDxtZXRhIG5hbWU9ImRlc2NyaXB0aW9uIiBjb250ZW50PSIiPgogICAgICAgIDxtZXRhIG5hbWU9ImtleXdvcmRzIiBjb250ZW50PSIiPiAKICAgICAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Intwcm9qZWN0X3BhdGh9L2Nzcy9zdHlsZXMuY3NzIj4KICAgIDwvaGVhZD4KICAgIDxib2R5PgogICAgPC9ib2R5Pgo8L2h0bWw+
"""
    index_content = base64.b64decode(html_encoded)
    index_decoded = index_content.decode("utf-8")

    with open(project_path + '/index.html', 'w') as index:
        index.write(index_decoded)
        index.close()

    with open(f'{project_path}/css/styles.css', 'w') as styles:
        styles.close()

except Exception as e:
    print('[!!]no se pudo crear el directorio ', e)

print('[**]se han creado las carpetas basicas para el website')

