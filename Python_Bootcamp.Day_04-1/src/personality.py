import random

def turrets_generator():
    traits = ['neuroticism', 'openness', 'conscientiousness', 'extraversion', 'agreeableness']
    trait_values = [random.randint(0, 100) for _ in range(5)]
    total_traits = sum(trait_values)
    trait_probs = [value * 100 // total_traits for value in trait_values]
    trait_probs[4] = 100 - sum(trait_probs[:4])

    def shoot():
        print("Shooting")
    
    def search():
        print("Searching")
    
    def talk():
        print("Talking")
    
    turret_class = {
        trait: trait_probs[i] for i, trait in enumerate(traits)
    }
    
    turret_instance = {
        'shoot': shoot,
        'search': search,
        'talk': talk
    }

    return type('Turret', (object, ), dict(list(turret_class.items()) + list(turret_instance.items())))

turret = turrets_generator()
print(type(turret))

turret.shoot()
turret.search()
turret.talk()

print(turret.neuroticism)
print(turret.openness)
print(turret.conscientiousness)
print(turret.extraversion)
print(turret.agreeableness)
