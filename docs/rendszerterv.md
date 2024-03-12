# Rendszerterv

A rendszerterv célja az, hogy részletesen leírja és meghatározza egy adott projekt vagy rendszer teljes technológiai, infrastrukturális és működési kereteit.
Ennek a dokumentumnak a célja, hogy a projekt résztvevői számára egy átfogó útmutatást nyújtson a rendszer tervezéséhez, fejlesztéséhez és üzemeltetéséhez.

A rendszerterv összességében a projekt résztvevőinek egy átfogó irányt nyújt a projekt teljes életciklusán keresztül, segítve a hatékonyabb tervezést, fejlesztést és üzemeltetést.

## 1. A rendszer célja

A rendszer célja, hogy hatékonyan és átláthatóan kezelje és vizualizálja a feladatok áramlását, optimalizálja a munkafolyamatokat, és javítsa a csapat kommunikációját és együttműködését.
A Kanban rendszer lehetővé teszi a csapatok számára, hogy könnyen kövessék és kezeljék a munkafolyamatokat, vizuális táblák segítségével nyomon kövessék a feladatok előrehaladását, valamint gyorsan reagáljanak az esetleges változásokra és prioritásokra.
A Kanban célja, hogy maximalizálja a termelékenységet, minimalizálja a hibák számát és a feldolgozási időt, és biztosítsa a projektek gyors és hatékony kiszállítását.


## 2. Projektterv

### 2.1 Projektszerepkörök, felelőségek:
   * Scrum masters: 
      + Katona Bálint
   * Product owner:
      + Birinyi Gergő
   * Üzleti szereplő: 
      + Eszterházy Károly Katólikus Egyetem
     
### 2.2 Projektmunkások és felelőségek:
   * Frontend:
      + Sipos Valentin Dominik
      + Tóth Dorina Ildikó
      + Kovácspál Bálint István
   * Backend:
      + Sipos Valentin Dominik
      + Tóth Dorina Ildikó
      + Kovácspál Bálint István
   * Tesztelés:
      + Sipos Valentin Dominik
      + Tóth Dorina Ildikó
      + Kovácspál Bálint István
     
### 2.3 Ütemterv:

|Funkció                  | Feladat                                | Prioritás | Becslés (nap) | Aktuális becslés (nap) | Eltelt idő (nap) | Becsült idő (nap) |
|-------------------------|----------------------------------------|-----------|---------------|------------------------|------------------|---------------------|
|Követelmény specifikáció |Megírás                                 |         1 |             1 |                      1 |                1 |                   1 |             
|Funkcionális specifikáció|Megírás                                 |         1 |             1 |                      1 |                1 |                   1 |
|Rendszerterv             |Megírás                                 |         1 |             1 |                      1 |                1 |                   1 |
|Program                  |Képernyőtervek elkészítése              |         2 |             1 |                      1 |                1 |                   1 |
|Program                  |Prototípus elkészítése                  |         3 |             8 |                      8 |                8 |                   8 |
|Program                  |Alapfunkciók elkészítése                |         3 |             8 |                      8 |                8 |                   8 |
|Program                  |Tesztelés                               |         4 |             2 |                      2 |                2 |                   2 |

### 2.4 Mérföldkövek:
   * Projektterv kidolgozása
   * Kanban tábla bevezetése
   * Feladatok prioritizálása és megosztása
   * Fejlesztési sprintek
   * Tesztelések
   * Prototípus átadása

## 3. Üzleti folyamatok modellje

# Feladatok fogadása és prioritizálása
   + Az új feladatok és követelmények beérkezése a projekt csapatához.
   + Lépések:
      + Feladatok fogadása az ügyfél vagy a csapat tagjai részéről.
      + Feladatok és követelmények rögzítése a prioritások és határidők alapján.

# Feladatok kiosztása
   + A feladatok kiosztása a megfelelő csapat tagokhoz.
   + Lépések:
      + Feladatok kiosztása a megfelelő csapat tagokhoz, figyelembe véve a készségeket és a kapacitást.
      + Feladatok megosztása a Kanban táblán vagy más projektmenedzsment eszközön.

# Munkafolyamat végrehajtása és nyomon követése
   + A csapat tagjai végrehajtják a hozzájuk rendelt feladatokat és nyomon követik az előrehaladást.
   + Lépések:
      + Feladatok végrehajtása a tervezett határidők szerint.
      + Feladatok előrehaladásának naprakész nyomon követése a Kanban táblán.

# Feladatok átadása
   + A befejezett feladatok átadása a következő szakasz számára vagy az ügyfél részére.
   + Lépések:
      + Feladatok befejezése és ellenőrzése a minőség és a követelmények szerint.
      + Befejezett feladatok átadása a következő szakasznak vagy az ügyfél részére.

### 3.1 Üzleti szereplők

Az üzleti szereplők azon személyek vagy csoportok, akik érdekeltek vagy érintettek lehetnek a projektben, és akiknek szerepet vagy felelősséget kell vállalniuk a projekt sikerében.


### 3.2 Üzleti folyamatok

Egy specifikusan a programozói feladatokra szabható digitális Kanban alkalmazás használatával kerül megvalósításra.
Ez az alkalmazás lehetővé teszi a feladatok és projektek könnyű nyomon követését, átlátható és könnyen kezelhető folyamatok létrehozását.
Emellett egy nyelvi modell integrálása biztosítja a programozói feladatok specifikus automatizálását és támogatja a hatékony együttműködést és dokumentációt.

## 4. Követelmények

### Funkcionális követelmények

| ID | Megnevezés | Leírás |
| --- | --- | --- |
| K1 | Feladatok kezelése |  Feladatok létrehozása, szerkesztése és törlése. Prioritások hozzárendelése a feladatokhoz. |
| K2 | Kanban tábla kezelése | Vizuális Kanban tábla létrehozása és kezelése. |
| K3 | Felhasználói felület | Felhasználóbarát és könnyen kezelhető felhasználói felület biztosítása |
| K4 | Értesítések és kommunikáció | Kommunikációs lehetőségek biztosítása a csapattagok között. |


### Nemfunkcionális követelmények

| ID | Megnevezés | Leírás |
| --- | --- | --- |
| K5 | Teljesítmény maximalizálása | Gyors és hatékony működés biztosítása nagy adatmennyiségek esetén is. |
| K6 | Biztonság | Felhasználói adatok biztonságos tárolása és kezelése. |
| K7 | Skálázhatóság | Rugalmas skálázhatóság biztosítása a növekvő felhasználói igények kezelésére. |
| K8 | Használhatóság | Könnyen érthető és kezelhető felhasználói felület biztosítása.|

### Támogatott eszközök

Az alkalmazás elsősorban webkeresőn működik, esetleges fejlesztési lehetőség lehet asztali, vagy mobil eszközös alkalmazás fejlesztése.

## 5. Funkcionális terv

# Feladatok generáltatása az AI-al

A project főbb feladata a hatékony és rugalmas project generálás lenne, amelyet egy AI segítségével tennénk megvalósíthatóvá.
Az AI pár paraméter vagy utasítás után legenerálja a szükséges dokumentumokat, a feladatokat felosztja részfeladatokra, amit a felhasználó hozzá tud rendelni a projekten dolgozó programozókhoz.

# Feladatkezelés

Feladatok létrehozása: A felhasználóknak lehetőségük van új feladatok létrehozására a Kanban táblán.
Feladatok szerkesztése és törlése: A felhasználók módosíthatják és törölhetik a már létrehozott feladatokat szükség esetén.
Prioritások kezelése: A felhasználók képesek lesznek hozzárendelni prioritást a feladatokhoz annak fontossága alapján, és a prioritás alapján rendezhetik a feladatokat.

# Kanban tábla kezelése

Kanban tábla létrehozása: A felhasználók létrehozhatnak új Kanban táblákat a projektjeikhez, és testre szabhatják az oszlopokat és címkéket.
Feladatok áthelyezése a táblán: A felhasználók képesek lesznek áthelyezni a feladatokat a Kanban táblán különböző oszlopokba a munkafolyamatuk megfelelő állapotának megfelelően.

# Felhasználói felület

Felhasználóbarát felület: A projekt rendelkezik egy felhasználóbarát felülettel, amely lehetővé teszi a felhasználók számára a könnyű navigációt és a feladatok egyszerű kezelését.
Megjelenítési lehetőségek: A felhasználók kiválaszthatják a megjelenítés módját, például listanézet vagy Kanban nézet között.

# Értesítések és kommunikáció

Értesítések: A felhasználók automatikus értesítéseket kapnak a feladatok állapotváltozásairól, például új feladatok létrehozása vagy az állapot frissítése esetén.
Kommunikáció a csapatban: A felhasználók lehetőséget kapnak a csapat többi tagjával történő kommunikációra, például megjegyzések vagy chat funkciók segítségével.

### 5.1 Rendszerszereplők

# Ügyfél

Az ügyfél az, aki az adott projektért felelős vagy akinek az igényeit a projekt céljainak elérése érdekében szolgálni kell.
Az ügyfél szorosan együttműködik a projekt csapatával, és biztosítja, hogy a projekt teljesítse az üzleti követelményeket és elvárásokat.

# Projektmenedzser

A projektmenedzser felelős a projekt teljes körű irányításáért és koordinálásáért. 
Ő felügyeli a projektcsapatot, kezeli a feladatokat, időzíti a határidőket, és biztosítja, hogy a projekt az ütemtervnek megfelelően haladjon.

# Csapattagok

Csapattagok: A csapattagok olyan személyek, akik részt vesznek a projektben, és felelősek különböző feladatok végrehajtásáért.

### 5.2 Menühierarchiák

## Bejelentkezés

Regisztráció: Egy új fiók létrehozása a rendszerbe.

## Főmenü

Kanban : A projectek kanban táblái elérhetőek itt feladatokkal.
Dokumentumok: Az AI által generált dokumentumok elérhetőek itt.


## 6. Fizikai környezet

A fizikai környezet a projekt infrastruktúráját és hardveres környezetét írja le, amelyben a rendszer működni fog.
Ide tartoznak a szükséges hardveres erőforrások, a felhasznált szoftverkomponensek és külső rendszerek.

### Vásárolt softwarekomponensek és külső rendszerek

Az alkalmazás fejlesztése során felhasználtunk egy sor ingyenes szoftverkomponenst és nyílt forráskódú eszközt, mint például a Django webes keretrendszert Pythonban, valamint különböző Python csomagokat és modulokat.
Ezenkívül nem vásároltunk be semmilyen specifikus szoftverkomponenst vagy külső rendszert.

### Hardver topológia

A rendszer hardveres topológiája alapvetően egy szerver-kliens architektúrát követ.
A szerveroldali alkalmazás a Django keretrendszeren fut egy webkiszolgálón, míg a kliensoldali felhasználói felületet böngészőkben futtatjuk.

### Fizikai alrendszerek

A fizikai alrendszerek magukban foglalják a szerverhardvert, amelyen a Django alkalmazás fut, valamint a felhasználók által használt kliensoldali eszközöket, mint például asztali vagy hordozható számítógépek, okostelefonok és táblagépek.

### Fejlesztő eszközök

A fejlesztés során használtunk több eszközt és szoftvert is:

- **Fejlesztői környezet (IDE)**: A kód szerkesztéséhez és teszteléséhez a Visual Studio Code-ot használtuk, amely egy könnyűsúlyú, nyílt forráskódú fejlesztői környezet különféle programozási nyelvekhez.

- **Verziókezelő rendszer**: A projekt verziókezeléséhez teljes mértékben a Gitet alkalmaztuk, amely lehetővé teszi a változtatások nyomon követését és verziókezelését.

- **Egyéb eszközök**: Számos Python csomagot és modult használtunk a projekt fejlesztéséhez, beleértve a Django keretrendszert is.

# Feladat követő rendszer

A projekt folyamatosan követi és dokumentálja a még hátralévő feladatokat és teendőket a fejlesztés során.
Ennek célja az átláthatóság és a hatékony projektmenedzsment biztosítása.

## 7. Architekturális terv

Az alkalmazás webalkalmazásként kerül megvalósításra, amely Django keretrendszert használ a backend fejlesztéséhez és HTML/CSS-t a frontend fejlesztéséhez.
A webalkalmazás felhőalapú környezetben fut majd, ami lehetővé teszi a könnyű skálázhatóságot és elérhetőséget.

### Adatbázis rendszer

Az alkalmazás adatbázisrendszere egy MySQL relációs adatbázisra épül.
Az adatbázis tartalmazza a felhasználók, projektek, feladatok és azok állapotainak tárolásához szükséges táblákat.
A következő táblák szerepelnek az adatbázisban:
Az adatbázisrendszert gondosan tervezték és optimalizálták a hatékonyság és a megbízhatóság érdekében, hogy biztosítsák a rendszer stabil működését és gyors teljesítményét.

### A program elérése, kezelése

A program elérése és kezelése egy webes felhasználói felületen keresztül történik, amelyet a felhasználók bármely modern webböngészőn keresztül elérhetnek.
A felhasználóknak csak egy internetkapcsolat és egy támogatott böngészőre van szükségük a program használatához.
A felhasználók képesek lesznek bejelentkezni a rendszerbe egyedi felhasználói azonosítóval és jelszóval, majd hozzáférhetnek a projektekhez és feladatokhoz, valamint kezelhetik azokat a rendelkezésre álló funkciók segítségével.


## 8. Adatbázis terv

Az adatbázis felépítése a következő

1. Felhasználók tábla: Tartalmazza a felhasználók adatait, beleértve a felhasználónevet, jelszót, e-mail címet stb.

2. Projektek tábla: Ebben a táblában tárolódnak a létrehozott projektek adatai, például a projekt neve, leírása, stb.

3. Feladatok tábla: Tartalmazza a projektekhez rendelt feladatok részleteit, beleértve a feladat nevét, leírását, állapotát stb.

## 9. Implementációs terv

Az implementációs terv részletesen leírja, hogyan valósítjuk meg a rendszer architekturális tervét és funkcionalitásait a kódban. Az implementáció során a következő lépéseket fogjuk követni:

1. Backend fejlesztés: Először a Django keretrendszer segítségével elkészítjük a backend részt, beleértve az adatbázis modellek létrehozását, az üzleti logika implementálását és az API-k kidolgozását a frontenddel való kommunikációhoz.

2. Frontend fejlesztés: Ezután a HTML és CSS segítségével elkészítjük a felhasználói felületet. A frontend fejlesztés során figyelembe vesszük a tervezett dizájnt és az eszközbarát megjelenést.

3. Integráció: A backend és a frontend elkészült részeit összeillesztjük és integráljuk, hogy a rendszer teljes egésze működjön. Teszteljük az egyes funkciók működését és az adatok megfelelő átvitelét.

4. Tesztelés és hibajavítás: Végül teszteljük a rendszert, hogy megbizonyosodjunk arról, hogy megfelel az elvárásoknak és a funkcionalitásnak. Javítjuk és optimalizáljuk a kódot, ha szükséges, és biztosítjuk, hogy a rendszer stabilan és hatékonyan működjön.

Az implementációs terv részletesen meghatározza a fejlesztési folyamat lépéseit és menetét, hogy biztosítsuk a sikeres projekt végrehajtást és kiszállítást.

## 10. Telepítési terv

A telepítési terv leírja, hogyan kerül a rendszer telepítésre és konfigurálásra a végfelhasználók környezetében. A telepítési folyamat a következő lépésekből áll:

1. Szükséges szoftverek és eszközök előkészítése: A rendszer telepítéséhez szükséges szoftverek és eszközök előzetes letöltése és telepítése a végfelhasználó környezetében.

2. Rendszerkövetelmények ellenőrzése: Ellenőrizni kell, hogy a végfelhasználó rendszere megfelel-e a rendszer minimális hardver- és szoftverkövetelményeinek.

3. Telepítési folyamat végrehajtása: A rendszer telepítési folyamatának végrehajtása, beleértve a szükséges fájlok másolását, konfigurációs beállítások végrehajtását és a rendszer indulását.

4. Konfiguráció és testelés: A telepítés után a rendszer konfigurációjának befejezése és a rendszer alapos tesztelése, hogy megbizonyosodjunk arról, hogy minden megfelelően működik.

5. Felhasználók képzése: Szükség esetén a felhasználók képzése és oktatása a rendszer használatára, beleértve a funkciók és a felhasználói felület áttekintését.

A telepítési terv részletesen meghatározza a telepítési folyamat lépéseit és teendőit annak érdekében, hogy a rendszer sikeresen telepítésre kerüljön a végfelhasználó környezetében.


## 11. Karbantartási terv

A karbantartási terv célja a rendszer hosszú távú fenntartása és optimalizálása, hogy biztosítsa a folyamatos működést és teljesítményt. A karbantartási tevékenységek magukban foglalják:

1. Rendszerfrissítések és javítások: Rendszeresen ellenőrizni és frissíteni kell a rendszer összetevőit, beleértve az operációs rendszert, alkalmazásokat és függőségeket, valamint javítani kell a fennálló hibákat és sebezhetőségeket.

2. Teljesítményoptimalizálás: Rendszeres teljesítményértékelések és optimalizációs tevékenységek végrehajtása annak érdekében, hogy biztosítsuk a rendszer hatékony működését és megfelelő reakcióidőket.

3. Biztonsági intézkedések: Rendszeres biztonsági ellenőrzések és intézkedések végrehajtása annak érdekében, hogy megelőzzük a biztonsági incidenseket és védelmet nyújtsunk a kibertámadások ellen.

4. Felhasználói támogatás és képzés: Folyamatos felhasználói támogatás biztosítása, beleértve a rendszerrel kapcsolatos kérdések és problémák megoldását, valamint a felhasználók oktatását és képzését a rendszer hatékony használatára.

5. Vésztervek és mentési folyamatok: Részletes vésztervek készítése és rendszeres mentési folyamatok végrehajtása annak érdekében, hogy biztosítsuk az adatok és a rendszer integritását, és gyors helyreállítást biztosítsunk bármilyen katasztrófa esetén.

A karbantartási terv részletesen meghatározza ezeket a tevékenységeket és felelősöket rendszeres időközönként történő végrehajtásukhoz annak érdekében, hogy a rendszer hosszú távon hatékonyan és megbízhatóan működjön.

Figyelembe kell venni a felhasználó által jött visszajelzést is a programmal kapcsolatban.
Ha hibát talált, mielőbb orvosolni kell, lehet az:
*  Működéssel kapcsolatos
*  Kinézet, dizájnnal kapcsolatos