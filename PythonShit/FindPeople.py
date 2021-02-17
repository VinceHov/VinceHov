import vk
import random
import datetime, time
import requests
access_token = " " #API_KEY 
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)


list_word = ["А","а","Б","б","В","в","Г","г","Д","д","Е","е","Ё","ё","Ж","ж","З","з","И","и","Й","й","К","к","Л","л","М","м","Н","н","О","о","П","п","Р","р","С","с","Т","т","У","у","Ф","ф","Х","х","Ц","ц","Ч","ч","Ш","ш","Щ","щ","Ъ","ъ","Ы","ы","Ь","ь","Э","э","Ю","ю","Я","я","Я","я","A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]


    # Изменяемая часть
MY_ID = 507920843 # Твой ID (Используется если ты ищешь по группам)
age_range = range(18, 24) # От 18 до 26 лет
LAST_SEEN_ABLE = "2021-01-13" # Была в сети не раньше 10.10.2020

    # Просто блок инициализации
fields = ("last_seen", "can_write_private_message", "connections",'has_mobile', 'photo_max_orig', 'relation', 'followers_count', 'common_count') # Поля информации, которые мы получаем с пользователя
able_relations = [0, 1, 6] # Не замужем, Не указано, в активном поиске
good_persons = [] # Инициализация хороших тяночек
persons = []
calculate_tyan = 0

def find_tyan(): # Фукнция для поиска тяночек
    for iterator in age_range: # Дробим запросы на критерии
        print("get some tyan")
        response = api.users.search(count=1000, fields=fields, city=143, country=1, age_from=iterator, age_to=iterator, sex=1, offset=0, sort=0, has_photo=1) # Получаем тяночек
        persons.extend(response['items'])
        time.sleep(0.4) # Обходим ограничение на число запросов в секунду

def find_tyan_from_groups(myid): # Функция для поиска тяночек среди наших групп. Сюда надо закинуть свой id 
    global calculate_tyan
    groups = api.groups.get(user_id=myid, count=1000)['items']
    index = 1 
    for group in groups: 
        print(str(index), "tyan group of", len(groups)) 
        
        groupMembers = []
        offset_group = 0 
        try:
            while api.groups.getMembers(group_id=group, count=1, offset=offset_group, fields=('sex', 'city', 'country', 'photo_max_orig', 'has_mobile', 'can_write_private_message', 'last_seen', 'bdate', 'relation'))['items'] != []:
                offset_group += 1000
                try:
                    groupMembers.extend(api.groups.getMembers(group_id=group, count=1000, offset=offset_group, fields=('sex', 'city', 'country', 'photo_max_orig', 'has_mobile', 'can_write_private_message', 'last_seen', 'bdate', 'relation'))['items'])
                except:
                    index += 1
                    continue
                for groupMember in groupMembers:
                    calculate_tyan += 1 
                    if 'country' in groupMember and 'city' in groupMember and 'bdate' in groupMember and groupMember['sex'] == 1 and groupMember['can_write_private_message'] == 1 and 'relation' in groupMember and 'last_seen' in groupMember:
                        if groupMember['country']['id'] == 1 and groupMember['city']['id'] == 1 and len(groupMember['bdate']) > 8 and datetime.datetime.fromtimestamp(groupMember['last_seen']['time']).strftime('%Y-%m-%d') >= LAST_SEEN_ABLE:
                            if groupMember['relation'] in able_relations and int(datetime.datetime.now().strftime('%Y')) - int(groupMember['bdate'].split(".")[2]) in age_range:
                                if not groupMember in good_persons: # Типо фильтрую тяночек, да
                                    good_persons.append(groupMember)
                                    print("Нашли тяночку!!! Уже", len(good_persons))
                index += 1
        except:
            continue

def sort_good(): # Функция для сортировки хороших тяночек
    for person in persons:
        try:
            if (person['can_write_private_message'] == 1 and datetime.datetime.fromtimestamp(person['last_seen']['time']).strftime('%Y-%m-%d') >= LAST_SEEN_ABLE and 
            person['relation'] in able_relations and person['followers_count'] <= 700): # Делаем проверку, можно ли написать ей и не мертва ли она
                good_persons.append(person) # Добавляем в список хороших 
        except:
               continue
def print_log():
    print(len(good_persons), "of", len(persons)) # Логгируем выходные значения
    print(good_persons[0]) 

def download_avatar(destination): # Функция для скачивания аватарки тяночки. Формат вывода: id .jpg
    for good_person in good_persons:
        image = requests.get(good_person['photo_max_orig']).content
        file = open("D:/" + destination + "/id" + str(good_person['id']) + ".jpg", "wb")
        file.write(image)
        file.close

def find_tyanochku_base(): # Тупо тяночек по городу ищет
    find_tyan() 
    sort_good()
    print_log()
    download_avatar("grab_tyan_roman")

def find_tyanochku_extended(): # Ищет тяночек по увлечениям
    global good_persons
    global MY_ID
    find_tyan_from_groups(MY_ID)
    print("%d Тяночек подходит из %d" % (len(good_persons), calculate_tyan))
    download_avatar("grab_tyan_vince")

# find_tyanochku_base()
find_tyanochku_extended()