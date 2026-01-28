import requests

NODES = [
    "http://localhost:5001",
    "http://localhost:5002",
    "http://localhost:5003",
]


def put(key, value):
    success = 0

    for node in NODES:
        try:
            r = requests.put(
                f"{node}/put",
                json={"key": key, "value": value},
                timeout=1
            )
            if r.status_code == 200:
                success += 1
        except requests.exceptions.RequestException:
            print(f"[WARN] Node {node} is unavailable")

    print(f"Write acknowledged by {success}/{len(NODES)} nodes")


def get(key):
    for node in NODES:
        try:
            r = requests.get(f"{node}/get", params={"key": key}, timeout=1)
            if r.status_code == 200:
                data = r.json()
                print(f"Read from {node}: {data}")
                return
        except requests.exceptions.RequestException:
            print(f"[WARN] Node {node} is unavailable")

    print("Failed to read key from any node")

if __name__ == "__main__":
    while True:
        cmd = input("Enter command (put/get/exit): ")

        if cmd == "put":
            k = input("Key: ")
            v = input("Value: ")
            put(k, v)

        elif cmd == "get":
            k = input("Key: ")
            get(k)

        elif cmd == "exit":
            break
