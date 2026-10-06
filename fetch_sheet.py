import csv, json, urllib.request
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR5IjxGoHqI63-Us3dGTytWTsQwXINoAJwl2FcwM30ZODBMV1-Fl75_UidNrtyEeABh5qcqoSgumJ2Y/pub?gid=110366739&single=true&output=csv"
def main():
    res = urllib.request.urlopen(CSV_URL)
    lines = [l.decode('utf-8') for l in res.readlines()]
    data = [row for row in csv.DictReader(lines)]
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Success: {len(data)} rows")
if __name__ == '__main__':
    main()
