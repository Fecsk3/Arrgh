# Követelmény specifikáció

---

## 1. Áttekintés

A Kanban alkalmazás egy digitális eszköz, amely lehetővé teszi a feladatok vizuális kezelését és nyomon követését oszlopok és kártyák segítségével. 
A célja az átláthatóság és az együttműködés növelése a projektek kezelése során.

A Kanban rendszer alapja egy tábla, amely oszlopokban szervezi a feladatokat. 
Minden oszlop egy adott munkafolyamat állapotát reprezentálja, "Teendő", "Folyamatban", "Ellenőrzés", "Kész", stb. 
A kártyák pedig az egyes feladatok vagy teendők reprezentációi, amelyeket a megfelelő oszlopok között mozgatva követhető és kezelhető a projektek előrehaladása.

Az alkalmazás lehetővé teszi a felhasználók számára, hogy könnyen létrehozzanak projekteket, hozzárendeljenek kártyákat, és ezeket mozgathassák az állapotoknak megfelelő oszlopok között. 
A nyelvi modell segítségével az alkalmazás javaslatokat tehet a feladatok kiosztásához, figyelembe véve az egyes felhasználók képességeit és elérhetőségét.

A Kanban alkalmazás használata átláthatóságot és strukturált munkavégzést biztosít, javítva ezzel a produktivitást és az együttműködést a csapatok között.

## 2. A jelenlegi helyzet leírása

Bár léteznek már Kanban alapú eszközök, a cél egy olyan alkalmazás létrehozása, amelybe beépítésre kerül egy nyelvi modell, és lehetőség van a projektek dokumentációinak felvitelére és megosztására az alkalmazás felületén.

## 3. Vágyálomrendszer

A projekt célja egy digitális Kanban alkalmazás létrehozása, mely lehetővé teszi a felhasználók számára, hogy feladataikat vizuálisan kezeljék és nyomon kövessék oszlopok és kártyák segítségével. Az alkalmazásnak átláthatónak és együttműködést segítőnek kell lennie, lehetővé téve a felhasználók számára, hogy hatékonyan kezeljék munkafolyamataikat. Emellett egy nyelvi modell automatizálja bizonyos munkafolyamatokat, segít a dokumentáció megírásában és biztosít helyet a dokumentumok tárolására az oldalon.

### Fő Funkciók

1. **Kártyák kezelése:** A felhasználók lehetőséget kapnak kártyák létrehozására, melyek reprezentálják az egyes feladatokat vagy teendőket. Ezek a kártyák vizuálisan képviselik a feladatokat és könnyen mozgathatók az oszlopok között.

2. **Oszlopok kezelése:** Az alkalmazás lehetővé teszi oszlopok létrehozását és kezelését, amelyek reprezentálják a különböző állapotokat vagy fázisokat a munkafolyamatban. A kártyák mozgathatók ezek között az oszlopok között, hogy tükrözzék az adott feladat aktuális állapotát.

3. **Projektek kezelése:** A felhasználók képesek projektek létrehozására, amelyekben több feladatot csoportosíthatnak. Ez segíti az átláthatóságot és a projekt alapú munkavégzést.

4. **Feladatok kezelése:** Az alkalmazás lehetőséget biztosít a feladatok létrehozására, szerkesztésére és törlésére a projektekben. Ez segíti a felhasználókat abban, hogy könnyen áttekinthetően kezeljék és frissítsék a feladataikat.

5. **Együttműködés támogatása:** Az alkalmazásnak az a célja, hogy elősegítse az együttműködést a csapatok között. Ennek érdekében lehetőséget biztosít a felhasználók számára arra, hogy lássák és kövessék egymás munkáját, valamint könnyen megoszthassák információikat és dokumentációikat.

6. **Automatizált munkafolyamatok:** A nyelvi modell segítségével bizonyos munkafolyamatok automatizálhatók, ami javítja a hatékonyságot és csökkenti a manuális munkát.

7. **Dokumentáció kezelése:** Az alkalmazás lehetővé teszi a dokumentáció megírását és tárolását az oldalon, így könnyen hozzáférhetővé teszi az összes csapattag számára, ami segíti a projektek átláthatóságát és a tudás megosztását.

## 4. Jelenlegi üzleti folyamatok modellje

A jelenlegi üzleti folyamatok részben digitális platformokon zajlanak, azonban ezek nem optimálisan integráltak, és nem biztosítanak teljes körű nyomon követési és kezelési lehetőségeket. Az elérhető digitális eszközök fragmentáltak, és nem képesek teljes mértékben támogatni az együttműködést és az átláthatóságot a feladatok és projektek kezelésében.

## 5. Igényelt üzleti folyamatok modellje

Egy specifikusan a programozói feladatokra szabható digitális Kanban alkalmazás használatával kerül megvalósításra. Ez az alkalmazás lehetővé teszi a feladatok és projektek könnyű nyomon követését, átlátható és könnyen kezelhető folyamatok létrehozását. Emellett egy nyelvi modell integrálása biztosítja a programozói feladatok specifikus automatizálását és támogatja a hatékony együttműködést és dokumentációt.

## 6. Követelménylista

| Id | Modul | Név | Leírás |
| :---: | --- | --- | --- |
| K1 | Kártyák és Oszlopok Kezelése | Kártyák létrehozása, mozgatása oszlopok között | Lehetőség a feladatokat vagy projekteket reprezentáló kártyák létrehozására, valamint azok mozgatására az egyes oszlopok között a folyamat során. |
| K2 | Projektek és Feladatok Kezelése | Projektek és feladatok létrehozása, szerkesztése, törlése | Lehetőség projektek és feladatok létrehozására, szerkesztésére és törlésére. |
| K3 | Állapotkövetés | Kártyák állapotának nyomon követése | Felhasználók nyomon követhetik a kártyák állapotát és azokat az oszlopokat, amelyekben éppen tartózkodnak. |
| K4 | Dokumentáció Generálása | Automatikus dokumentáció generálás | Az alkalmazás integrál egy nyelvi modellt, amely automatikusan generál dokumentációkat a projektekhez vagy feladatokhoz. |
| K5 | Feladatok Kiosztása | Feladatok kiosztása felhasználók között | Felhasználók könnyen kioszthatnak feladatokat egymásnak az alkalmazáson keresztül. |

## 7. Fogalomtár

Az alkalmazásban használt kulcsfogalmak és kifejezések definíciói:

- **Kanban:** Vizuális munkaállapot-kezelési technika, mely oszlopok és kártyák segítségével jelzi a feladatok állapotát.
- **Oszlop:** A Kanban táblázat egyes részei, amelyek az egyes munkaállapotokat reprezentálják.
- **Kártya:** Egy feladat vagy projekt reprezentációja a Kanban táblán.
- **Projekt:** Egy meghatározott cél vagy tevékenység, amelynek megvalósítására szervezett módon kerül sor.
- **Feladat:** Egy konkrét tevékenység vagy teendő, amely egy projekt része lehet.
- **Állapotkövetés:** A feladatok vagy projektek aktuális állapotának követése és frissítése az alkalmazásban.
- **Dokumentáció:** Az írásos vagy digitális információk gyűjteménye, amelyek segítik a munkavégzést és a tudás megosztását.
- **Automatizáció:** Az alkalmazás által végrehajtott folyamatok automatikus végrehajtása, minimalizálva a manuális beavatkozást.
- **Együttműködés:** A csapatok közötti hatékony kommunikáció és munkamegosztás elősegítése az alkalmazás segítségével.
- **Nyelvi modell:** Egy mesterséges intelligencia alapú rendszer, amely a természetes nyelvet használja az automatizációhoz és a dokumentáció generálásához.
- **Kiosztás:** Feladatok vagy projektek megosztása és delegálása a csapat tagjai között az alkalmazásban.
