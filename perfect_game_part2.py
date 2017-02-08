from time import sleep
from selenium import webdriver
import csv
import sys
from queue import Queue
from threading import Thread
from datetime import datetime

q = Queue(maxsize=0)
base_url = "http://www.perfectgame.org/Players/"

#-----------------------------------------------------------------------------------------
in_file_name = "links350_400"
num_of_threads = 4
#-----------------------------------------------------------------------------------------
out_file_name = "contact_data"+in_file_name[-7:]+".csv"

start_time = datetime.now()
file_txt = open("C:\\Users\\emirh\\PycharmProjects\\untitled\\Other\\"+in_file_name+".txt" , "r")
urls = file_txt.readlines()
file_txt.close()
print(len(urls))

for url in urls:
    q.put(url)

file_csv = open(out_file_name, "w", newline='', encoding='utf-8')
csv_writer = csv.writer(file_csv, dialect=csv.excel)
csv_writer.writerow(["ID","Name and Surname","Address","Phone","Email", "HS Coach", "Coach Phone", "Coach Email", "Player DOB", "Player's other sports", "Player's glasses/contacts", "Father", "Father's athletic history", "Father's college", "Mother", "Mother's athletic history", "Mother's college"])

address="";phone="";email="";hs_coach="";phone_coach="";email_coach="";player_dob="";player_other_sports="";player_glasses="";
father="";father_athl_hist="";father_college="";mother="";mother_athl_hist="";mother_college=""
def parserilion():
    driver = webdriver.Chrome(r"chromedriver.exe")
    driver.set_window_size(1500,1080)
    driver.get("http://www.perfectgame.org/")
    driver.find_element_by_id("signdiv").click()
    driver.find_element_by_name("ctl00$Header1$HeaderTop1$tbUsername").send_keys("hockeyscoutingca@hotmail.com")
    driver.find_element_by_name("ctl00$Header1$HeaderTop1$tbPassword").send_keys("bballstats10")
    driver.find_element_by_name("ctl00$Header1$HeaderTop1$Button1").click()

    while not q.empty():
        try:
            driver.get(base_url + q.get().replace("\n", ""))
            name = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblName").text
            url_id = driver.find_element_by_id("ContentPlaceHolder1_Bio1_hlOverview").get_attribute("href")[-6:]
            driver.execute_script("window.scrollTo(0, 1100);")
    #-----------------------------------------------------------------------------------
            try:
                driver.find_element_by_id("ContentPlaceHolder1_lbDisplayContact").click()
                try:
                    sleep(1)
                    address = driver.find_element_by_id("ContentPlaceHolder1_lblAddress").text.replace("\n"," ")
                    phone = driver.find_element_by_id("ContentPlaceHolder1_lblPhone").text
                    email = driver.find_element_by_id("ContentPlaceHolder1_lblEmail").text
                except:
                    sleep(1)
                    address = driver.find_element_by_id("ContentPlaceHolder1_lblAddress").text.replace("\n"," ")
                    phone = driver.find_element_by_id("ContentPlaceHolder1_lblPhone").text
                    email = driver.find_element_by_id("ContentPlaceHolder1_lblEmail").text
            except:
                address = "NaN";
                phone = "NaN";
                email = "NaN";
    #-------------------------------------------------------------------------------------
            try:
                driver.find_element_by_id("ContentPlaceHolder1_lbCoach").click()
                try:
                    sleep(1)
                    hs_coach = driver.find_element_by_id("ContentPlaceHolder1_lblCoachName").text
                    phone_coach = driver.find_element_by_id("ContentPlaceHolder1_lblCoachPhone").text
                    email_coach = driver.find_element_by_id("ContentPlaceHolder1_lblCoachEmail").text
                except:
                    sleep(1)
                    hs_coach = driver.find_element_by_id("ContentPlaceHolder1_lblCoachName").text
                    phone_coach = driver.find_element_by_id("ContentPlaceHolder1_lblCoachPhone").text
                    email_coach = driver.find_element_by_id("ContentPlaceHolder1_lblCoachEmail").text
            except:
                hs_coach = "NaN";
                phone_coach = "NaN";
                email_coach = "NaN";
    #-----------------------------------------------------------------------------------------
            sleep(1)
            driver.execute_script("window.scrollTo(0, 1400);")
            try:
                driver.find_element_by_id("ContentPlaceHolder1_lbDetails").click()
                try:
                    sleep(1)
                    player_dob = driver.find_element_by_id("ContentPlaceHolder1_lblDOB").text
                    player_other_sports = driver.find_element_by_id("ContentPlaceHolder1_lblothersports").text
                    player_glasses = driver.find_element_by_id("ContentPlaceHolder1_lblglasses").text
                    father = driver.find_element_by_id("ContentPlaceHolder1_lblFather").text
                    father_athl_hist = driver.find_element_by_id("ContentPlaceHolder1_lblFatherAthletic").text
                    father_college = driver.find_element_by_id("ContentPlaceHolder1_lblFatherCollege").text
                    mother = driver.find_element_by_id("ContentPlaceHolder1_lblMother").text
                    mother_athl_hist = driver.find_element_by_id("ContentPlaceHolder1_lblMotherAthletic").text
                    mother_college = driver.find_element_by_id("ContentPlaceHolder1_lblMotherCollege").text
                except:
                    sleep(1)
                    player_dob = driver.find_element_by_id("ContentPlaceHolder1_lblDOB").text
                    player_other_sports = driver.find_element_by_id("ContentPlaceHolder1_lblothersports").text
                    player_glasses = driver.find_element_by_id("ContentPlaceHolder1_lblglasses").text
                    father = driver.find_element_by_id("ContentPlaceHolder1_lblFather").text
                    father_athl_hist = driver.find_element_by_id("ContentPlaceHolder1_lblFatherAthletic").text
                    father_college = driver.find_element_by_id("ContentPlaceHolder1_lblFatherCollege").text
                    mother = driver.find_element_by_id("ContentPlaceHolder1_lblMother").text
                    mother_athl_hist = driver.find_element_by_id("ContentPlaceHolder1_lblMotherAthletic").text
                    mother_college = driver.find_element_by_id("ContentPlaceHolder1_lblMotherCollege").text
            except:
                player_dob = "NaN";
                player_other_sports = "NaN";
                player_glasses = "NaN";
                father = "NaN";
                father_athl_hist = "NaN";
                father_college = "NaN";
                mother = "NaN";
                mother_athl_hist = "NaN";
                mother_college = "NaN"
            csv_writer.writerow([url_id,name,address,phone,email,hs_coach,phone_coach,email_coach,player_dob,player_other_sports,player_glasses,father,father_athl_hist,father_college,mother,mother_athl_hist,mother_college])
            file_csv.flush()
        except:
            address = "NaN";
            phone = "NaN";
            email = "NaN";
            hs_coach = "NaN";
            phone_coach = "NaN";
            email_coach = "NaN";
            player_dob = "NaN";
            player_other_sports = "NaN";
            player_glasses = "NaN";
            father = "NaN";
            father_athl_hist = "NaN";
            father_college = "NaN";
            mother = "NaN";
            mother_athl_hist = "NaN";
            mother_college = "NaN"
            print(str(url_id) + " last: " + str(sys.exc_info()[0]))
        csv_writer.writerow([url_id, name, address, phone, email, hs_coach, phone_coach, email_coach, player_dob, player_other_sports, player_glasses, father, father_athl_hist, father_college, mother, mother_athl_hist, mother_college])
        print(url_id)
        file_csv.flush()
        q.task_done()

for i in range(num_of_threads):
    t1 = Thread(target = parserilion)
    t1.start()

q.join()

file_csv.close()

print (datetime.now()-start_time)
