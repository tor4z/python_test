from concurrent.futures import ProcessPoolExecutor


class C:
    def server(self):
        print("sever")
        
    def client(self):
        print("client")
    
    def run(self):
        with ProcessPoolExecutor(max_workers=2) as e:
            e.submit(self.server)
            e.submit(self.client)
            


if __name__ == "__main__":
    c=C()
    c.run()
    #with ProcessPoolExecutor(max_workers=2) as e:
    #    e.submit(server)
    #    e.submit(client)