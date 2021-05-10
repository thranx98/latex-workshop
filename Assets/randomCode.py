from random import randint
def main():
    # Make function work with pandas df afterwards
    name_of_anime = input("Enter Name of Anime:")
    numberEpsSeason1 = input("Enter the number of episodes in Season 1:")
    SlappeNotFound = True 
    Episodes = list(range(0,int(numberEpsSeason1)))

    while(SlappeNotFound and (len(Episodes)>0)):
        sample = int(Episodes.pop(randint(0,len(Episodes)-1)))
        print(f"See if Slappe Present in {sample}")
        prompt = input("Enter Y if slappe found: ")
        if prompt.lower() == 'y':
            SlappeNotFound = False
            print(f"{name_of_anime} Slappe Sample from Episode {sample}")
        if (len(Episodes)==0):
            print("No Slappe Found in this Series - Sample Invalid")

if __name__ == "__main__":
    main()
