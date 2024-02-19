import colorama
import random
import time

red=colorama.Fore.RED
green=colorama.Fore.GREEN
blue=colorama.Fore.BLUE
magenta=colorama.Fore.MAGENTA
reset=colorama.Style.RESET_ALL

klasses={
    'лучник':{'здоровье':80,
              'атака':40,
              'защита':20,
              'навыки':{
                  'бег':8,
                  'стрельба':10
              } },
    'воин':{
        'здоровье':100,
        'атака':35,
        'защита':25,
        'навыки':{
            'щит':8,
            'сила':10
        } },
    'маг':{'здоровье':50,
           'атака':40,
           'защита':15,
           'навыки':{
               'магический щит':10,
               'выздоравливание':5
           } }
}
rol={'1':'лучник',
     '2':'воин',
     '3':'маг'
}

print(f"{blue} Здравствуйте, это игра-дуэль.{reset}")

def name_hero():
    name_h=input("Имя героя: ")
    while name_h=="":
        name_h=input("Имя героя: ")
    return name_h

def name_enemy():
    f_name=['doctor','professor','mega','letaushii']
    s_name=['strange','aibolit','mozg','zlodey']
    two_name=random.choice(f_name) +" "+ random.choice(s_name)
    return two_name

def create_person(name, is_enemy):
    if is_enemy==True:
        rol_enemy=random.choice(list(rol.values()))
        person={'name':name, 'class':rol_enemy, 'skills':klasses[rol_enemy]}
    else:
        print(list(rol.items()))
        ro_hero=input('Введи 1,2 или 3: ')
        chislo=['1','2','3']
        while ro_hero not in chislo:
            ro_hero = input("Введи 1,2 или 3: ")
        person = {'name':name, "class": rol[ro_hero], "skills": klasses[rol[ro_hero]]}

    return person


def skill(person, is_enemy):
    if is_enemy == True:
        ski=random.choice(list(person["skills"]['навыки'].keys()))
        print(f"{blue}Для врага выбран такой навык: {ski}{reset}")

    else:
        ski=input(f'Выберите свой скилл:  {list(person['skills']['навыки'].keys())}  ')
        while ski not in person['skills']['навыки']:
            ski = input(f'Выберите свой скилл:  {list(person['skills']['навыки'].keys())}')
        print(f"{blue}Вы выбрали: {ski}{reset}")
    return person["skills"]['навыки'][ski]

def attack(p1, p2, is_enemy):
    print(f'{magenta}{p1['name']} аттакует {p2['name']}{reset}')
    if is_enemy==True:
        sk = skill(hero, False)
    else:
        sk=skill(enemy, True)
    damage= p1['skills']['атака']-p2['skills']['защита']
    if damage<0:
        damage=1
    p2['skills']['здоровье']+=sk
    p2['skills']['здоровье']-=damage
    print(f'{blue}Игрок {p1['name']} наносит {damage} урона.{reset}')
    time.sleep(2)
    print(f'{blue}У игрока {p2['name']} осталось {p2['skills']['здоровье']} здоровья{reset}')


def fight(attacer, defender):
    ch = 0
    while True:

        time.sleep(2)
        if attacer['skills']["здоровье"]>0:
            ch+=1
            print(f'{magenta} Раунд {ch}{reset}')
            time.sleep(2)
            attack(attacer, defender, False)
        else:
            print(f'{red}{attacer['name']}  проиграл{reset}')
            print(f"{red}{defender['name']}  выиграл{reset}")
            break
        if defender['skills']["здоровье"]>0:
            ch += 1
            print(f'{magenta}  Раунд {ch}{reset}')
            time.sleep(2)
            attack(defender, attacer, True)
        else:
            print(f'{red}{defender['name']}  проиграл{reset}')
            print(f"{green}{attacer['name']}  выиграл{reset}")
            break
        input('Нажмите Enter чтобы продолжить')


na_ene=name_enemy()
enemy=create_person(na_ene, True)


na_hero=name_hero()
hero=create_person(na_hero, False)




print( f"{green} {hero} {reset}")
print(f"{magenta}{enemy}{reset}")
fight(hero, enemy)
