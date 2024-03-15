class Father:
    def bike():
        print("Bike : Harley Davidson")
    def laptop():
        print("Laptop : Dell 15s => 4gb RAM , 256GB HDD")

class Son(Father):
    def laptop():
        sec = "Mac Book Pro"
        print("Laptop : Mac Book 15 Pro => 16gb RAM, 2TB SSD")

Son.bike()
Son.laptop()
