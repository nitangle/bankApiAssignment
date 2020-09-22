import re


import requests
import xlrd
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
# import shutil

from django.core.management.base import BaseCommand

from api.models import BankDetail

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        
        URL = "https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009"
        page = requests.get(URL).text
        soup = BeautifulSoup(page,'html.parser')
        file_table = soup.table.table
        table_rows = file_table.find_all('tr')[1:] 
        for row in table_rows:
            url_data = row.a['href']
            filePath = re.search(r'.*/(\w*.xlsx)',url_data).groups()[0]
            dst = filePath
            print("dst is {}",dst)
            urlretrieve(url_data, dst)
            with xlrd.open_workbook(dst,'wb') as f:
                sheet =f.sheet_by_index(0)
                # for checking given just 2 rows
                for row in range(0,3):
                    ifsc_code = sheet.cell_value(row,1)
                    bank_name = sheet.cell_value(row,0)
                    branch_name = sheet.cell_value(row,2)
                    address = sheet.cell_value(row,3)
                    BankDetail.objects.update_or_create(ifsc_code=ifsc_code,bank_name=bank_name,branch_name=branch_name,address=address)
                    

        self.stdout.write("okay we have the data now!! ")