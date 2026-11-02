"""One-page CV: source text comes from the website's FR/EN locale modules."""
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr
try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor, white
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import Paragraph
    from reportlab.lib.styles import ParagraphStyle
except ImportError:
    sys.exit('ReportLab manquant : lancer npm run pdf:setup, puis npm run pdf.')

W, H = 595.276, 841.89
PINK, DARK, INK, MUTED, PALE = map(HexColor, ['#F25170', '#302E34', '#36343B', '#68656C', '#F6F4F5'])


def clean(value):
    return escape(str(value).replace('—', '-').replace('–', '-').replace('\u2011', '-'))


def entries(section):
    return [value for value in section.values() if isinstance(value, dict)]


def render(root, out, data, locale):
    for name, filename in [('Lato', 'Regular'), ('LatoBold', 'Bold'), ('LatoItalic', 'Italic')]:
        pdfmetrics.registerFont(TTFont(name, str(root / f'scripts/pdf/fonts/Lato-{filename}.ttf')))
    pdfmetrics.registerFontFamily('Lato', normal='Lato', bold='LatoBold', italic='LatoItalic')
    profile = json.loads((root / 'scripts/pdf/profile.json').read_text())
    c = canvas.Canvas(str(out), pagesize=(W, H), invariant=1)
    c.setTitle(profile['firstName'] + ' ' + profile['lastName'] + ' - ' + data['userProfile']['job'])
    c.setAuthor(profile['firstName'] + ' ' + profile['lastName'])
    c.setFillColor(PALE); c.rect(0, 0, 187, H, fill=1, stroke=0)
    c.setFillColor(DARK); c.rect(187, H-160, W-187, 160, fill=1, stroke=0)
    c.setFillColor(PINK); c.rect(0, H-160, 187, 160, fill=1, stroke=0)
    c.rect(0, H-8, W, 8, fill=1, stroke=0); c.rect(0, 0, W, 4, fill=1, stroke=0)
    c.saveState()
    path = c.beginPath(); path.circle(93.5, H-84, 61); c.clipPath(path, stroke=0, fill=0)
    c.drawImage(str(root / 'src/assets/user.png'), 32.5, H-145, width=122, height=122, mask='auto', preserveAspectRatio=True, anchor='c')
    c.restoreState()

    def p(text, x, y, width, size=9.2, leading=12, color=INK, bold=False):
        paragraph = Paragraph(text, ParagraphStyle('cv', fontName='LatoBold' if bold else 'Lato', fontSize=size, leading=leading, textColor=color))
        _, height = paragraph.wrap(width, H)
        if y-height < 20:
            raise ValueError(f'{locale.upper()} : contenu trop long pour une page (près de « {text[:75]} »). Raccourcir les textes dans src/i18n/{locale}.ts. Aucun PDF remplacé.')
        paragraph.drawOn(c, x, y-height)
        return y-height

    def label(text, x, y, width):
        c.setFillColor(PINK); c.rect(x, y-3, 18, 2, fill=1, stroke=0)
        return p(clean(text.rstrip(' :')).upper(), x, y-10, width, 9.5, 12, DARK, True)-8

    def link(text, url):
        return f'<link href={quoteattr(url)} color="#A7304C">{clean(text)}</link>'

    p(clean(profile['firstName']), 210, H-27, 362, 24, 27, white)
    p(clean(profile['lastName'].upper()), 210, H-53, 362, 30, 34, white, True)
    p(clean(data['userProfile']['job']), 210, H-101, 362, 11, 15, white, True)
    x, width, y = 20, 147, H-178
    y = label(data['personalInformation']['title'], x, y, width)
    for text in [link(profile['email'], 'mailto:'+profile['email']), link(profile['phone'], profile['phoneUri']), clean(profile['location']), link(profile['website'].removeprefix('https://'), profile['website']), link('LinkedIn / '+profile['firstName']+' '+profile['lastName'], profile['linkedin'])]:
        y = p(text, x, y, width, 9, 12)-3
    y = label(data['userCompetence']['title'], x, y-8, width)
    for group in data['competenceGroups']:
        y = p(clean(group['name']), x, y, width, 9, 11, DARK, True)
        y = p(clean(' · '.join(group['items'])), x, y-2, width, 8.7, 11.3, MUTED)-7
    y = label(data['userEducation']['title'], x, y-2, width)
    for item in entries(data['userEducation']):
        y = p(clean(item['title'] + ' · ' + item['date']), x, y, width, 9, 11, DARK, True)
        y = p(clean(item['location']), x, y-2, width, 8.5, 11, MUTED)-7
    y = label(data['userLanguages']['title'], x, y-2, width)
    for lang in ['Fr', 'En', 'Jp']:
        y = p('<b>'+clean(data['userLanguages']['name'+lang])+'</b> · '+clean(data['userLanguages']['label'+lang]), x, y, width, 8.7, 12)

    x, width, y = 210, 362, H-178
    y = p(clean(data['userAbout']['text1']), x, y, width, 10, 14)-8
    y = p(clean(data['search']['text']), x, y, width, 9.2, 12.5, MUTED)
    y = label(data['professionalExperiences']['title'], x, y-12, width)
    for item in entries(data['professionalExperiences']):
        p(clean(item['date']), x+width-78, y, 78, 9, 12, PINK, True)
        y = p(clean(item['location']), x, y, width-85, 10, 12.5, DARK, True)
        y = p(clean(item['title']), x, y-2, width, 9, 12, MUTED)
        y = p(clean(' '.join(item['bullets'])), x, y-4, width, 9.2, 12.5)-9
    y = label(data['portfolio']['title'], x, y-1, width)
    # Compact portfolio: all project links, full descriptions remain on the website.
    for item in entries(data['portfolio']):
        y = p('<b>'+clean(item['name'])+'</b> · '+link(item['url'].removeprefix('https://').rstrip('/'), item['url']), x, y, width, 9, 12)-3
    c.showPage(); c.save()


def main():
    root, temp, output = map(Path, sys.argv[1:])
    data = json.load(sys.stdin)
    # Both languages must pass layout validation before either public file changes.
    for locale in ['fr', 'en']:
        render(root, temp / f'cv-fabien-crovetti-{locale}.pdf', data[locale], locale)
    output.mkdir(parents=True, exist_ok=True)
    for locale in ['fr', 'en']:
        name = f'cv-fabien-crovetti-{locale}.pdf'
        (output / name).write_bytes((temp / name).read_bytes())
        print(f'PDF {locale.upper()} : {output / name}')


if __name__ == '__main__':
    try:
        main()
    except ValueError as error:
        sys.exit(str(error))
