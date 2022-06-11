import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Kohwan17",
  database="logistik"
)


def insert_data(db):
  id = input("Masukan id : ")
  tanggal = input("Masukan tanggal : ")
  jenisPengiriman = input("Masukan jenis pengiriman : ")
  jenisBarang = input("Masukan jenis barang : ")
  asalBarang = input("Masukan asal : ")
  tujuanBarang = input("Masukan tujuan : ")
  status = input("Masukan status : ")
  val = (id, tanggal, jenisPengiriman, jenisBarang, asalBarang, tujuanBarang, status)
  cursor = db.cursor()
  sql = "INSERT INTO dataLogistik (id, tanggal, jenisPengiriman, jenisBarang, asalBarang, tujuanBarang, status) VALUES (%s, %s, %s,%s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))

def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci : ")
  sql = "SELECT * FROM dataLogistik WHERE id LIKE %s"
  val = ("%{}%".format(keyword))
  cursor.execute(sql, (val,))
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Search Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu > ")
  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("ID salah!")


if __name__ == "__main__":
    while(True):
        show_menu(db)