import random

def find():
    snitch_count = random.randint(0, 10)
    return snitch_count


def main():
    snitchs = find()
    print("Found", snitchs, " snitches")
    
    
main()