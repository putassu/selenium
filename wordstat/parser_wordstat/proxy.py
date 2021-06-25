class Proxy:
    def __init__(self):
        self.proxy = {
            "91.107.119.18": "34512",
            "89.191.227.143": "34512",
            "193.233.80.125": "34512",
            "185.30.99.106": "34512",
            "5.180.103.105": "34512",
            "176.53.132.68": "34512",
            "77.220.205.48": "34512",
            "85.117.233.45": "34512",
            "31.148.99.157": "34512",
            "46.16.13.93": "34512",
        }

        self.port_https = "34512"
        self.port_socks5 = "34513"
        self.login = "achuhrajI3"
        self.password = "F2f0LeZ"

    def get_proxy(self, num):
        keys = list(self.proxy.keys())
        values = list(self.proxy.values())
        return {keys[num]: values[num]}

proxies = {
    "http": "http://achuhrajI3:F2f0LeZ@91.107.119.18:34512/"
}
