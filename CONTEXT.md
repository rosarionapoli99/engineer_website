# CONTEXT — Sito Studio Taranto-Vancheri

## Panoramica generale

**Nome studio:** Studio di Ingegneria e Architettura "Taranto - Vancheri"  
**Sede:** Via Uberto Bonino, 8/scala G, 98124 Messina ME  
**Telefono:** 090 714435  
**Email contatti:** info@example.com _(da aggiornare con email reale)_  
**Email ricezione form:** rosarionapoli99@gmail.com _(in `send_mail.php`)_  
**Fondazione:** 1985 — 40+ anni di attività  
**Certificazione:** ISO 9001:2015 — n. STUD4608Q2501 — EUCI European Certification Institute  
**Social:** Facebook, LinkedIn (Ing. Luciano Taranto)

---

## Stack tecnologico

- HTML5 statico (nessun framework frontend)
- Bootstrap 5 (CSS custom: `css/bootstrap.min.css`, `css/style.css`)
- jQuery 3.4.1
- WOW.js (animazioni scroll)
- Owl Carousel (carousel homepage + testimonials)
- CounterUp (counter animato)
- Font: Open Sans + Teko (Google Fonts)
- Icone: Font Awesome 5 + Bootstrap Icons
- Backend contatti: PHP (`send_mail.php`) — PHP `mail()` nativo
- Lang: `lang="it"` su tutte le pagine

---

## Struttura file

```
/
├── index.html              — Homepage
├── about.html              — Team / Chi Siamo
├── service.html            — Servizi
├── feature.html            — Info / Caratteristiche + Clienti
├── contact.html            — Contatti
├── lavora-con-noi.html     — Lavora con Noi (nuova pagina)
├── project.html            — Progetti (non in navbar)
├── 404.html                — Pagina errore (non in navbar)
├── appointment.html        — Appuntamenti (non usata / nascosta)
├── team.html               — (non in navbar, probabilmente deprecata)
├── testimonial.html        — (non in navbar, probabilmente deprecata)
├── send_mail.php           — Backend form contatti
├── css/
│   ├── bootstrap.min.css
│   └── style.css           — Stili custom
├── js/
│   └── main.js             — JS custom (spinner, navbar, carousel, counter)
├── img/                    — Immagini (carousel, about, service, project, team)
├── docs/cv/                — CV scaricabili (luciano_taranto.pdf, salvatore_vancheri.pdf, andrea_taranto.pdf)
└── lib/                    — Librerie (wow, owlcarousel, counterup, easing, waypoints, tempusdominus)
```

---

## Navigazione (navbar — identica su tutte le pagine)

| Label navbar       | File                    |
|--------------------|-------------------------|
| Home               | `index.html`            |
| Servizi            | `service.html`          |
| Il nostro Team     | `about.html`            |
| Info               | `feature.html`          |
| Contatti           | `contact.html`          |
| Lavora con Noi     | `lavora-con-noi.html`   |

> `project.html` esiste ma **non è in navbar** — raggiungibile solo dai bottoni interni.

---

## Elementi comuni a tutte le pagine

**Spinner:** `#spinner` — div overlay bianco, scompare su load (1ms timeout in `main.js`).

**Navbar:** sticky-top, bg-white, logo (`img/icons/icon-1.png`) + testo studio. Su homepage: nascosta finché scroll < 300px. Su pagine interne: sempre visibile.

**Footer:** bg-dark, 3 colonne:
- Indirizzo + tel + email + social (Facebook, LinkedIn)
- Servizi (link placeholder vuoti — da aggiornare)
- Link Rapidi (link placeholder vuoti — da aggiornare)
- Copyright © Studio "Taranto - Vancheri"

**Back-to-top:** bottone fisso, appare dopo 300px scroll.

**Page Header (pagine interne):** banner scuro con titolo pagina + breadcrumb. Assente in homepage.

---

## Pagine — dettaglio sezioni

---

### `index.html` — Homepage

**Sezioni nell'ordine:**

1. **Carousel** (`owl-carousel header-carousel`)  
   3 slide, autoplay, dots con thumbnail immagine.  
   - Slide 1: `img/carousel-1.jpg` — CTA → `about.html` ("Leggi di più")  
   - Slide 2: `img/carousel-2.jpg` — CTA → `service.html` ("Scopri di più")  
   - Slide 3: `img/carousel-3.jpg` — CTA → `service.html` ("Scopri di più")  
   Testo slides: presentazione studio, sede Messina, approccio multidisciplinare.

2. **Team** (anteprima 3 soci principali)  
   Card con foto + nome + ruolo + LinkedIn (solo Luciano Taranto).  
   CTA → `about.html` ("Conosci tutto il team")

3. **Facts** (3 card bg-light con icona)  
   - Approccio al Design  
   - Soluzioni Innovative  
   - Gestione del Progetto

4. **About** (sezione Chi Siamo)  
   Immagini doppie (`about-1.jpg`, `about-2.jpg`). Counter animato "40 anni". Badge ISO 9001:2015.  
   CTA → `service.html`

5. **Servizi** (6 card con immagine sfondo + testo sovrapposto)  
   Progettazione / Direzione Lavori / Coordinamento Sicurezza / Collaudi / Gestione Pratiche / Consulenze Tecniche.  
   Tutti i CTA puntano a `service.html`.

6. **Feature** ("Perché sceglierci")  
   Testo + 3 punti (Esperienza, Qualità ISO, Approccio Integrato) + immagini.

7. **Progetti** (tab pill — 4 progetti)  
   Stessa struttura di `project.html`. CTA → `project.html`.

8. **Contatti** (form + info)  
   Form **NON collegato a `send_mail.php`** in homepage — action mancante, solo submit senza fetch.  
   Info: indirizzo, tel 090 714435, email info@example.com.

9. **Google Maps** embed — Studio Taranto-Vancheri (coordinate Messina).

> **Note:** Sezioni Appointment e Testimonial presenti nel codice ma commentate/nascoste.

---

### `about.html` — Il nostro Team / Chi Siamo

**Sezioni nell'ordine:**

1. **Page Header** — titolo "Chi Siamo" + breadcrumb

2. **About** — storia studio (1985, Messina, settore pubblico/privato), counter 40 anni, ISO badge.  
   CTA → `service.html`

3. **Team — Soci principali** (3 card con foto, CV scaricabile)

   | Nome | Ruolo | Albo | Bio |
   |------|-------|------|-----|
   | Ing. Luciano Taranto | Ingegnere Civile Edile — Fondatore | n.1238 | Nato Giarre (CT) 1959. Laureato Palermo 1985. Consigliere OI Messina (1993–2000 e 2013–2017), AD ATO ME 3 S.p.A. (2002–2006), Consulente tecnico-scientifico ARS (2013–2017). |
   | Ing. Salvatore Vancheri | Ingegnere Civile Edile — Socio | n.2232 | Nato Messina 1972. Laureato Messina 1998. Consulente tecnico banche, imprese costruzioni e aziende commerciali. |
   | Arch. Andrea Taranto | Architetto — Restauro e Design d'Interni | n.2230 | Nato Messina 1987. Laureato Reggio Calabria 2015. Iscritto OA Messina dal 19/07/2016. Consigliere OA Messina (2021–2025). Specializzato in restauro conservativo, interior design, relazioni paesaggistiche. |

   CV: `docs/cv/luciano_taranto.pdf`, `docs/cv/salvatore_vancheri.pdf`, `docs/cv/andrea_taranto.pdf`

4. **Collaboratori** (8 card senza foto, icona placeholder)

   | Nome | Ruolo specifico |
   |------|----------------|
   | Geom. Alessio Sturniolo | Progettazione CAD, Contabilità Lavori, Rilievi |
   | Geom. Domenico Puleio | Progettazione CAD e Design |
   | Ing. Francesco Venuto | Progettazione Strutturale, Efficientamento Energetico, Impianti |
   | Arch. Fabrizio Cacciola | Restauro, Interior Design — Residenze e Locali Commerciali |
   | P.E. Giuseppe Denaro | Progettazione CAD, Computi Metrici, Contabilità Lavori |
   | Arch. Cristina Lanteri | Restauro, Interior Design — Residenze e Locali Commerciali |
   | Ing. Francesca Ranieri | Ingegnere Civile Edile |
   | Geom. Francesco Mondo | Rilievi e Procedure Catastali |

---

### `service.html` — Servizi

**Sezioni nell'ordine:**

1. **Page Header** — titolo "Servizi" + breadcrumb

2. **Facts** (3 card): Progettazione Integrata / Qualità Certificata ISO 9001 / 40 Anni Esperienza

3. **Servizi** (6 card con immagine sfondo)

   | Servizio | Descrizione estesa |
   |----------|--------------------|
   | Progettazione | PFTE ed esecutiva, lavori pubblici/privati, civile/industriale/commerciale, sicurezza sismica, impianti, prevenzione incendi |
   | Direzione Lavori | DL civile e architettura, misura e contabilità, alta sorveglianza, direzione operativa |
   | Coordinamento Sicurezza | CSP (PSC) e CSE, POS, consulenza imprese |
   | Collaudi | Statici e tecnico-amministrativi, verifica preventiva art. 42 D.Lgs.36/2023 |
   | Gestione Pratiche | Comune, Genio Civile, Soprintendenza, ASL, ANAS, Demanio, catasto, VVF |
   | Consulenze Tecniche | Perizie asseverate/giurate, CTU Tribunali, consulenza di parte, perizie immobiliari stima |

4. **Settori di intervento** (8 badge)  
   Residenziale e Rurale / Ospedaliero e Sanitario / Commerciale / Scolastico / Alberghiero e Ristorazione / Militare / Chiese e Cimiteri / Opere Stradali e Urbanizzazione

---

### `feature.html` — Info / Caratteristiche

**Sezioni nell'ordine:**

1. **Page Header** — titolo "Caratteristiche" + breadcrumb

2. **Feature** ("Perché sceglierci") — 3 punti: Esperienza Pluridecennale / Qualità Certificata / Approccio Integrato

3. **Certificazioni** — ISO 9001:2015, cert. n. STUD4608Q2501, rilasciato EUCI

4. **Clienti** (3 colonne attive + 1 nota)

   **Enti Regionali, Nazionali e Sanitari (colonna 1):**  
   Regione Siciliana, ARS, Ministero Difesa (11° Reparto Infrastrutture), Tribunale Messina, Università Messina, Commissario Baraccopoli Messina, Commissario Dissesto Idrogeologico Sicilia, Società ATO ME 3 S.p.A., AOU G. Martino, AO Papardo, AO Piemonte IRCCS Bonino Pulejo, ASP 5 Messina, ASP 3 Catania, ASP 2 Caltanissetta, Città Metropolitana Messina, IACP Messina, AMAM, ATM, Consorzio Strade Siciliane

   **Comuni (colonna 2 — lista completa):**  
   Messina, Patti, S. Piero Patti, Limina, Noto, Marsala, Avola, Terme Vigliatore, Rometta, Tripi, Letojanni, Furnari, Monforte S. Giorgio, Forza d'Agrò, Montalbano Elicona, Novara di Sicilia, Mazzarrà Sant'Andrea, Valdina, Leni, Naso, Saponara, Galati Mamertino, Alcara Li Fusi

   **Privati e Aziende (colonna 3):**  
   Miscela d'Oro S.p.A., Unieuro S.p.A., Siesei S.p.A., Mohd Mollura Home Design S.p.A., Conivest Immobiliare S.p.A., Grimaldi Immobiliare, Arcidiocesi Messina/Lipari/S.Lucia del Mela, Ente Provincia Sicula C.C.R.R., Chiesa Evangelica Pentecostale Cristo Risorto, Opera Pia Istituto S. Lucia Palermo, Edifica s.r.l., Sitec s.r.l., Cogedis s.r.l., Edilcolor 2000 s.a.s.

---

### `contact.html` — Contatti

**Sezioni nell'ordine:**

1. **Page Header** — titolo "Contattaci" + breadcrumb

2. **Contatti** — info + form

   **Info:**
   - Indirizzo: Via Uberto Bonino, 8/scala G, 98124 Messina ME
   - Tel: 090 714435
   - Email: info@example.com

   **Form** (`id="contactForm"`, `novalidate`):  
   Campi: nome, email, oggetto, messaggio + honeypot `name="website"` (nascosto anti-spam).  
   Submit AJAX → `fetch('send_mail.php')` → risposta JSON → `#formFeedback` alert success/danger.  
   Email recapitata a: rosarionapoli99@gmail.com

3. **Google Maps** — embed Studio Taranto-Vancheri Messina

---

### `lavora-con-noi.html` — Lavora con Noi _(nuova pagina)_

**In navbar: sì.**

**Sezioni nell'ordine:**

1. **Page Header** — titolo "Lavora con Noi" + breadcrumb

2. **Intro** — presentazione studio, invito a unirsi al team. Immagini `about-1.jpg` / `about-2.jpg`.

3. **Posizione aperta** (bg-light)  
   Figura cercata: **Ingegnere — Efficientamento Energetico & Impiantistico**  
   - Cosa cerchiamo: laurea ingegneria, normative L.10/91, APE, impianti, autonomia, iscrizione albo  
   - Cosa offriamo: studio 40+ anni, affiancamento senior, varietà progetti, ISO 9001, flessibilità  
   - CTA → `contact.html` ("Invia la tua candidatura")

4. **Candidatura spontanea**  
   Aperta a ingegneri, architetti, geometri, periti. Contatti: email + telefono.  
   2 fact card: "40+ anni di storia" / "Team multidisciplinare"

---

### `project.html` — Progetti

**Non in navbar.** Raggiungibile da CTA homepage e sezione progetti.

**Sezioni nell'ordine:**

1. **Page Header** — titolo "Progetti" + breadcrumb

2. **Progetti** (tab pill Bootstrap — 4 tab)

   | # | Nome | Descrizione |
   |---|------|-------------|
   | 01 | Free-Flow A18 | PFTE impianto esazione pedaggi Free-Flow, A18 Siracusa-Gela (Lotti 3-8). Committente pubblico. |
   | 02 | PINQuA Trapani | Recupero Rione Cappuccinelli Trapani. Programma PNRR/PINQuA 1. Ufficio DL + Direttore Operativo. |
   | 03 | Miscela d'Oro | Restauro Flagship Store Piazza Cairoli Messina + magazzino automatico caffè via E. Fermi (ZIR). Committente privato. |
   | 04 | Palazzo Arezzo | Progetto strutturale restauro conservativo Palazzo Arezzo di Donnafugata, Ragusa Ibla. Cambio destinazione d'uso in struttura turistico-ricettiva. |

   Immagini: `img/project-1.jpg` … `img/project-4.jpg`

---

### `send_mail.php` — Backend form

- Honeypot: se `$_POST['website']` non vuoto → risponde success silenzioso (bot trap)
- Validazione: tutti i campi obbligatori + `FILTER_VALIDATE_EMAIL`
- Sanitizzazione: `htmlspecialchars` + `strip_tags`
- Invio: `mail()` nativo PHP a `rosarionapoli99@gmail.com`
- Risposta: JSON `{success: bool, message: string}`

---

### Pagine non attive / non in navbar

- `404.html` — pagina errore custom
- `appointment.html` — form appuntamento (codice presente ma commentato in homepage)
- `team.html` — probabilmente precedente versione di `about.html`
- `testimonial.html` — sezione testimonials (commentata/nascosta ovunque)

---

## Contenuti da aggiornare / TODO noti

- `info@example.com` → sostituire con email reale dello studio in tutte le pagine e footer
- Footer: link "Servizi" e "Link Rapidi" sono `href=""` — placeholder, non puntano a nessuna pagina
- Form homepage (`index.html`) non collegato a `send_mail.php` (nessun fetch JS) — solo in `contact.html`
- CV collaboratori: file PDF non ancora caricati (path attivi solo per i 3 soci principali)
- `project.html` non inserito in navbar (scelta intenzionale o da valutare)
- Sezione Testimonials commentata — da attivare quando ci sono recensioni reali

---

## Immagini principali

| File | Utilizzo |
|------|----------|
| `img/carousel-1/2/3.jpg` | Slide homepage carousel |
| `img/about-1/2.jpg` | Sezione Chi Siamo + Lavora con Noi (doppia immagine sovrapposta) |
| `img/service-1…6.jpg` | Sfondo card servizi |
| `img/project-1…4.jpg` | Tab progetti |
| `img/icons/icon-1.png` | Logo navbar + spinner |
| `img/icons/icon-2…10.png` | Icone fact/feature/service |

## Foto team (`photo/`)

| File | Utilizzo | Dove |
|------|----------|------|
| `photo/luciano.jpg` | Ing. Luciano Taranto | `index.html` (anteprima team) + `about.html` (card socio) |
| `photo/salvatore_vancheri.jpg` | Ing. Salvatore Vancheri | `index.html` + `about.html` |
| `photo/andrea_taranto.jpg` | Arch. Andrea Taranto | `index.html` + `about.html` |
| `photo/alessio_sturniolo.jpg` | Geom. Alessio Sturniolo | `about.html` (collaboratori, cerchio 100px) |
| `photo/domenico_puleo.jpg` | Geom. Domenico Puleio | `about.html` (collaboratori) |
| `photo/francesco_venuto.jpg` | Ing. Francesco Venuto | `about.html` (collaboratori) |
| `photo/fabrizio_cacciola.jpg` | Arch. Fabrizio Cacciola | `about.html` (collaboratori) |
| `photo/giuseppe_denaro.jpg` | P.E. Giuseppe Denaro | `about.html` (collaboratori) |
| `photo/cristina_lanteri.jpg` | Arch. Cristina Lanteri | `about.html` (collaboratori) |
| `photo/francesco_mondo.jpg` | Geom. Francesco Mondo | `about.html` (collaboratori) |
| `photo/all_team.jpg` | Foto gruppo team | Non ancora usata in pagine |
| `photo/office_all_team.jpg` | Team in ufficio | Non ancora usata in pagine |
| `photo/office_1/2/3/4.jpg` | Foto ufficio | Non ancora usate in pagine |
| `photo/vertical_office.jpg` / `photo/vertical_office_2.jpg` | Foto verticali ufficio | Non ancora usate in pagine |
| `photo/duo.jpg` | Foto coppia (uso da verificare) | Non ancora usata in pagine |
| `photo/luciano_2.jpg` | Seconda foto Luciano Taranto | Disponibile come alternativa |

> **Nota:** Ing. Francesca Ranieri non ha foto in `photo/` — mantiene icona placeholder `fa-user-circle` in `about.html`.
