import random

def find_snitchs():
    snitch_count = random.randint(0, 10)
    return snitch_count


def main():
    snitchs = find_snitchs()
    print("Found", snitchs, " snitches")
    
    
main()