# Funkcionális specifikáció

---

## 1. Jelenlegi helyzet leírása

A csapatnak nincs megfelelő online eszköze a feladatok nyomon követésére és kezelésére.
Az üzleti folyamatok jelenlegi kezelése kaotikus és nem hatékony.
Nehézségek merülnek fel a csapatmunkában a hiányos kommunikáció miatt.
A feladatokat nem könnyű követni és szervezni.
A csapat nem rendelkezik egységes rendszerrel a munkafolyamatok koordinálására.
Ez a helyzet akadályozza a hatékony munkavégzést és a feladatok átlátható kezelését.

## 2. Vágyálomrendszer leírása

Szeretnénk egy olyan Kanban alkalmazást, ami segít a feladatok és projektek szervezésében.
Célunk, hogy könnyebb legyen a csapatmunka és az együttműködés.
Fontos számunkra, hogy átlátható legyen a munkafolyamat.
Az automatizált döntéstámogatás és dokumentáció generálás is része a terveinknek.
A nyelvi modell integrálása segítené a hatékonyabb kommunikációt és feladatmegosztást.
A végső cél egy olyan rendszer létrehozása, ami megkönnyíti a feladatok kezelését és a munkafolyamatokat.

## 3. Jelenlegi üzleti folyamatok modellje

Jelenleg a vállalat folyamatai manuálisak és körülményesek.
A feladatok és projektek kezelése sok esetben papíralapú vagy egyszerű digitális eszközökön keresztül zajlik.
Ez a módszer nem teszi könnyűvé a munkafolyamatok átláthatóságát.
A manuális rendszerek nehezítik az együttműködést a csapat tagjai között.
Az efféle megoldások nem hatékonyak a feladatok koordinálásában és nyomon követésében.
Szükség van egy modernebb, digitális eszközre, ami segítene az üzleti folyamatok hatékonyabb kezelésében és a csapatmunka javításában.

## 4. Igényelt üzleti folyamatok modellje

A vállalat igényelt üzleti folyamatai a Kanban módszerre épülnek.
Ez a módszer lehetővé teszi a feladatok és projektek vizuális kezelését és nyomon követését.
A Kanban alkalmazás könnyű együttműködést biztosít a csapat tagjai között.
A vizuális megjelenítés segíti az átláthatóságot és a feladatok kezelését.
A csapat hatékonyabban tud együtt dolgozni a Kanban rendszer segítségével.
A Kanban alapú modell lehetővé teszi a folyamatok átlátható kezelését és a munka hatékonyabb szervezését.

## 5. Követelménylista

| Id | Modul | Név | Leírás |
| :---: | --- | --- | --- |
| K1 | Kártyák és oszlopok | Feladatok reprezentálása kártyákon és azok mozgatása oszlopok között | Lehetőség kártyák létrehozására, szerkesztésére és mozgatására az oszlopok között |
| K2 | Projektek és feladatok kezelése | Projektek és feladatok létrehozása, szerkesztése és törlése | Funkciók projektek és feladatok kezelésére, valamint ezek hozzárendelésére a megfelelő kártyákhoz |
| K3 | Állapotkövetés | Kártyák állapotának nyomon követése | Lehetőség nyomon követni a kártyák állapotát és azokat az oszlopokat, amelyekben éppen tartózkodnak |
| K4 | Dokumentáció generálása | Automatikus dokumentáció generálása projektekhez vagy feladatokhoz | Integráció egy nyelvi modelllel a dokumentáció automatikus generálásához |
| K5 | Feladatok kiosztása | Feladatok kiosztása egymásnak a csapat tagjai között | Lehetőség feladatok kiosztására, javaslatokat adva a nyelvi modell alapján |

## 6. Használati esetek

A felhasználók létrehoznak, szerkesztenek és mozgatnak kártyákat az oszlopok között.
Projekteket és feladatokat készítenek, módosítanak és törölnek.
Követik a projektek és feladatok állapotát.
Dokumentációt generálnak a nyelvi modell segítségével.
Feladatokat osztanak ki egymásnak a csapat tagjai között.

## 7. Megfeleltetés, hogyan fedik le a használati eseteket a követelményeket

A használati esetek segítségével a felhasználók könnyen kezelhetik a feladatokat és projekteket.
Az állapotok nyomon követése is része ennek a folyamatnak.
Emellett a felhasználók dokumentációt tudnak generálni a rendszeren keresztül.
Ezen kívül a feladatokat is könnyen tudják kiosztani egymásnak.
A rendszer lehetővé teszi a feladatok és projektek hatékony kezelését és koordinálását.
Végül, a csapat tagjai közötti kommunikáció is könnyebbé válik ezen eszköz segítségével.

## 8. Képernyőtervek

| Kép | Leírás |
| :-----------: | :-----------: |
| ![regisztracio.png](https://github.com/Fecsk3/Arrgh/blob/main/docs/img/regisztracio.png) | A regisztrációs oldal tervezete. Ez az a rész, ahol az oldalra látogatók pár adat megadásával máris az oldal felhasználói közé tartozhat. |
| ![bejelentkezes.png](https://github.com/Fecsk3/Arrgh/blob/main/docs/img/bejelentkezes.png) | A bejelentkező oldal tervezete. Ez az a rész, ahol a már előzetesen regisztrált felhasználók, pár adat megadásával bármikor beléphetnek az oldalra. |
| ![fooldal.png](https://github.com/Fecsk3/Arrgh/blob/main/docs/img/fooldal.png) | A főoldal tervezete. Szükséges egy profillal rendelkezni, ha erre az oldalra térnek az emberek. |
| ![kanban.png](https://github.com/Fecsk3/Arrgh/blob/main/docs/img/kanban.png) | A kanban tervezete. Szükséges egy profillal rendelkezni, ha erre az oldalra térnek az emberek. {DORINA} |

## 9. Forgatókönyvek

A felhasználók bejelentkeznek az alkalmazásba.
Létrehoznak vagy szerkesztenek kártyákat, projekteket vagy feladatokat.
Követik azok állapotát a folyamat során.
Amennyiben szükséges, generálnak dokumentációt az alkalmazás segítségével.
Szintén az alkalmazáson keresztül osztanak ki feladatokat egymásnak.
Mindezeken keresztül hatékonyabban tudnak együtt dolgozni és kommunikálni a csapat tagjai.

## 10. Funkció - követelmény megfeleltetése

| Id | Követelmény | Funkció |
| :---: | --- | --- |
| K1 | Kártyák és oszlopok | Kártyák létrehozása, szerkesztése és mozgatása |
| K2 | Projektek és feladatok kezelése | Projektek és feladatok létrehozása, szerkesztése és törlése |
| K3 | Állapotkövetés | Kártyák állapotának nyomon követése |
| K4 | Dokumentáció generálása | Automatikus dokumentáció generálása nyelvi modellel |
| K5 | Feladatok kiosztása | Feladatok kiosztása javaslatok alapján |

## 11 Fogalomszótár

1. **Kanban**: Egy japán eredetű, vizuális munkafolyamat-kezelési módszer, amely során a feladatokat kártyák formájában ábrázolják, és azokat oszlopok között mozgatják a folyamat során.

2. **Kártya**: Egy digitális vagy fizikai kártya, amelyen egy feladat vagy projekt információi találhatók. Általában a Kanban rendszerekben használják a feladatok vizuális kezelésére.

3. **Állapot**: Egy feladat vagy projekt aktuális helyzete vagy státusza a munkafolyamat során. Például: "Folyamatban", "Kész", stb.

4. **Dokumentáció**: Az írásos vagy digitális információk gyűjteménye, amelyek részletesen leírják egy projekt vagy feladat részleteit, folyamatait és céljait.

5. **Feladatkiosztás**: A feladatok vagy projektek kiosztása a csapat tagjai között, hogy hatékonyan lehessenek végrehajtva és befejezve.

6. **Automatizált döntéstámogatás**: Olyan technológiai megoldások alkalmazása, amelyek segítik a felhasználókat a döntéshozatalban a rendszer által gyűjtött adatok és elemzések alapján.

7. **ORM (Object-Relational Mapping)**: Egy programozási technika, amely lehetővé teszi az objektum-orientált programozási nyelvekben írt objektumok és az adatbázisok közötti átjárhatóságot.

8. **URL routing**: Az internetes kérések (URL-ek) irányítása egy webalkalmazáson belül a megfelelő végpontokhoz vagy funkciókhoz.

9. **Beépített funkciók**: Olyan előre elkészített funkciók, amelyeket egy keretrendszer vagy szoftver tartalmaz az egyszerűsített fejlesztés érdekében.
