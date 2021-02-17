from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.common.keys import Keys
import time
# import win32com.client

cookies = {'domain': '.mos.ru', 'expiry': 1703324500, 'httpOnly': True, 'name': 'ag_session_id', 'path': '/', 'secure': False, 'value': 's%3AsnYx2QkywVTZSewjl4Yje18J-zL_UOeK.TF6sAcJTEO0Od6A3l6WsU0wphhS8pv61iTnk8e6PN8w'}

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
opts = Options()
opts.add_argument("user-agent=%s" % user_agent)


dr = webdriver.Chrome(chrome_options=opts)	
dr.get("https://ag.mos.ru/poll?filters=active")
dr.delete_cookie("ag_session_id")
dr.add_cookie(cookies)

bs = BeautifulSoup(dr.page_source,"lxml")
dr.refresh()
dr.maximize_window() 
answers = {
"«Осенний марафон – 2020». История и культура Москвы. 1-й этап": ["Неглинная", "Репортером", "«Моя улица»", "Тверская", "65 метров", "Царицыно"],
"«Осенний марафон – 2020». История и культура Москвы. 2-й этап": ["В сентябре", "На Тверской площади", "В здании ЦУМа", "Георгий Данелия", "На Ивановской площади", "В 1917 году большевики разделили город на восемь районов"],
"«Осенний марафон – 2020». Москва активного гражданина. 1-й этап": ["Медвежонок Миша", "Скандинавская ходьба", "Саудовской Аравии", "Поганые болота", "42,2 км и 21 км", "Улицу Николая Старостина"],
"«Осенний марафон – 2020». Москва активного гражданина. 2-й этап": ["Окончания Смутного времени и изгнания польских интервентов", "Нос собаки пограничника", "1", "«День без турникетов»", "«Торпедо»", "195"],
"«Осенний марафон – 2020». Москва – город возможностей. 1-й этап": ["125", "«Тройка»", "108,9 км", "«Спорт в метро»", "Запись ребенка в первый класс и получение единого платежного документа", "Главный военный клинический госпиталь имени Н.Н. Бурденко"],
"«Осенний марафон – 2020». Москва – город возможностей. 2-й этап": ["В Александровском саду", "В январе 2020 года", "Печатники", "Дворец гимнастики Ирины Винер-Усмановой", "Мотоцикл", "Розовый"]}
def _login(login):
	dr.find_element_by_class_name("menu-toggle.ng-tns-c194-1").click()
	dr.execute_script("document.getElementsByClassName('header-menu-mobile__auth-actions ng-tns-c198-0 ng-star-inserted')[0].children[0].click()")
	dr.find_element_by_class_name("button.button--muted.button--fill.button--special-red").click()
	time.sleep(1)
	login_shit =  str('document.getElementById("login").value = "' + login + '"')
	dr.execute_script(login_shit)
	dr.execute_script('document.getElementById("password").value = "zFKTRC3"')
	dr.find_element_by_class_name("btn.btn-lg.btn-primary.btn-block.bc-form-btn").click()

# _login(login)

def do_things():
	global dr
	dr.get("https://ag.mos.ru/poll?filters=active")
	try:
		dr.refresh()
	except:
		try:
			Alert(dr).dismiss()
		except:
			try:
				Alert(dr).dismiss()
			except:
				dr.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
				dr.execute_script("window.open('');")
				dr.switch_to.window(dr.window_handles[0])
				dr.close()
				dr.switch_to.window(dr.window_handles[0])
				dr.get("https://ag.mos.ru/poll?filters=active")
				pass
			pass

	buttons = dr.find_elements_by_class_name('button')
	if buttons == []:
		do_news()
		exit()
	buttons[0].click()
	
	def click_radiobuttons(wtf=None):
		radiobuttons = dr.find_elements_by_class_name("poll-answer__icon.input-radio")
		if radiobuttons == [] or wtf == "checkbox":
			radiobuttons = dr.find_elements_by_class_name("input-checkbox")
		return radiobuttons
	
	if dr.find_element_by_tag_name("h1").text in answers:
		do_maraphone()
		exit()

	try:
		dr.execute_script('document.getElementsByTagName("ag-poll-description")[1].parentElement.children[2].children[0].children[0].children[0].children[1].click()')
	except:
		click_radiobuttons()[0].click()
	
	polls = dr.find_elements_by_tag_name("ag-poll-description")
	index = 2
	if polls != [] and len(polls) != 2:
		for poll in polls[2:]:
			dr.execute_script('document.getElementsByTagName("ag-poll-description")[%d].click()' % index)
			try:
				dr.execute_script('document.getElementsByTagName("ag-poll-description")[%d].parentElement.children[1].children[0].children[0].children[0].children[1].click()' % index)
			except:
				dr.execute_script('document.getElementsByTagName("ag-poll-description")[%d].click()' % index)
				dr.execute_script('document.getElementsByTagName("ag-poll-description")[%d].parentElement.children[1].children[0].children[0].children[0].children[1].click()' % index)

			index += 1

	dr.find_element_by_class_name("submit-button.button.button--green").click()
	try:
		dr.execute_script('document.getElementsByClassName("button button--fill button--muted")[0].click()')
	except:
		pass
	do_things()

def do_news():
	global dr
	dr.get("https://ag.mos.ru/novelties?filters=active")
	dr.refresh()

	buttons = dr.find_elements_by_class_name('button')
	if buttons == []:
		do_pulse()
		exit()
	buttons[0].click()
	dr.execute_script('document.getElementsByClassName("rating-icon ng-star-inserted")[4].click()')
	try:
		dr.find_element_by_class_name("form__submit.button.button--attention.button--fill").click()
	except:
		do_news()
	try:
		Alert(dr).dismiss()
	except:
		try:
			Alert(dr).dismiss()
		except:
			pass
		pass
	do_news()

def do_pulse():
	global dr
	dr.get("https://ag.mos.ru/home")
	dr.refresh()
	time.sleep(2)
	try:
		dr.find_element_by_class_name("banner.ng-star-inserted").click()
	except:
		do_maraphone()
		dr.quit()
	time.sleep(1)
	dr.find_element_by_class_name("answer-wrapper.answer-wrapper--3.ng-star-inserted").click()
	do_maraphone()
	dr.quit()

def do_maraphone(i=0, tab=1):
	global dr
	print(tab)
	dr.get("https://ag.mos.ru/promo/autumn2020?utm_source=banner&utm_medium=banner&utm_campaign=autumn2020")
	dr.refresh()
	time.sleep(1)
	dr.find_elements_by_class_name("fake-input-button.form-input-text.participant-form-field")[1].click()
	try:
		dr.find_element_by_class_name("form-field").click()
		dr.find_elements_by_class_name("day-cell.ng-star-inserted")[11].click()
		dr.find_element_by_class_name("button.button--fill").click()
		time.sleep(1)
		dr.find_element_by_class_name("modal-window__close-button.ng-star-inserted").click()
		dr.find_element_by_class_name("wrapper-avatar").click()
		dr.find_elements_by_class_name("sr-only")[2].send_keys("C:\\murk.jpg")
		dr.find_element_by_class_name("button.button--fill.avatarAnalytics").click()
		dr.find_element_by_class_name("switch.ng-star-inserted").click()
		dr.find_element_by_class_name("button.button--fill").click()
		dr.find_element_by_class_name("btn.btn-participant-number").click()
		dr.find_element_by_class_name("btn.button--fill.btn-green").click()
	except:
		pass
	time.sleep(2)
	if tab == 1:
		dr.find_element_by_class_name("btn.btn--stroked.button--fill.btn-green").click()
	elif tab == 2:
		try:
			dr.find_element_by_class_name("btn.button--fill.btn-red").click()
		except:
			pass
		finally:
			time.sleep(1)
			try:
				dr.find_element_by_class_name("btn.btn--stroked.button--fill.btn-red").click()
			except:
				pass
	elif tab == 3:
		try:
			dr.find_element_by_class_name("btn.button--fill.btn-orange").click()
		except:
			pass
		finally:
			time.sleep(1)
			try:
				dr.find_element_by_class_name("btn.btn--stroked.button--fill.btn-orange").click()
			except:
				pass
	elif tab == 4:
		dr.get("http://kotomatrix.ru/")
		dr.quit()
		exit()
	time.sleep(3)
	dr.execute_script('document.getElementsByClassName("marathon-poll-wrapper marathon-poll-link ng-star-inserted")[%d].click()' % i)
	time.sleep(3)
	dr.switch_to.window(dr.window_handles[1])
	poll_name = dr.find_element_by_tag_name("h1").text

	polls = dr.find_elements_by_tag_name("ag-poll-question")
	index = 0 
	for poll in polls:
		time.sleep(1)
		try:
			poll.click()
		except:
			dr.find_element_by_class_name("modal-window__close-button.ng-star-inserted").click()
			rb.click()
			time.sleep(2)
			poll.click()
		variants = poll.find_elements_by_tag_name("ag-variant")
		for variant in variants:
			try:
				text, rb = variant.find_element_by_tag_name("span").text, variant.find_element_by_tag_name("app-radio-button")
			except:
				dr.close()
				dr.switch_to.window(dr.window_handles[0])
				if i == 0:
					do_maraphone(1, tab=tab)
				else:
					do_maraphone(tab=tab + 1)
			if text == answers[poll_name][index]:
				try:
					rb.click()
				except:
					time.sleep(1)
					rb.click()
		index += 1
	
	dr.find_element_by_class_name("submit-button.button.button--green").click()
	dr.close()
	dr.switch_to.window(dr.window_handles[0])
	if i == 0:
		do_maraphone(1, tab=tab)
	elif i == 1 and tab != 3:
		do_maraphone(tab=tab + 1)

	print(i, tab)
	dr.get("http://kotomatrix.ru/")
	dr.quit()
	exit()

try:
	do_things()
except:
	dr.quit()
	dr = webdriver.Chrome(chrome_options=opts)	
	dr.get("https://ag.mos.ru/poll?filters=active")
	dr.delete_cookie("ag_session_id")
	dr.add_cookie(cookies)
	bs = BeautifulSoup(dr.page_source,"lxml")
	dr.refresh()
	dr.maximize_window() 
	do_things()
