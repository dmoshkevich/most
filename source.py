from flask import Flask
import psutil
import docker
# import json

# def tpl_to_json(tpl):
#     dict = tpl._asdict()
#     return json.dumps(dict)


app = Flask(__name__)


@app.route('/get_info', methods=['POST'])
def get_info():

    client = docker.from_env()
    containers = client.containers.list()
    cont_info = []
    if containers:
        for container in containers:
            cont = client.containers.get(str(container))
            cont_info.append(cont.stats())
    else:
        cont_info.append('no running containers')

    cpu = str(psutil.cpu_stats())[10:-1]
    vmem = str(psutil.virtual_memory())[6:-1]
    dusage = str(psutil.disk_usage('/'))[11:-1]
    niocnt = str(psutil.net_io_counters(pernic=False, nowrap=True))[7:-1]
    cont_inf = ''.join(cont_info)

    response = (' CPU: ' + cpu +
                ' Virtual memory: ' + vmem +
                ' Disk usage: ' + dusage +
                ' Net io counters: ' + niocnt +
                ' Containers: ' + cont_inf)
    return response


if __name__ == '__main__':
    app.run()

