from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
path = "C:\\Users\\Apocalypse\\Desktop\\House_Prediction\\Web_scrapping\\chromedriver_win32\\chromedriver.exe"
#loading Driver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
# Load the CSV file and extract the URLs
with open('c://users//apocalypse//house_links_nepalhomes.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    urls = [row[0] for row in csv_reader]
print(urls[0])
# driver.get(urls[0])
# div_components =driver.find_elements(by='xpath',value='//*[@id="sectionOverview"]/ul/li/div')
# for component in div_components:
#     print(component.text)
# print(land_area)
# data_dict ={}
# for li in div_components:
#     title = li.find_element(by='xpath',value='//*[@id="sectionOverview"]/ul/li/div/h3').text
#     value=li.find_element(by='xpath',value='//*[@id="sectionOverview"]/ul/li/div/h5').text
#     data_dict[title]=value
    


# print(data_dict)
# for i in land_area:
#     print(i.text)
# # data_dict = {}
# for url in urls:
#     driver.get(url)

#     div_components = driver.find_elements(by='xpath', value='//*[@id="sectionOverview"]/ul/li/div')

#     data_dict = {}

#     for component in div_components:
#         # Get the h3 and h5 elements
#         h3_element = component.find_element(by='xpath', value='./h3')
#         h5_element = component.find_element(by='xpath', value='./h5')

#         # Get the text from the h3 and h5 elements
#         title = h3_element.text
#         value = h5_element.text

#         # Store the data in the dictionary with the title as key
#         data_dict[title] = value

#     # Print the dictionary
#     print(data_dict)

# driver.get(urls[0])
# main_component = driver.find_element(by='xpath',value='//*[@id="__next"]/div[3]/div[3]/section[1]/div/div/div[2]/div[1]')
# print(main_component.text)
# title = main_component.find_element(by='xpath',value='./div/div/div/div/h1')
# location = main_component.find_element(by='xpath',value='./div/div/div/div/p[@class="location"]')
# price=main_component.find_element(by='xpath',value='./div/div/div/div/p[@class="price"]')
# posted_on = main_component.find_element(by='xpath',value='./div/div/div[@class="details--hero-header-sub"]/span[4]')
# views = main_component.find_element(by='xpath',value='./div/div/div[@class="details--hero-header-sub"]/span[5]')
# print(title.text,"\n",location.text)
# print(price.text)
# print(posted_on.text[11:])
# print(views.text[:3])
# amenity_dataset={}
# Amenities = main_component.find_elements(by='xpath',value='./div/div[@id="sectionAmenities"]/ul')
# for i in Amenities:
#     amenity_dataset['amenity']=i.text.replace("\n",",")
# # print(Amenities.text)
# print(amenity_dataset)
data_list=[]
start_time = time.time()
for url in urls:
    driver.get(url)
    data_dict = {}
    main_component = driver.find_element(by='xpath',value='//*[@id="__next"]/div[3]/div[3]/section[1]/div/div/div[2]/div[1]')
    title = main_component.find_element(by='xpath',value='./div/div/div/div/h1')
    location = main_component.find_element(by='xpath',value='./div/div/div/div/p[@class="location"]')
    price=main_component.find_element(by='xpath',value='./div/div/div/div/p[@class="price"]')
    posted_on = main_component.find_element(by='xpath',value='./div/div/div[@class="details--hero-header-sub"]/span[4]')
    views = main_component.find_element(by='xpath',value='./div/div/div[@class="details--hero-header-sub"]/span[5]')
    div_components = driver.find_elements(by='xpath', value='//*[@id="sectionOverview"]/ul/li/div')

    data_dict['title'] = title.text
    data_dict['location'] = location.text
    data_dict['price'] = price.text
    data_dict['posted_on'] = posted_on.text[11:]
    data_dict['views'] = views.text[:3]

    for component in div_components:
        # Get the h3 and h5 elements
        h3_element = component.find_element(by='xpath', value='./h3')
        h5_element = component.find_element(by='xpath', value='./h5')

        # Get the text from the h3 and h5 elements
        key = h3_element.text
        value = h5_element.text

        # Store the data in the dictionary with the title as key
        data_dict[key] = value
        
    Amenities = main_component.find_elements(by='xpath',value='./div/div[@id="sectionAmenities"]/ul')
    for i in Amenities:
        data_dict['amenity']=i.text.replace("\n",",")
    
    data_dict['url']=url
    # Print the dictionary
    data_list.append(data_dict)

end_time = time.time()
# import pandas as pd

# df = pd.DataFrame(data_dict)
# df_homedata.to_csv('details.csv')
print(len(data_list))
print("Hose Details Extration time:",end_time-start_time,"sec")
# import csv

# # Create a list to store all the data dictionaries
# all_data = []

# # Your existing code here...

#     # Add the current data_dict to the all_data list
# all_data.append(data_dict)

# # Create the CSV file and write the data
# with open('real_estate_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     # Define the field names for the CSV file
#     fieldnames = ['title', 'location', 'price', 'posted_on', 'views', 'LAND AREA', 'ROAD ACCESS', 'FACING', 'FLOOR', 'FURNISH STATUS', 'PARKING', 'BEDROOM', 'BATHROOM', 'BUILTUP AREA', 'BUILT YEAR', 'amenity']

#     # Create the CSV writer object
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     # Write the header row to the CSV file
#     writer.writeheader()

#     # Write each data dictionary as a row in the CSV file
#     for data_dict in all_data:
#         writer.writerow(data_dict)
import pandas as pd

df = pd.DataFrame(data_list)
df.to_csv('dataset_nepalhomes.csv',index=False)
df_input = pd.read_csv('dataset_nepalhomes.csv')
df_input.tail()
