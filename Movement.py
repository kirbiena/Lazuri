from ModuleBase import Module
from pubsub import pub
import time
class Movement(Module):
    # (action, speed(0-2), time(s))
    # up and down speed caps at 2?
    #rest caps at 1, should cap
    steps = [
    ("UP", 2, 2),
    ("DOWN", 2, 2),
    ("BACKWARD", 0.5, 2),
             ]
    def __init__(self):
        super().__init__()

    def run_once_in_thread(self):
        #print(self.address, self.data_L, self.data_R)
        for i in self.steps:
            starttime = time.time()
            while time.time() - starttime <= i[2]:
                match i[0]:
                    case "FORWARD":
                        pub.sendMessage("joystick.movement", message = [0,-i[1],0,0,0,0])
                    case "BACKWARD":
                        pub.sendMessage("joystick.movement", message = [0,i[1],0,0,0,0])
                    case "STRAFEL":
                        pub.sendMessage("joystick.movement", message = [i[1],0,0,0,0,0])
                    case "STRAFER":
                        pub.sendMessage("joystick.movement", message = [-i[1],0,0,0,0,0])
                    case "UP":
                        pub.sendMessage("joystick.movement", message = [0,0,0,0,0,i[1]])
                    case "DOWN":
                        pub.sendMessage("joystick.movement", message = [0,0,0,0,i[1],0])
                    case _:
                        pub.sendMessage("joystick.movement", message = [0,0,0,0,0,0])
            pub.sendMessage("joystick.movement", message = [0,0,0,0,0,0])    


