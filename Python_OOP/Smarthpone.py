class Smartphone():
    def __init__(self, memory) -> None:
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if self.is_on and self.memory >= app_memory and app_memory > 0:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"
        elif not self.is_on:         
            return f"Turn your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())