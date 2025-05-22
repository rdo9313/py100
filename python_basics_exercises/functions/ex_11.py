def greet(iso):
    match iso:
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def english_greetings(region):
    match region:
        case 'US':
            return 'Hey!'
        case 'GB':
            return 'Hello!'
        case 'AU':
            return 'Howdy!'
        
def extract_language(locale):
    return locale.split("_")[0]

def extract_region(locale):
    return locale.split(".")[0].split("_")[1]

def local_greet(locale):
    iso = extract_language(locale)
    region = extract_region(locale)

    if iso == 'en':
        return english_greetings(region)
    
    return greet(iso)


print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!