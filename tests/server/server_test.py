import os, sys

_dir = __file__.split('\\')[:-3]
if _dir[0].endswith(':'): _dir[0] += '\\'
sys.path.insert(0, os.path.join(*_dir))

from server import Server

server = Server(main_file=__file__, settings_file="settings.json")
server.start()

print(f"{server.getTotalResourcesCount()} Resources Loaded.")
for res in server.getAllResources():
    print(f"Running Resource Path: {res.getCorePath()}")

network = server.getNetwork()
print(network.getNetRoute())