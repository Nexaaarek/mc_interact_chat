import json
import pytchat
from mcrcon import MCRcon

ip = ""
port = ""
password = ""

def create_config():
    print("Creating config file")
    data = []
    data.append({
        'ip': '127.0.0.1',
        'port': "25575",
        'password': 'passwd'
    })

    with open('config.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    print("Created")


def connect():
    with open('config.json') as json_file:
        data = json.load(json_file)
        for d in data:
            ip = d['ip']
            port = d['port']
            password = d['password']
    live_id = input("Enter your live id (video id) - ")
    mcr = MCRcon(ip, password, int(port))
    mcr.connect()
    print("Connecting to minecraft server using RCON")
    chat = pytchat.create(live_id)
    while chat.is_alive():
        for c in chat.get().sync_items():
            cmd_to_execute = mcr.command(c.message)
            print(cmd_to_execute)
    mcr.disconnect()
    print("Disconnected")
    quit()


def main():
    try:
        connect()
    except IOError:
        create_config()

if __name__ == '__main__':
    main()