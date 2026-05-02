from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, ListFlowable, ListItem
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

os.makedirs("docs/cv", exist_ok=True)

PRIMARY = colors.HexColor("#0d6efd")
DARK = colors.HexColor("#1a1a2e")

def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle("CVName", fontSize=22, textColor=DARK, spaceAfter=2, fontName="Helvetica-Bold"))
    styles.add(ParagraphStyle("CVRole", fontSize=13, textColor=PRIMARY, spaceAfter=8, fontName="Helvetica-Oblique"))
    styles.add(ParagraphStyle("CVSection", fontSize=12, textColor=PRIMARY, spaceBefore=14, spaceAfter=4, fontName="Helvetica-Bold"))
    styles.add(ParagraphStyle("CVBody", fontSize=10, textColor=DARK, spaceAfter=4, fontName="Helvetica", leading=14))
    styles.add(ParagraphStyle("CVBullet", fontSize=10, textColor=DARK, spaceAfter=2, fontName="Helvetica", leftIndent=12, leading=13))
    styles.add(ParagraphStyle("CVFooter", fontSize=8, textColor=colors.grey, alignment=TA_CENTER))
    return styles

def section(title, styles):
    return [
        Spacer(1, 4),
        Paragraph(title.upper(), styles["CVSection"]),
        HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=6),
    ]

def bullet(text, styles):
    return Paragraph(f"• {text}", styles["CVBullet"])

# Ing. Luciano Taranto
def cv_luciano(styles):
    story = []
    story.append(Paragraph("Ing. Luciano Taranto", styles["CVName"]))
    story.append(Paragraph("Ingegnere Civile Edile — Socio Fondatore", styles["CVRole"]))
    story.append(HRFlowable(width="100%", thickness=2, color=PRIMARY, spaceAfter=10))

    story += section("Dati Personali", styles)
    story.append(Paragraph("Nato a Giarre (CT) nel 1959", styles["CVBody"]))
    story.append(Paragraph("Iscritto all'Ordine degli Ingegneri della Provincia di Messina dal 26/06/1985 — n.1238", styles["CVBody"]))

    story += section("Formazione", styles)
    story.append(Paragraph("Laurea in Ingegneria Civile Edile — Università degli Studi di Palermo, 1985", styles["CVBody"]))

    story += section("Incarichi Istituzionali", styles)
    for item in [
        "Componente di numerose commissioni edilizie e urbanistiche di vari Comuni della Provincia di Messina",
        "Componente U.R.E.C.A. di commissioni di gara",
        "Consigliere dell'Ordine Provinciale degli Ingegneri di Messina",
        "Amministratore Delegato della Società d'Ambito ATO ME 3 S.p.A.",
        "Consulente tecnico-scientifico dell'Assemblea Regionale Siciliana",
        "Consulente Tecnico di Parte di Comuni Siciliani e Imprese di costruzioni",
    ]:
        story.append(bullet(item, styles))

    story += section("Principali Progetti", styles)
    progetti = [
        "Fabbricato per civile abitazione a quattro elevazioni f.t. — Messina, Salite Fosse, via Nuova Panoramica dello Stretto",
        "Programma Innovativo Nazionale PINQuA 1 — Recupero e Rigenerazione Urbana del Rione Cappuccinelli, Trapani (Ufficio D.L., Direttore Operativo)",
        "Opere di urbanizzazione primaria — Insediamenti produttivi artigianali, S. Piero Patti",
        "Adeguamento locali U.O.C. Anatomia Patologica, Presidio Ospedaliero 'Santo Pietro', Caltagirone (CT)",
        "Casa di comunità — Poliambulatorio di Riesi (CL): verifica vulnerabilità sismica",
        "Chiesa Cristiana Evangelica — Messina, via Tusa",
        "Impianto esazione pedaggi Free-Flow A18 Siracusa-Gela, Lotti 3-4-5 (PFTE)",
        "Impianto esazione pedaggi Free-Flow A18 Siracusa-Gela, Lotti 6-7-8 (PFTE)",
        "Manutenzione straordinaria edifici Compagnia dei Carabinieri di Patti",
        "Verifica strutturale per apparecchiatura TAC/TLC/Angiografo — Policlinico Universitario di Messina",
        "Fabbricato civile a tre elevazioni — Messina, villaggio Sant'Agata, contrada Principi",
        "Edificio residenziale quattro elevazioni f.t. — Messina, località Grotte",
        "Restauro Flagship store Miscela d'Oro — Messina, Piazza Cairoli",
        "Restauro conservativo Cappella funeraria 'Sant'Onofrio' — Gran Camposanto di Messina",
        "Restauro conservativo Cappella funeraria 'S. Cristoforo' — Gran Camposanto di Messina",
        "Restauro Palazzo Arezzo di Donnafugata — Ragusa Ibla (cambio d'uso ad attività turistico-ricettiva)",
        "Magazzino automatico per stoccaggio caffè — Messina, via Enrico Fermi (Miscela d'Oro S.p.A.)",
        "Restauro conservativo Santuario della Madonna di Lourdes — Messina, viale Regina Margherita",
        "Restauro Cappella funeraria 'S. Liberale' — Gran Camposanto di Messina",
        "Restauro Cappella funeraria 'San Francesco dei Mercanti' — Gran Camposanto di Messina",
        "Recupero fabbricati ad alloggi popolari — Comune di Limina (1° stralcio funzionale)",
        "Complesso edilizio residenze/uffici/commerciali — Messina, via Bonino",
        "Ex scuola elementare convertita a caserma — Comune di Terme Vigliatore",
        "Ristrutturazione Casa di Cura 'S. Camillo' — adeguamento L.R.39/88",
        "Manutenzione straordinaria Santuario di Dinnammare — Messina",
        "Albergo 4 stelle con centro benessere — Castelmola (ME), c/da Dietrà Marino (Progetto definitivo)",
        "Complesso residenziale 12 unità abitative — Messina, villaggio Rodia",
        "Manutenzione straordinaria Chiesa Parrocchiale Maria SS. Del Tindari — Braidi, Serro Tindari",
        "Opere di urbanizzazione primaria — Annunziata, contrada Ciaramita, Messina",
    ]
    for p in progetti:
        story.append(bullet(p, styles))

    story.append(Spacer(1, 20))
    story.append(Paragraph("Studio Taranto-Vancheri — Via Uberto Bonino 8/G, 98124 Messina — Tel. 090 714435", styles["CVFooter"]))
    return story

# Ing. Salvatore Vancheri
def cv_salvatore(styles):
    story = []
    story.append(Paragraph("Ing. Salvatore Vancheri", styles["CVName"]))
    story.append(Paragraph("Ingegnere Civile Edile — Socio", styles["CVRole"]))
    story.append(HRFlowable(width="100%", thickness=2, color=PRIMARY, spaceAfter=10))

    story += section("Dati Personali", styles)
    story.append(Paragraph("Nato a Messina nel 1972", styles["CVBody"]))
    story.append(Paragraph("Iscritto all'Ordine degli Ingegneri della Provincia di Messina dal 27/07/1998 — n.2232", styles["CVBody"]))

    story += section("Formazione", styles)
    story.append(Paragraph("Laurea in Ingegneria Civile Edile — Università degli Studi di Messina, 1998", styles["CVBody"]))

    story += section("Attività Professionale", styles)
    story.append(Paragraph("Libero professionista dal 1998. Ha sempre svolto attività nel settore dell'ingegneria civile ed edile, operando come consulente tecnico per istituti bancari, imprese di costruzioni e aziende commerciali.", styles["CVBody"]))

    for item in [
        "Progettazione e direzione lavori in ambito civile e infrastrutturale",
        "Consulente Tecnico di Istituti Bancari",
        "Consulente per Imprese di costruzioni e Aziende commerciali",
    ]:
        story.append(bullet(item, styles))

    story.append(Spacer(1, 20))
    story.append(Paragraph("Studio Taranto-Vancheri — Via Uberto Bonino 8/G, 98124 Messina — Tel. 090 714435", styles["CVFooter"]))
    return story

# Arch. Andrea Taranto
def cv_andrea(styles):
    story = []
    story.append(Paragraph("Arch. Andrea Taranto", styles["CVName"]))
    story.append(Paragraph("Architetto — Responsabile Architettura e Design", styles["CVRole"]))
    story.append(HRFlowable(width="100%", thickness=2, color=PRIMARY, spaceAfter=10))

    story += section("Dati Personali", styles)
    story.append(Paragraph("Nato a Messina nel 1987", styles["CVBody"]))
    story.append(Paragraph("Iscritto all'Ordine degli Architetti P.P.C. della Provincia di Messina dal 19/07/2016 — n.2230", styles["CVBody"]))

    story += section("Formazione", styles)
    story.append(Paragraph("Laurea in Architettura — Università degli Studi Mediterranea di Reggio Calabria, 2015", styles["CVBody"]))

    story += section("Incarichi Istituzionali", styles)
    story.append(bullet("Consigliere dell'Ordine degli Architetti P.P.C. della Provincia di Messina", styles))

    story += section("Attività Professionale", styles)
    story.append(Paragraph("Libero professionista dal 2016. All'interno dello studio si occupa dei servizi riguardanti l'architettura, con particolare specializzazione in:", styles["CVBody"]))
    for item in [
        "Progettazione e direzione lavori di restauro conservativo",
        "Design di interni di residenze private",
        "Design di interni di locali commerciali",
        "Progettazione architettonica per interventi residenziali e commerciali",
    ]:
        story.append(bullet(item, styles))

    story.append(Spacer(1, 20))
    story.append(Paragraph("Studio Taranto-Vancheri — Via Uberto Bonino 8/G, 98124 Messina — Tel. 090 714435", styles["CVFooter"]))
    return story


def generate(filename, story_fn, styles):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm,
    )
    doc.build(story_fn(styles))
    print(f"  OK {filename}")

if __name__ == "__main__":
    styles = build_styles()
    print("Generazione CV PDF...")
    generate("docs/cv/luciano_taranto.pdf", cv_luciano, styles)
    generate("docs/cv/salvatore_vancheri.pdf", cv_salvatore, styles)
    generate("docs/cv/andrea_taranto.pdf", cv_andrea, styles)
    print("Completato.")
