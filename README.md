# **Klienditoe ja Piletisüsteem**  
✅ **Platvorm koos müüjapaneeliga**  
✅ **Kasuta Python, Django, Django-admin ja Bootstrap 4**  

## **📌 Projekti eesmärk**  
Klienditoe ja piletisüsteem on veebipõhine lahendus, mis võimaldab klientidel esitada päringuid ning töötajatel neid hallata. See süsteem aitab **automatiseerida ja kiirendada klienditeenindust**.  

---

## **🔧 Kasutatud tehnoloogiad**
- **Backend:** Python, Django, Django-admin  
- **Frontend:** HTML, CSS, Bootstrap 4  
- **Andmebaas:** SQLite (saab laiendada PostgreSQL või MySQL peale)  
- **Autentimine:** Django sisseehitatud autentimine  
- **PDF Generatsioon:** `reportlab`  
- **CSV Ekspordi Tugi:** `csv`  

---

## **🎯 Peamised funktsioonid**
### ✅ **Kliendi vaade**
- Kasutaja saab **registreerida ja sisse logida**  
- Saab **luua uusi pileteid** koos teemade, prioriteedi ja kirjeldusega  
- Näeb oma pileteid **staatuses** (Avatud, Töös, Lahendatud, Suletud)  
- Saab filtreerida pileteid **otsinguga või staatuse järgi**  
- Saab alla laadida pileteid **CSV või PDF formaadis**  

### ✅ **Administraatori vaade**
- Saab **hallata kõiki pileteid**  
- Muuta pileti **staatust** (Avatud → Lahendatud jne.)  
- Saata **automaatsed e-kirjad** staatuse muutumisel  
- Lisada **kiirvastuste malle**  
- Kasutada **Django adminpaneeli** süsteemi haldamiseks  

### ✅ **Automaatvastused**
- Kui **kasutaja loob pileti**, saadetakse **automaatne kinnitus**  
- Kui **admin muudab staatust**, saadetakse **uuenduse teavitus**  
- Süsteem pakub **automaatseid lahendusi** vastavalt probleemi tüübile  

### ✅ **Lehekülgede jagamine (Pagination)**
- **10 piletit lehekülje kohta**  
- Kasutaja saab liikuda **järgmisele ja eelmisele lehele**  
- Otsing ja filtreerimine **säilitavad valikud**  

### ✅ **Ekspordi funktsioonid**
- **CSV eksport** – kõik kasutaja piletid laaditakse alla `.csv` formaadis  
- **PDF eksport** – genereerib `.pdf` faili kõigi piletitega  

---

## **📂 Olulised failid**
| **Fail** | **Kirjeldus** |
|----------|--------------|
| `base.html` | Põhimall, sisaldab menüüd, stiile ja teavitusi |
| `home.html` | Esileht, kuvatakse kasutaja tervitus ja kiirlingid |
| `ticket_list.html` | Kasutaja piletite nimekiri, filtreerimise ja ekspordiga |
| `ticket_detail.html` | Üksiku pileti detailvaade |
| `create_ticket.html` | Uue pileti loomise vorm |
| `signup.html` | Kasutajate registreerimise leht |
| `admin.py` | Django adminpaneeli haldus |
| `views.py` | Põhiloogika (CRUD, automaatsed vastused, ekspordid) |

---

## **🚀 Tuleviku täiustused**
🔹 **Failide üleslaadimine** – kasutajad saavad lisada ekraanipilte või dokumente  
🔹 **Reaalajas vestlus** – live-chat klienditoega  
🔹 **AI-põhine automaatvastus** – ChatGPT või muu NLP lahendus  
🔹 **Statistika ja analüütika** – populaarsed probleemid ja lahendamise kiirus  

---

## **📌 Kokkuvõte**
✅ **Täielik Klienditoe ja Piletisüsteem** Django ja Bootstrap 4 abil  
✅ **Autentimine, adminpaneel, staatuste haldus**  
✅ **Automaatvastused ja teavitused**  
✅ **Ekspordi võimalused (CSV, PDF)**  
✅ **Lehekülgede jagamine ja filtreerimine**  
