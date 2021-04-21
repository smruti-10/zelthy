class Wifi():
    def __init__(self):
        self.wifi_networks = [">[1] Wifi_network 1",">[2] Wifi_network 2",">[3] Wifi_network 3"]
        print("> Your available wifi networks are:")
        for i in self.wifi_networks:
            print(i)
        self.wifi_choice = input("Your choice?")
        if self.wifi_choice:
            self.passw = input("Password:")
            if self.passw:
                print("Connected!")

if __name__ == "__main__":
    x = Wifi()
        