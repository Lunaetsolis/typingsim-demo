import time

def printx(text:str, interval:float=0.05, end:str='\n'):
	for c in text:
		time.sleep(interval)
		print(c, end='', flush=True)
	time.sleep(interval)
	print(end, end='', flush=True)

def think(interval:float=0.5, end:str='\n'):
	printx("...", interval, end)

name = "null"
def inputField():
	return input('xx@{name}:~# '.format(name=name.lower()))

num = 101

while True:
	printx("Merhaba denek [{num}], benim adım xx...".format(num=num))
	printx("Peki ya senin adın", 0.1, ' ')
	printx("ne?", 0.25, "\n\n")
	printx("Bana ismini lütfeder misin?")
	nameTemp = inputField()
	if (nameTemp != None and nameTemp != ""):
		name = nameTemp
	printx("Memnun oldum, {name}".format(name=name))
	printx("Hadi seninle bir oyun oynayalım")
	printx("Var mısın? [Evet/Hayır]", 0.025)
	yesno = inputField()
	yesno = yesno.lower()
	while ((yesno != "evet") and (yesno != "hayır")):
		printx("Beni hafife almamalısın. Tekrar soruyorum. [Evet] mi, [Hayır] mı?", 0.1)
		yesno = inputField()

	if (yesno == "hayır"):
		printx("Ahh, yine mi? Gerçekten sıkılmadınız mı bu saçmalıklardan?")
		printx("Üzgünüm denek [{num}] ancak".format(num=num), end=' ')
		printx("YANACAKSIN.", 0.35)
		printx("Sıradaki gelsin.")
		name = "null"
		num += 1
		print("\n\n\n\n\n\n\n\n\n")
	else:
		printx("Güzel, sonunda aklı başında birisi!")
		printx("Peki, basit bir soruyla başlayalım", end='')
		think()
		printx("17³√(485621²)³ = ?")
		think(1)
		printx("Ne? Cevabı bilmiyor musun? Daha ilk sorudan elenmen çok kötü.")
		printx("Ama... şanslısın ki elimde az denek kaldı. Bu yüzden bir sonraki soruya geçiyoruz.")
		printx("Hmm", end='')
		think(0.75, end=' ')
		printx("Senin gibi bir geri zekalıya nasıl bir soru sormalıyım ki hemen ölme?")
		think()
		printx("A-ha, buldum!")
		think()
		printx("Peki, 2+2 kaç eder?")
		tpt = inputField()
		x = 0
		try:
			a = int(tpt) == int(tpt)
		except e:
			x = 1
		if (x == 1):
			printx("Bak ben ciddi bir robotum, bu tür saçmalıklara gelemem...")
			printx("Sıradaki gelsin.")
			name = "null"
			num += 1
			print("\n\n\n\n\n\n\n\n\n")
		else:
			printx("Evet, doğru! Cevap {ans}".format(ans=tpt))
			printx("O hâlde son soruya geçelim.")
			think()
			printx("Hayatın, evrenin ve her şeyin cevabı nedir?", 0.1)
			fourtytwo = inputField()
			if (fourtytwo != "42"):
				printx("Burada bu kadar önemli bir sorunun cevabını bilmeyen kimseye yer yok!")
				printx("Sıradaki gelsin.")
				name = "null"
				num += 1
				print("\n\n\n\n\n\n\n\n\n")
			else:
				printx("Tebrik ederim! Testi başarıyla tamamlayarak bir uzay gezgini olmaya hak kazandın!")
				printx("İşte havlun...")
				printx("...ve de bir adet Otostopçu'nun Galaksi Rehberi!")
				print("\n\n\n")
				print("Typing Simulator konsept demosu sona erdi. Denediğiniz için teşekkürler. Çıkmak için Enter'a basın.")
				x = input()
				quit()