print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis sinu nimi on?")
print(nimi,"oi kui ilus nimi!")
vastus=input(nimi +  "Kas leian Sinu keha indeksi? 0-ei, 1-jah =>")
if vastus== "1" :
    pikkus=int(input("Kui pikk sa oled?"))
    mass=float(input("Mis on teie kaal?"))
    indeks = mass/(0.01 * pikkus)**2 #ошибка с float и str
    print(indeks)
    indeks = round(indeks,1)
    vastus=print(nimi , "! Sinu keha indeks on:" , indeks)
