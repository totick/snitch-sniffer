import random

def sonar_find():
    snitch_count = random.randint(0, 10)
    return snitch_count

def lidar_find():
    snitch_count = random.randint(10, 1000)
    return snitch_count


def main():
    print("Sonar technique found", sonar_find(), " snitches")
    print("Lidar technique found", lidar_find(), " snitches")
    
    
main()