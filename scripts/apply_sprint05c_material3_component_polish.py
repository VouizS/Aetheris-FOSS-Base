from pathlib import Path
import re

print("Aplicando Sprint 05C — Material 3 Component Polish")

manifest = Path("app/src/main/AndroidManifest.xml")
theme_name = "AppTheme"

if manifest.exists():
    ms = manifest.read_text()
    m = re.search(r'android:theme="@style/([^"]+)"', ms)
    if m:
        theme_name = m.group(1)

print("Tema principal detectado:", theme_name)

# 1) Segurança: remover AppTheme duplicado de styles.xml
def remove_style(path: Path, name: str):
    if not path.exists():
        return
    s = path.read_text()
    old = s
    pattern = rf'\s*<style\s+name="{re.escape(name)}"[^>]*>.*?</style>'
    s = re.sub(pattern, "\n", s, flags=re.S)
    s = re.sub(r'\n{3,}', '\n\n', s)
    if s != old:
        path.write_text(s)
        print("Tema duplicado removido de:", path)

remove_style(Path("app/src/main/res/values/styles.xml"), theme_name)
remove_style(Path("app/src/main/res/values-night/styles.xml"), theme_name)

# 2) Helpers XML
def ensure_file(path: Path):
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("<resources>\n</resources>\n")
    return path.read_text()

def upsert_color(xml: str, name: str, value: str) -> str:
    pattern = rf'<color name="{re.escape(name)}">.*?</color>'
    replacement = f'<color name="{name}">{value}</color>'
    if re.search(pattern, xml):
        return re.sub(pattern, replacement, xml)
    return xml.replace("</resources>", f"    {replacement}\n</resources>")

def upsert_dimen(xml: str, name: str, value: str) -> str:
    pattern = rf'<dimen name="{re.escape(name)}">.*?</dimen>'
    replacement = f'<dimen name="{name}">{value}</dimen>'
    if re.search(pattern, xml):
        return re.sub(pattern, replacement, xml)
    return xml.replace("</resources>", f"    {replacement}\n</resources>")

# 3) Paleta Material 3 baseline light
colors_light = Path("app/src/main/res/values/colors.xml")
s = ensure_file(colors_light)

light = {
    "m3_primary": "#6750A4",
    "m3_on_primary": "#FFFFFF",
    "m3_primary_container": "#EADDFF",
    "m3_on_primary_container": "#21005D",

    "m3_secondary": "#625B71",
    "m3_on_secondary": "#FFFFFF",
    "m3_secondary_container": "#E8DEF8",
    "m3_on_secondary_container": "#1D192B",

    "m3_tertiary": "#7D5260",
    "m3_on_tertiary": "#FFFFFF",
    "m3_tertiary_container": "#FFD8E4",
    "m3_on_tertiary_container": "#31111D",

    "m3_error": "#B3261E",
    "m3_on_error": "#FFFFFF",
    "m3_error_container": "#F9DEDC",
    "m3_on_error_container": "#410E0B",

    "m3_background": "#FFFBFE",
    "m3_on_background": "#1C1B1F",
    "m3_surface": "#FFFBFE",
    "m3_on_surface": "#1C1B1F",
    "m3_surface_variant": "#E7E0EC",
    "m3_on_surface_variant": "#49454F",
    "m3_outline": "#79747E",
    "m3_outline_variant": "#CAC4D0",
    "m3_inverse_surface": "#313033",
    "m3_inverse_on_surface": "#F4EFF4",
    "m3_inverse_primary": "#D0BCFF",

    "m3_surface_container_lowest": "#FFFFFF",
    "m3_surface_container_low": "#F7F2FA",
    "m3_surface_container": "#F3EDF7",
    "m3_surface_container_high": "#ECE6F0",
    "m3_surface_container_highest": "#E6E0E9",

    "ic_launcher_background": "#050B18",

    # Compatibilidade herdada da base
    "red": "#F44336",
    "pink": "#E91E63",
    "purple": "#9C27B0",
    "blue": "#2196F3",
    "teal": "#009688",
    "green": "#4CAF50",
    "lime": "#CDDC39",
    "yellow": "#FFEB3B",
    "orange": "#FF9800",
    "brown": "#795548",
    "grey": "#9E9E9E",
}

for k, v in light.items():
    s = upsert_color(s, k, v)

colors_light.write_text(s)
print("Cores Material 3 light atualizadas")

# 4) Paleta Material 3 baseline dark
colors_dark = Path("app/src/main/res/values-night/colors.xml")
s = ensure_file(colors_dark)

dark = {
    "m3_primary": "#D0BCFF",
    "m3_on_primary": "#381E72",
    "m3_primary_container": "#4F378B",
    "m3_on_primary_container": "#EADDFF",

    "m3_secondary": "#CCC2DC",
    "m3_on_secondary": "#332D41",
    "m3_secondary_container": "#4A4458",
    "m3_on_secondary_container": "#E8DEF8",

    "m3_tertiary": "#EFB8C8",
    "m3_on_tertiary": "#492532",
    "m3_tertiary_container": "#633B48",
    "m3_on_tertiary_container": "#FFD8E4",

    "m3_error": "#F2B8B5",
    "m3_on_error": "#601410",
    "m3_error_container": "#8C1D18",
    "m3_on_error_container": "#F9DEDC",

    "m3_background": "#141218",
    "m3_on_background": "#E6E0E9",
    "m3_surface": "#141218",
    "m3_on_surface": "#E6E0E9",
    "m3_surface_variant": "#49454F",
    "m3_on_surface_variant": "#CAC4D0",
    "m3_outline": "#938F99",
    "m3_outline_variant": "#49454F",
    "m3_inverse_surface": "#E6E0E9",
    "m3_inverse_on_surface": "#313033",
    "m3_inverse_primary": "#6750A4",

    "m3_surface_container_lowest": "#0F0D13",
    "m3_surface_container_low": "#1D1B20",
    "m3_surface_container": "#211F26",
    "m3_surface_container_high": "#2B2930",
    "m3_surface_container_highest": "#36343B",
}

for k, v in dark.items():
    s = upsert_color(s, k, v)

colors_dark.write_text(s)
print("Cores Material 3 dark atualizadas")

# 5) Dimens oficiais de polimento visual
dimens = Path("app/src/main/res/values/dimens.xml")
s = ensure_file(dimens)

dimens_values = {
    "m3_corner_extra_small": "4dp",
    "m3_corner_small": "8dp",
    "m3_corner_medium": "12dp",
    "m3_corner_large": "16dp",
    "m3_corner_extra_large": "28dp",
    "m3_card_corner_radius": "24dp",
    "m3_menu_corner_radius": "28dp",
    "m3_nav_corner_radius": "24dp",
    "m3_fab_size": "56dp",
    "m3_touch_target": "48dp",
    "m3_spacing_small": "8dp",
    "m3_spacing_medium": "16dp",
    "m3_spacing_large": "24dp",
}

for k, v in dimens_values.items():
    s = upsert_dimen(s, k, v)

dimens.write_text(s)
print("Dimens Material 3 adicionadas")

# 6) Styles de shape/componente sem duplicar AppTheme
styles = Path("app/src/main/res/values/styles.xml")
s = ensure_file(styles)

def upsert_style(xml: str, name: str, body: str) -> str:
    pattern = rf'\s*<style\s+name="{re.escape(name)}"[^>]*>.*?</style>'
    style = f'''    <style name="{name}">
{body}
    </style>
'''
    if re.search(pattern, xml, flags=re.S):
        return re.sub(pattern, "\n" + style, xml, flags=re.S)
    return xml.replace("</resources>", style + "</resources>")

s = upsert_style(s, "ShapeAppearance.Aetheris.M3.Small", """        <item name="cornerFamily">rounded</item>
        <item name="cornerSize">@dimen/m3_corner_small</item>""")

s = upsert_style(s, "ShapeAppearance.Aetheris.M3.Medium", """        <item name="cornerFamily">rounded</item>
        <item name="cornerSize">@dimen/m3_corner_medium</item>""")

s = upsert_style(s, "ShapeAppearance.Aetheris.M3.Large", """        <item name="cornerFamily">rounded</item>
        <item name="cornerSize">@dimen/m3_corner_large</item>""")

s = upsert_style(s, "ShapeAppearance.Aetheris.M3.ExtraLarge", """        <item name="cornerFamily">rounded</item>
        <item name="cornerSize">@dimen/m3_corner_extra_large</item>""")

s = upsert_style(s, "Widget.Aetheris.M3.MaterialCardView", """        <item name="cardCornerRadius">@dimen/m3_card_corner_radius</item>
        <item name="cardElevation">0dp</item>
        <item name="strokeColor">@color/m3_outline_variant</item>
        <item name="strokeWidth">1dp</item>""")

styles.write_text(re.sub(r'\n{3,}', '\n\n', s))
print("Styles de componentes Material 3 adicionados")

# 7) Injetar itens de tema com segurança
def inject_theme_items(path: Path, name: str):
    if not path.exists():
        return

    xml = path.read_text()

    items = {
        "shapeAppearanceSmallComponent": "@style/ShapeAppearance.Aetheris.M3.Small",
        "shapeAppearanceMediumComponent": "@style/ShapeAppearance.Aetheris.M3.Medium",
        "shapeAppearanceLargeComponent": "@style/ShapeAppearance.Aetheris.M3.Large",
        "materialCardViewStyle": "@style/Widget.Aetheris.M3.MaterialCardView",
        "colorControlNormal": "@color/m3_on_surface_variant",
        "colorControlActivated": "@color/m3_primary",
        "android:colorAccent": "@color/m3_primary",
        "colorAccent": "@color/m3_primary",
        "android:forceDarkAllowed": "false",
    }

    pattern = rf'(<style\s+name="{re.escape(name)}"[^>]*>)(.*?)(</style>)'
    m = re.search(pattern, xml, flags=re.S)
    if not m:
        print("Tema não encontrado em:", path)
        return

    body = m.group(2)

    for item_name, item_value in items.items():
        item_pattern = rf'<item name="{re.escape(item_name)}">.*?</item>'
        item_xml = f'        <item name="{item_name}">{item_value}</item>'
        if re.search(item_pattern, body):
            body = re.sub(item_pattern, item_xml, body)
        else:
            body += "\n" + item_xml

    new_style = m.group(1) + body + "\n    " + m.group(3)
    xml = xml[:m.start()] + new_style + xml[m.end():]
    xml = re.sub(r'\n{3,}', '\n\n', xml)
    path.write_text(xml)
    print("Tema polido em:", path)

inject_theme_items(Path("app/src/main/res/values/themes.xml"), theme_name)
inject_theme_items(Path("app/src/main/res/values-night/themes.xml"), theme_name)

# 8) Segurança: remover background duplicado
dup = Path("app/src/main/res/values/ic_launcher_background.xml")
if dup.exists():
    dup.unlink()
    print("ic_launcher_background.xml duplicado removido")

# 9) Atualizar versão
gradle = Path("app/build.gradle")
if gradle.exists():
    s = gradle.read_text()
    s = re.sub(r'versionCode\s+\d+', 'versionCode 4', s)
    s = re.sub(r'versionName\s+"[^"]+"', 'versionName "0.2.2-m3polish"', s)
    gradle.write_text(s)
    print("Versão atualizada para 0.2.2-m3polish")

# 10) Documentação
notes = Path("docs/releases/SPRINT_05C_MATERIAL3_COMPONENT_POLISH.md")
notes.write_text("""# Aetheris Sprint 05C — Material 3 Component Polish

## Objetivo

Refinar a camada Material 3 já aplicada na Sprint 05B usando tokens oficiais de cor, superfície, shape, controle e estilos de componente.

## Alterações

- Paleta Material 3 baseline light/dark ajustada.
- Surface containers adicionados.
- Dimens de canto, espaçamento e toque adicionadas.
- ShapeAppearance Small/Medium/Large/ExtraLarge criadas.
- MaterialCardView style criado para cards com cantos mais modernos.
- colorControlNormal/colorControlActivated alinhados ao tema.
- colorAccent alinhado ao primary Material 3.
- AppTheme duplicado continua proibido em styles.xml.
- ic_launcher_background duplicado continua removido.
- Versão ajustada para 0.2.2-m3polish.

## Não alterado

- Motor WebView.
- Abas.
- Histórico.
- Favoritos.
- Downloads.
- Permissões.
- WebRTC.
- Extensões.
- Filtros de câmera.

## Checklist de teste

- [ ] APK instala.
- [ ] App abre sem crash.
- [ ] Menu flutuante abre.
- [ ] Abas/favoritos/histórico aparecem.
- [ ] Configurações abrem.
- [ ] Tema escuro está legível.
- [ ] Cards não quebraram.
- [ ] Bottom bar continua funcionando.
- [ ] Navegação continua funcionando.
""")

print("Sprint 05C aplicada com sucesso.")
