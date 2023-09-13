import subprocess


class Utils:


    def execute_task(path):
        result = subprocess.run(['python', path])

        if result.returncode == 0:
            print('Ok')

        else:
            print('Erro')
