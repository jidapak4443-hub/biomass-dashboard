import csv
import json
import urllib.request

# ใส่ลิงก์ Public CSV จาก Google Sheet ของคุณตรงนี้
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR5IjxGoHqI63-Us3dGTytWTsQwXINoAJwl2FcwM30ZODBMV1-Fl75_UidNrtyEeABh5qcqoSgumJ2Y/pub?gid=110366739&single=true&output=csv"

def convert_sheet_to_json():
    print("กำลังดึงข้อมูลจาก Google Sheet...")
    response = urllib.request.urlopen(CSV_URL)
    lines = [line.decode('utf-8') for line in response.readlines()]
    
    reader = csv.DictReader(lines)
    data_list = [row for row in reader]
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=2)
        
    print(f"แปลงข้อมูลสำเร็จทั้งหมด {len(data_list)} แถว ลงใน data.json แล้ว")

if __name__ == "__main__":
    convert_sheet_to_json()
