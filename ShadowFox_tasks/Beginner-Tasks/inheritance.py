class MobilePhone:
    def __init__(self,ScreenType,NetworkType,DualSim,FrontCamera,RearCamera,RAM,Storage):
        self.ScreenType = ScreenType
        self.NetworkType = NetworkType
        self.DualSim = DualSim
        self.FrontCamera = FrontCamera
        self.RearCamera = RearCamera
        self.RAM = RAM
        self.Storage = Storage
    def showDetails(self):
        print(f"The Properties of this Mobile Phone: {self.ScreenType} {self.NetworkType} {self.DualSim} {self.FrontCamera} {self.RearCamera} {self.RAM} {self.Storage}")
    def make_call(self):
        print("Making a call...")
    def receive_call(self):
        print("Receiving a call...")
    def take_a_picture(self):
        print("Taking a picture...")
class Apple(MobilePhone):
    def __init__(self,ScreenType,NetworkType,DualSim,FrontCamera,RearCamera,RAM,Storage):
        super().__init__(ScreenType, NetworkType, DualSim, FrontCamera, RearCamera, RAM, Storage)
    def showBattery(self):
        print("Battery capacity (Standard/Pro): 3200-3400 mAH")
        print("Battery capacity (Plus/Pro max): 4300-4500 mAH")
class Samsung(MobilePhone):
    def __init__(self,ScreenType,NetworkType,DualSim,FrontCamera,RearCamera,RAM,Storage):
        super().__init__(ScreenType, NetworkType, DualSim, FrontCamera, RearCamera, RAM, Storage)
    def showProcessor(self):
        print("Processors used:")
        print("Exynox/SnapDragon/MediaTek")
#apple objects
iPhone1 = Apple("Touch Screen", "4G", "True", "12MP", "12MP", "4GB", "128GB")
iPhone2 = Apple("Touch Screen", "5G", "True", "12MP", "12MP", "4GB", "256GB")
#samsung objects
samsung1 = Samsung("Touch Screen", "4G", "True", "8MP", "48MP", "4GB", "64GB")
samsung2 = Samsung("Touch Screen", "5G", "True", "16MP", "32MP", "4GB", "64GB")
iPhone1.showDetails()
iPhone1.showBattery()
samsung1.showDetails()
samsung1.showProcessor()


