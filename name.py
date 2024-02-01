import random
import nltk
indian_names = ['Aarav', 'Arjun', 'Rohan', 'Vivek', 'Rajat', 'Siddharth',  'Kunal', 'Ravi','Abhinav', 'Karthik', 'Yash','Ashishika','Pranjal','Saksham','Aashi','Aayushi','Ayushii','Jyotie','Kinjal','Vinay','Divyanshu',
    'Aisha', 'Neha', 'Priya', 'Ananya',  'Isha', 'Kavya', 'Tanvi', 'Mira', 'Dia', 'Ritu', 'Aarohi', 'Anjali', 'Pooja', 'Lavisha','Lovi','Romie','Harhsitaa','Nishat','Nishant','Beena','Aarya','Rishika',
     'Samar', 'Dev', 'Kiran', 'Rishi', 'Simran', 'Anika',  'Aditya', 'Sahil', 'Tara', 'Krish', 'Samaira','Yukta','Ishika','Bhumika','Shivansha','Lavisha','Archie','Piyush','Ashish','Dewansh','Katrina','Anushaka','Anushka','Utkarsha','utkarsh',    
    'Mudit','Avi','Pav','Abishekk','Adesh','Yusuf','shyamm','Shubhanshu','Shubhh','Houshik','Vidish','Shivek','Varnikaa','Trapti','Huda','Chetan','Naveen','Bhavesh','Garvit', 'Aditi', 'Advait', 'Aishwarya', 'Akshay', 'Akanksha', 'Amit', 'Amrita', 'Aniket','Anuj', 'Apoorva',  'Ayesha', 'Ayush', 'Bhavya','Chaitanya', 'Chandni', 'Darsh', 'Deepika', 'Dev', 'Divya', 'Dhruv', 'Esha', 'Gaurav', 'Gayatri',
    'Gopal', 'Himanshu', 'Ishita', 'Ishan', 'Jhanvi', 'Jatin', 'Kriti',  'Krishna','Lakshya', 'Manisha', 'Mayank', 'Mehak', 'Mihir',  'Nikhil', 'Nandini',
    'Pranav', 'Prachi', 'Prateek', 'Preeti', 'Rahul', 'Riya', 'Rohit', 'Radhika',  'Sakshi','Samarth', 'Sanika', 'Sarthak', 'Shreya', 'Shivam', 'Sneha', 'Soham', 'Swara', 'Tanisha', 'Tarun','Urmila', 'Varun', 'Vidhi', 'Vijay', 'Vandana', 'Yamini', 'Yuvraj','Zoya', 'Aahan', 'Aarushi', 'Arnav', 'Aanya', 'Advik', 'Avni',
    'Atharva', 'Anaya',  'Dev', 'Dhriti', 'Divisha','Ishaan', 'Kiara',  'Kashvi',  'Maira','Om', 'Oviya', 'Pihu', 'Reyansh', 
    'Sanvi', 'Shaurya', 'Shiv', 'Siya', 'Tanay', 'Tanya', 'Vihaan', 'Vanya','Vivaan', 'Vaishnavi', 'Yuvan', 'Yamika', 'Zayan', 'Zara', 'Aarit', 'Amaira', 'Ahaan', 'Anvi','Aarush', 'Anvika', 'Advay',  'Abeer', 'Bhavika', 'Aiden','Aryan', 'Chahat',
    'Atharv', 'Diyara', 'Gia', 'Ayaan', 'Hansa', 'Divit', 'Ira', 'Harsh', 'Kashish','Kyra', 'Jai', 'Laasya', 'Kabir', 'Misha', 'Laksh', 'Myra', 'Mohit', 'Navya',
    'Naman', 'Niyati', 'Ojas', 'Pari', 'Parth', 'Riaan', 'Risha', 'Rudra', 'Sanya', 'Shanaya', 'Shlok', 'Taara', 'Tanish', 'Veer', 'Viha','Zayn']
    
last_names = [  "Sharma", "Verma", "Singh", "Patel", "Kumar", "Jha", "Gupta", "Rao", "Shah",
    "Mishra", "Yadav", "Chauhan", "Das", "Choudhary", "Jain", "Thakur",
    "Reddy", "Goswami", "Nair", "Iyer", "Menon", "Mehta", "Shetty", "Pandey", "Khan",
    "Pawar", "Yaduvanshi", "Dixit", "Chopra", "Malhotra", "Biswas", "Bhat", "Rathore",
    "Goyal", "Shukla", "Garg", "Bhattacharya", "Kaur", "Chatterjee", "Sen", "Nag", "Dasgupta",
    "Banerjee", "Roy", "Dutta", "Mahajan", "Shinde", "Purohit", "Bhandari", "Soni", "Saxena",
    "Dube", "Acharya", "Mukherjee", "Mittal", "Tiwari", "Dubey", "Joshi", "Rajput", "Kamble",
    "Barman", "Srivastava", "Tripathi", "Sinha", "Rawat", "Nayak", "Parikh", "Seth",
    "Kapoor", "Rana", "Sarin", "Gill", "Rathod", "Deshmukh", "Chavan", "Kadam", "Nagpal",
    "Dhillon", "Nanda", "Gosain","Bali", "Narayan", "Prajapati", "Rastogi", "Bhagat",
    "Bharti", "Lal", "Kashyap", "Sethi", "Bhatia", "Walia", "Malik", "Chaudhry", "Chabra","Upadhyay","Kalesh",
   "Jindal","Arya","Sisodia","raj","Krishna","Pilania","Punia","Shaw","Sham","Sahni","mahawat","mahapatra","singhal"
]
animal_names = [
    "Aardvark", "Albatross", "Alligator", "Alpaca", "Ant", "Anteater", "Antelope", "Ape", "Armadillo", "Baboon",
    "Badger", "Barracuda", "Bat", "Bear", "Beaver", "Bee", "Bison", "Boar", "Buffalo", "Butterfly",
    "Camel", "Capybara", "Caribou", "Cassowary", "Cat", "Caterpillar", "Cheetah", "Chicken", "Chimpanzee", "Chinchilla",
    "Chough", "Clam", "Cobra", "Cockroach", "Cod", "Cormorant", "Coyote", "Crab", "Crane", "Crocodile",
    "Crow", "Curlew", "Deer", "Dinosaur", "Dog", "Dogfish", "Dolphin", "Donkey", "Dotterel", "Dove",
    "Dragonfly", "Duck", "Dugong", "Dunlin", "Eagle", "Echidna", "Eel", "Eland", "Elephant", "Elk",
    "Emu", "Falcon", "Ferret", "Finch", "Fish", "Flamingo", "Fly", "Fox", "Frog", "Gaur",
    "Gazelle", "Gecko", "Gerbil", "Giraffe", "Gnat", "Gnu", "Goat", "Goldfinch", "Goosander", "Goose",
    "Gorilla", "Goshawk", "Grasshopper", "Grouse", "Guanaco", "Gull", "Hamster", "Hare", "Hawk", "Hedgehog",
    "Heron", "Herring", "Hippopotamus", "Hornet", "Horse", "Human", "Hummingbird", "Hyena", "Ibex", "Ibis",
    "Jackal", "Jaguar", "Jay", "Jellyfish", "Kangaroo", "Kingfisher", "Koala", "Kookabura", "Kouprey", "Kudu",
    "Lapwing", "Lark", "Lemur", "Leopard", "Lion", "Llama", "Lobster", "Locust", "Loris", "Louse",
    "Lyrebird", "Magpie", "Mallard", "Manatee", "Mandrill", "Mantis", "Marten", "Meerkat", "Mink", "Mole",
    "Mongoose", "Monkey", "Moose", "Mouse", "Mosquito", "Mule", "Narwhal", "Newt", "Nightingale", "Octopus",
    "Okapi", "Opossum", "Oryx", "Ostrich", "Otter", "Owl", "Ox", "Oyster", "Panther", "Parrot",
    "Panda", "Partridge", "Peafowl", "Pelican", "Penguin", "Pheasant", "Pig", "Pigeon", "Pony", "Porcupine",
    "Porpoise", "Quail", "Quelea", "Quokka", "Quoll", "Rabbit", "Raccoon", "Rail", "Ram", "Rat",
    "Raven", "Red deer", "Red panda", "Reindeer", "Rhinoceros", "Rook", "Salamander", "Salmon", "Sand Dollar", "Sandpiper",
    "Sardine", "Scorpion", "Sea cucumber", "Sea lion", "Sea Urchin", "Seahorse", "Seal", "Serval", "Shark", "Sheep",
    "Shrew", "Skunk", "Snail", "Snake", "Sparrow", "Spoonbill", "Squid", "Squirrel", "Starling", "Stingray",
    "Stinkbug", "Stork", "Swallow", "Swan", "Tapir", "Tarsier", "Tiger", "Toad", "Trout", "Turkey",
    "Turtle", "Vulture", "Wallaby", "Walrus", "Wasp", "Water buffalo", "Weasel", "Whale", "Wildcat", "Wolf",
    "Wolverine", "Wombat", "Woodpecker", "Worm", "Wren", "Yak", "Zebra"
]
flower_names = [
    "Rose", "Lily", "Daisy", "Tulip", "Sunflower", "Hibiscus", "Orchid", "Iris", "Carnation", "Peony",
    "Cherry Blossom", "Daffodil", "Lilac", "Marigold", "Hydrangea", "Pansy", "Snapdragon", "Dahlia", "Zinnia", "Freesia",
    "Petunia", "Aster", "Begonia", "Poppy", "Columbine", "Gladiolus", "Jasmine", "Chrysanthemum", "Bluebell", "Magnolia",
    "Camellia", "Primrose", "Violet", "Forget-Me-Not", "Daisy", "Blossom", "Thistle", "Tansy", "Lavender", "Dandelion",
    "Azalea", "Ivy", "Clover", "Geranium", "Bougainvillea", "Crocus", "Anemone", "Tiger Lily", "Morning Glory", "Queen Anne's Lace",
    "Daffodil", "Dianthus", "Edelweiss", "Fuchsia", "Gardenia", "Heather", "Heliotrope", "Jasmine", "Larkspur", "Lavender",
    "Lilac", "Lily of the Valley", "Lotus", "Marigold", "Narcissus", "Oleander", "Peony", "Periwinkle", "Petunia", "Poinsettia",
    "Primrose", "Rhododendron", "Snapdragon", "Sunflower", "Sweet Pea", "Tulip", "Verbena", "Violet", "Wisteria", "Zinnia",
    "Bluebell", "Dahlia", "Foxglove", "Iris", "Jacaranda", "Jonquil", "Marigold", "Pansy", "Rosemary", "Snowdrop",
    "Sweet Alyssum", "Tansy", "Tiger Lily", "Wisteria", "Yarrow", "Yucca", "Zinnia",
    "Aconitum", "Allium", "Alyssum", "Amaranthus", "Anemone", "Angelica", "Artemisia", "Aster", "Astilbe", "Baptisia",
    "Bee Balm", "Bellflower", "Bergenia", "Bleeding Heart", "Borage", "Butterfly Weed", "Calendula", "Candytuft", "Canterbury Bells",
    "Cardinal Flower", "Carnations", "Castor Bean", "Catmint", "Chicory", "Chrysanthemum", "Clematis", "Cleome", "Columbine", "Comfrey",
    "Coreopsis", "Cosmos", "Cotton Lavender", "Crocosmia", "Cuphea", "Dame's Rocket", "Delphinium", "Dianthus", "Dusty Miller", "Echinacea",
    "Eupatorium", "Euphorbia", "Fennel", "Feverfew", "Floss Flower", "Flowering Tobacco", "Flowering Kale", "Foam Flower", "Forget-Me-Not",
    "FourO'Clocks", "Foxglove", "Gaillardia", "Gaura", "Gayfeather", "Gazania", "Globe Thistle", "Gloriosa Daisy", "Goat's Beard", "Godetia",
    "Goldenrod", "Helenium", "Heliotrope", "Hollyhock", "Honesty", "Hosta", "Hyacinth", "Hyssop", "Impatiens", "Iris",
    "Jack-in-the-Pulpit", "Jacob's Ladder", "Joe Pye Weed", "Kangaroo Paw", "Knapweed", "Lavender Cotton", "Liatris", "Lily of the Nile", "Lobelia", "Love-In-A-Mist",
    "Lupine", "Lychnis", "Lysimachia", "Maltese Cross", "Marsh Marigold", "Meadow Rue", "Meadowsweet", "Mignonette", "Monarda", "Moss Rose",
    "Nasturtium", "Nemophila", "Nicotiana", "Obedient Plant", "Oxalis", "Painted Daisy", "Pampas Grass", "Pansy", "Pasque Flower", "Penstemon",
    "Pincushion Flower", "Pinks", "Plumbago", "Poppy", "Portulaca", "Primrose", "PurpleConeflower", "Quince", "Rudbeckia", "RussianSage",
    "Salvia", "Scabiosa", "SeaHolly", "SeaLavender", "ShastaDaisy", "SilverMound", "Sneezeweed", "Soapwort", "SocietyGarlic", "Sorrel",
    "SpiderFlower", "Spurge", "Statice", "Stonecrop", "Sunrose", "Sunflower", "SweetPea", "SweetSultan", "SweetWilliam", "Tansy",
    "Tarragon", "Thrift", "Thyme", "Toadflax", "Torenia", "Trillium", "Trollius", "Tuberose", "Tulip", "Veronica",
    "Vinca", "Violet", "Virginia Bluebell", "Wallflower", "WaterLily", "Wax"," Begonia", "WildBergamot", "Windflower", "Yarrow", "YellowArchangel",
    "Zinnia", "Abutilon", "Aconitum", "African","Iris", "Ageratum", "Alchemilla", "Allamanda", "Alyssum", "Amaranthus", "Anemone", "Angelonia",
    "Anthurium", "Armeria", "Asters", "Astilbe", "Balsam", "Begonia", "Bergenia", "Browallia", "Cactus", "CalaLily",
    "Campanula", "Candytuft", "Canna", "Cape", "Marigold", "Carnation", "Celosia", "Chrysanthemum", "Cineraria", "Cleome", "Cockscomb",
    "Coleus", "Columbine", "Coneflower", "Coral","Bells", "Coreopsis", "Cosmos", "Cotton Lavender", "Crown","Imperial", "Daffodil", "Dahlia",
    "Daisy", "Delphinium", "Dianthus", "Dusty Miller", "Euphorbia", "Freesia", "Fuchsia", "Gaillardia", "Geranium", "Ginger",
    "Gladiolus"]
human_names = [
    "John", "Mary", "Michael", "Emily", "William", "Sophia", "James", "Olivia", "Robert", "Emma",
    "Joseph", "Ava", "David", "Isabella", "Christopher", "Mia", "Daniel", "Abigail", "Matthew", "Ella",
    "Andrew", "Madison", "Anthony", "Scarlett", "Elizabeth", "Henry", "Grace", "Jackson", "Avery", "Samuel",
    "Sofia", "Benjamin", "Aria", "Christopher", "Chloe", "Emily", "Lucas", "Lily", "Aiden", "Amelia",
    "Ethan", "Harper", "Alexander", "Evelyn", "Sebastian", "Aubrey", "Jack", "Layla", "Owen", "Nora",
    "Ryan", "Zoey", "Liam", "Addison", "Nathan", "Camila", "Carter", "Hannah", "Gabriel", "Brooklyn",
    "Isaac", "Penelope", "Nicholas", "Riley", "Elijah", "Natalie", "Christian", "Zoe", "Jonathan", "Leah",
    "Landon", "Stella", "Julian", "Hazel", "Aaron", "Ellie", "Charles", "Aurora", "Thomas", "Violet",
    "Connor", "Lillian", "Caleb", "Mila", "Joseph", "Elizabeth", "Levi", "Claire", "Jaxon", "Lucy",
    "Lincoln", "Anna", "John", "Sarah", "David", "Lila", "Isaiah", "Aaliyah", "Dylan", "Kinsley",
    "Jordan", "Maya", "Adam", "Alexa", "Colton", "Savannah", "Julian", "Nova", "Eli", "Scarlet",
    "John", "Arya", "Nathaniel", "Emilia", "Jaxson", "Luna", "Samuel", "Elena", "Tyler", "Victoria",
    "Mason", "Madelyn", "Angel", "Audrey", "Wyatt", "Alice", "Joseph", "Paisley", "Dominic", "Eva",
    "Brandon", "Skylar", "Austin", "Autumn", "Cameron", "Caroline", "Jace", "Genesis", "Xavier", "Kennedy",
    "Chase", "Kylie", "Kevin", "Ariana", "Zachary", "Piper", "Gavin", "Allison", "Hayden", "Alexandra",
    "Bryan", "Gabriella", "Parker", "Jasmine", "Kai", "Valentina", "Charlie", "Daisy", "Adam", "Liliana",
    "Louis", "Arianna", "Evan", "Isabelle", "Alex", "Melanie", "Brody", "Adeline", "Jason", "Sienna",
    "Brian", "Ruby", "Jaden", "Chloe", "Juan", "Sophie", "Leo", "Alexis", "Cooper", "Kaylee",
    "Ayden", "Aubree", "Ian", "Ariel", "Garrett", "Madeline", "Carson", "Gianna", "Ezekiel", "Faith",
    "Miles", "Kimberly", "Eric", "Eleanor", "Blake", "Clara", "Hayden", "Isabel", "Diego", "Michelle",
    "Luca", "Leilani", "Vincent", "Mya", "Cole", "Jocelyn", "Maxwell", "Athena", "Seth", "Alaina",
    "Xander", "Ayla", "Kaden", "Summer", "Ashton", "Finley", "Wesley", "Diana", "Timothy", "Raelynn",
    "Thomas", "Mackenzie", "Richard", "Reagan", "Oliver", "Elise", "Brayden", "Harmony", "Alexis", "Jayla",
    "Victor", "Juliana", "Joel", "Makayla", "Luis", "Alana", "Alan", "Destiny", "Max", "Miranda",
    "Levi", "Georgia", "George", "Isla", "Jesse", "Rylee", "Derek", "Londyn", "Jared", "Elliana",
    "Charlie", "Angelina", "Oscar", "Rosie", "Charlie", "Nova", "Zane", "Paris", "Emmett", "Isabela",
    "Hudson", "Juliette", "Luke", "Lilly", "Jordan", "Charlie", "Camden", "Amara", "Aidan", "Lacey","Lorea","Roc"]
username_list = ["Luminesce","Vivacious","Enamored","Enigma","Serendipity","Whimsy","Ephemeral","Mellifluous","Eloquence",
    "Effervescent","Transcendent","Luminary","Ineffable","Ethereal","Galvanize","Radiant","Effulgent","Resplendent","Luminescent","Vivaciousness",
    "Sparkle","Xenon","Sapphire","Onyx","Frost","Solar","Svelte","Sly","Starlight","Just-in","Zenith","Hype"
"Nimbus","Glint","Flux","Pulse","Radiance","Bliss","Mirage","Fuse","Flare","Shine","Glitz","Euphoria","Xenon","Nexus","Fash","Kayle","Carol"]

def generate_indian_name(num_names=1400):

    

    generated_names = []

    

    for _ in range(num_names):
        
        name = random.choice(indian_names)
        last= random.choice(last_names)
        generated_names.append([name,last])
       
        

    return generated_names




# nltk.download('words')
# from nltk.corpus import words

def generate_username(num_usernames=1400):
    usernames = set()
    
    human_array = [element.replace(" ", "") for element in human_names]
    animal_array = [element.replace(" ", "") for element in animal_names]
    flower_array = [element.replace(" ", "") for element in flower_names]

    while len(usernames) < num_usernames:
        # Randomly select two words from the word list
        word1 = random.choice(list(flower_array + human_array + animal_array + username_list))
        # word2 = random.choice(list(animal_array + username_list))
        number = random.randint(101, 8999)
        symbols = "!@#$%^&*()_-+=<>?/|"
        symbol = random.choice(symbols)
        

        # Join the two words to create the username
        generated_username = f"{word1}{number}".capitalize()
        usernames.add(generated_username)
        if generated_username not in usernames:
            usernames.add(generated_username)

    return list(usernames)

# Example usage: generate 10 usernames by joining two real words

if __name__ == "__main__":
    generated_usernames = generate_username(num_usernames=1400)
    print((generated_usernames))
    random_indian_names = generate_indian_name(num_names=1400)
    print(random_indian_names)
