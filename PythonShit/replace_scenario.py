# -*- coding: utf-8 -*-
import re 
text = u"\nГг: по-моему это здесь.\n\nДевушка секретарь:\nЗдравствуйте молодой\nчеловек, а вы к кому ?\n\nГг: я к Сергею\nВикторовичу вашему\nпрофессиональному как в\nинтернете было написано\nпсихологу.\n\nДевушка секретарь:\n*ничего не ответив она\nпровела меня до крайнего\nкабинета в этом зданий*\n\nГг: Здравствуйте вы\nсвободны \n\nПсихолог: входите.\nСлушаю вас ?\n\nГг: я нашёл вас в\nинтернете, говорят вы\nхороший психолог ?\n\nПсихолог: да ? А с чего вы\nтак решили ?\n\nГг: ну как по мне хороший\nпсихолог, это тот к кому\nпосле пару курсов\nпосещения , не\nвозвращаются снова ибо\nон им помог.\n\nГг: а то бывает люди\nшарлатаны что просто\nтянут время и деньги, \nпациента что их посещает.\n\nПсихолог: ну это вы верно\nподметили.\n\nПсихолог: я отнюдь\nвижу, вы сами человек не\nпальцем деланный.\n\nГг: * вопросительно\nпосмотрел на психолога*\n\nПсихолог: ну голубчик я\nобычно проверяю историю\nпо карте пациента , кто он\nи кем является , по его\nдиагнозам. Обычно я\nберусь за людей что\nлечатся тут в местной \nбольнице.\n\nПсихолог: Если спросите\nкак ?  То больница что\nстоит напротив, место где\nвы состоите на учёте и\nявляетесь ее резидентом.\nЯ был врачом в ней на\nпротяжений нескольких\nлет, благодаря моим\nбылым заслугам и\nопределенных выгод для\nсамой больницы,она\nвыдаёт мне истории\nболезни пациентов\nчто посещают меня, вы\nзаписались ко мне за три\nдня, до посещения.\nВот я и навёл о вас\nсправки да уж, ваше\nистории болезни желают\nоставлять лучшего .\n\nПсихолог: но вы пришли\nсюда осознанно, так что я\nвас внимательно слушаю.\n\nГг: да уж я теперь жалею\nчто посетил вас , но и\nобращаться к кому нету\nжелания да и что нужно вы\nобо мне знаете.\nТак что не вижу смысла\nуходить.\n\nПсихолог: да это верно к\nтому же вы оплатили\nзаранее несколько\nкурсов , а деньги назад мы\nне возвращаем.\n\nГг: дело не в деньгах, а в\nрезультате.\n\nПсихолог: ладно теперь\nближе к вашей проблеме, \nчто вас беспокоит?\n\nГг: Я за такое короткое\nвремя, пережил то что\nизменили в корне мою\nжизнь, я был на волосок от\nсуицида , думал спрыгнуть\nс крыши или обожраться\nтаблетками , ну и на \nкрайний случай  феном в\nванной , для получения\nцинкового гроба.\n\nПсихолог: давайте по\nподробнее с начало , что\nвас беспокоит?\n\nГг: ну.....\n(начало истории)\n\nГг: Меня зовут ..... и мне\n20 , вот-вот будет 21 . А\nвроде только вчера\nпосещал школу.\nЯ был думером, если вы\nспросите кто такой\nдумер ,то вкратце думеры\n- это псевдодепрессивные\nлюди. Ибо как по мне\nдепрессии как таковой\nнет . Это лишь состояния\nдуши которые мы сами\nсебе внушаем. Такие люди \nстрого не привязаны ни к\nкакому конкретному\nпоколению, а скорее\nхарактеризуются своим\nподавленным\nэмоциональным\nсостоянием, но всё же\nчаще принято соотносить\nего с поколением 90-х.\nТаких людей вряд ли\nназовёшь серыми\nмышами,но и королями\nвечеринок ,они тоже не\nявляются. Мешки под\nглазами, грязные волосы ,\nбывает и длинные\nпатлы ,сигарета, чёрная\nшапка , чёрная одежда , в\nоснове это что то удобное,\nкак штаны от спортивок, и\nбольшого размера кофта с\nкапюшоном, глубокие и не\nособо всем ясные ,мысли\nо мироздании и чем то \nвысшем , о том самом\nбытье - вот главные\nатрибуты думера. Выходит\nполное описание меня\nсамого. Хотя точного\nответа нет ,ни у кого.....\nЯ жил самой обычной\nжизнью ,являясь не\nуделом у всех . Мать\nхотела что бы я был\nнормальным , что является\nтипичным ,детский сад ,\nпродлёнка , школа ,\nунивер , жена , ребёнок ,\nармия , потом работа . Тот\nсамый нормальный чтоб\nбыл на шее галстук, был\nнормальным мать\nготовила бы пасту , быть\nнормальным отдавать\nжене свою зарплату , по\nскидону иметь золотую\nкарту. Стоп это все полная\nчушь не так ли ?Ну я так \nсчитаю.\nДрузья ,знакомые,\nотвернулись от меня по\nвсякой ерунде , знаете эти\nсамые подростковые\nслухи, завистники и\nподобные люди , увы я в\nтакие детские игры не\nиграл , вот и остался у\nразбитого корыта , один да\nи в гордости .\nДа и вообще есть ли это\nсамая дружба ?\nНу я так думал что дружбы\nне бывает, и все хотят\nпроцентов . У меня было\nпарочку друзей и то я им\nне верил , я не верил и\nсебе , тратя попусту\nденьги , все бы ничего но\nпо итогу я сейчас жалею.\nНе любил я анорексичек\nлюбил с фигурой\nпосочнее , да каким был я, \nи каким сейчас стал, я\nнаучился ценить жизнь ,\nлюдей , их внутренний\nмир, и стал более живым и\nуверенным в себе.\nИногда бывало не спал\nсутками, думая о жизни ,\nчто делать дальше , как\nжить в этом мире , и зачем\nя ему нужен.\nНу и сидел за и\nпривычным для всех\nдосугом , это социальные\nсети , в которых даже\nтам ,у меня нету людей с\nкоторыми я могу\nпоговорить ,и не\nчувствовать себя странно.\nЯ занимался музыкой , ну\nкак музыкой я писал\nглупые песенки про\nлюбовь , которые кто\nболее менее впитывал ,\nбыло даже пару \nконцертов , малолетки\nлюбили меня , это было\nвсе так наяву , а теперь я\nвижу это только во сне. Я\nне сильно переживаю на\nэтот счёт, ибо все\nприходит и уходит , осадок\nвсе же остался , но с кем\nне бывает да ?\nЖиву я более-менее\nсамодостаточно , квартира\nв центре, мог позволить\nсебе дорогие вещи ,\nхороший алкоголь,\nутонченные сигареты , еду\nв ресторанах , прочее\nобывательская ерунда, о\nкотором мечтает простой\nчеловек.\nУ меня была не взаимная\nлюбовь , был я в вечной\nфрендзоне, в один\nпрекрасный день , моя\nмуза прямым текстом \nответила , ты конечно\nприкольный паренёк , но\nна тебя у меня нету\nвремени, да и желания , к\nтому же ты себя видел ?\nОтчасти она была права , я\nуже был не тот парниша\nкак в 16-17 лет , вы\nнаверное думаете, что же\nмогло изменится, за за\nстоль короткий срок, я вам\nотвечу многое , но не\nсуть .\nС чего вообще началось\nэто приключение .\n"
regex = r'(?s)(?<=\n).*?:.*?(?=\n\n)'

test_list = re.findall(regex, text)

for test in test_list:
	while "\n" in test:
		test = test.replace("\n", " ")
	print(test, '\n')
# print(test_list)
