import csv
import json
import urllib.request

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR5IjxGoHqI63-Us3dGTytWTsQwXINoAJwl2FcwM30ZODBMV1-Fl75_UidNrtyEeABh5qcqoSgumJ2Y/pub?output=csv"

try:
    print("กำลังเชื่อมต่อ Google Sheet...")
    req = urllib.request.urlopen(CSV_URL)
    lines = [l.decode('utf-8') for l in req.readlines()]
    reader = csv.DictReader(lines)
    data = [row for row in reader]
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"สำเร็จ! บันทึกข้อมูล {len(data)} แถวลง data.json เรียบร้อย")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump([], f)
