import vk
import random
import time
access_token = " " # API_KEY
session = vk.Session(access_token=access_token)
v = '5.95'
api = vk.API(session, v=v)

text = []

text.append(u'Красивая бабенка с аккуратными очками на лице, живет со своим парнем на съемной квартире и чтобы оплачивать кварплату и проживание во время пандемии, они перешли в режим онлайн работы. Ежедневно транслируя свой рабочий день с восьми до восьми, но работа как вы поняли заключается не в подсчете бухгалтерии, а самый что есть настоящий секс по вебке.')
text.append(u'Студенты в общаге сделали из общей комнаты большое, раскладное ложе любви, на котором чпокали на камеру соседских девчонок с верхних этажей, а вечером пропивали их вместе. И вот лежат три дрочера, а между ними по очереди ползает голая девица, отсасывая каждому, ее подруга оказалась стеснительной и оставалась за кадром, периодически заглядывая в объектив.')
text.append(u'Пацан друга в беде не бросил после разрыва долгих отношений с девушкой, чтобы тот не находился в одиночестве, чувак позвал его с собой на свидание с женой. Девушка была не против тройничка, но в свою писечку чужой член не впустила, только отсосала и за этим наблюдал молодой куколд, теребонькая свое хозяйство ручонкой.')
text.append(u'Курьер привез пиццу по Московскому адресу, а там домохозяйка без денег, в одном халатике на голое тело. Молвит юноше на иностранном не правильном языке, мол заплатить нечем, но могу хорошенько отработать глоткой твой пичуган. Пошарил в карман и нашел чем заплатить за нее, вынул хозяйство из штанин и сунул ей его в рот.')

for message in text:
	try:
		api.messages.send(random_id=random.randint(0,100000), chat_id=122, message=message)
	except:
		time.sleep(10)
		api.messages.send(random_id=random.randint(0,100000), chat_id=122, message=message)