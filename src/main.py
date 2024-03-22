from swu import Deck, RandomAgent, Engine, Database

def main():
    print("start")

    db = Database('/home/matt/workspace/swu/data/sets')
    
    agents = [
        RandomAgent(Deck('/home/matt/workspace/swu/data/decks/sor-starter-vader.json')),
        RandomAgent(Deck('/home/matt/workspace/swu/data/decks/sor-starter-vader.json'))
    ]

    engine = Engine(db, agents)
    engine.run()

    print("end")

if __name__ == "__main__":
    main()
