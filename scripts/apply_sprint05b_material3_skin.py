from pathlib import Path
import re

print("Aplicando Sprint 05B — Material 3 Skin Base")

# Detectar tema usado no AndroidManifest
manifest = Path("app/src/main/AndroidManifest.xml")
theme_name = "Theme.Aetheris"

if manifest.exists():
    ms = manifest.read_text()
    m = re.search(r'android:theme="@style/([^"]+)"', ms)
    if m:
        theme_name = m.group(1)

print("Tema detectado:", theme_name)

# Garantir Material Components atualizado no Gradle
gradle = Path("app/build.gradle")
if gradle.exists():
    s = gradle.read_text()

    if "com.google.android.material:material" in s:
        s = re.sub(
            r"implementation\s+['\"]com\.google\.android\.material:material:[^'\"]+['\"]",
            "implementation 'com.google.android.material:material:1.14.0'",
            s
        )
    else:
        s = s.replace(
            "dependencies {\n",
            "dependencies {\n    implementation 'com.google.android.material:material:1.14.0'\n"
        )

    gradle.write_text(s)
    print("Gradle verificado com Material Components")

def ensure_resources_file(path: Path):
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

# Paleta Material 3 clara
colors_light = Path("app/src/main/res/values/colors.xml")
s = ensure_resources_file(colors_light)

light_palette = {
    "m3_primary": "#0061A4",
    "m3_on_primary": "#FFFFFF",
    "m3_primary_container": "#D1E4FF",
    "m3_on_primary_container": "#001D36",

    "m3_secondary": "#535F70",
    "m3_on_secondary": "#FFFFFF",
    "m3_secondary_container": "#D7E3F7",
    "m3_on_secondary_container": "#101C2B",

    "m3_tertiary": "#6B5778",
    "m3_on_tertiary": "#FFFFFF",
    "m3_tertiary_container": "#F2DAFF",
    "m3_on_tertiary_container": "#251431",

    "m3_error": "#BA1A1A",
    "m3_on_error": "#FFFFFF",
    "m3_error_container": "#FFDAD6",
    "m3_on_error_container": "#410002",

    "m3_background": "#FCFCFF",
    "m3_on_background": "#1A1C1E",
    "m3_surface": "#FCFCFF",
    "m3_on_surface": "#1A1C1E",
    "m3_surface_variant": "#DFE2EB",
    "m3_on_surface_variant": "#43474E",
    "m3_outline": "#73777F",
    "m3_outline_variant": "#C3C7CF",
    "m3_inverse_surface": "#2F3033",
    "m3_inverse_on_surface": "#F1F0F4",
    "m3_inverse_primary": "#9ECAFF",

    "ic_launcher_background": "#050B18",

    # Cores herdadas usadas pelo código da base
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

for name, value in light_palette.items():
    s = upsert_color(s, name, value)

colors_light.write_text(s)
print("colors.xml atualizado com tokens Material 3")

# Paleta Material 3 escura
colors_night = Path("app/src/main/res/values-night/colors.xml")
s = ensure_resources_file(colors_night)

dark_palette = {
    "m3_primary": "#9ECAFF",
    "m3_on_primary": "#003258",
    "m3_primary_container": "#00497D",
    "m3_on_primary_container": "#D1E4FF",

    "m3_secondary": "#BBC7DB",
    "m3_on_secondary": "#253140",
    "m3_secondary_container": "#3B4858",
    "m3_on_secondary_container": "#D7E3F7",

    "m3_tertiary": "#D6BEE4",
    "m3_on_tertiary": "#3B2948",
    "m3_tertiary_container": "#523F5F",
    "m3_on_tertiary_container": "#F2DAFF",

    "m3_error": "#FFB4AB",
    "m3_on_error": "#690005",
    "m3_error_container": "#93000A",
    "m3_on_error_container": "#FFDAD6",

    "m3_background": "#111318",
    "m3_on_background": "#E2E2E9",
    "m3_surface": "#111318",
    "m3_on_surface": "#E2E2E9",
    "m3_surface_variant": "#43474E",
    "m3_on_surface_variant": "#C3C7CF",
    "m3_outline": "#8D9199",
    "m3_outline_variant": "#43474E",
    "m3_inverse_surface": "#E2E2E9",
    "m3_inverse_on_surface": "#2F3033",
    "m3_inverse_primary": "#0061A4",
}

for name, value in dark_palette.items():
    s = upsert_color(s, name, value)

colors_night.write_text(s)
print("values-night/colors.xml atualizado com tokens Material 3 dark")

# Remover arquivo duplicado problemático
dup = Path("app/src/main/res/values/ic_launcher_background.xml")
if dup.exists():
    dup.unlink()
    print("ic_launcher_background.xml duplicado removido")

def upsert_style_file(path: Path, theme_name: str, light: bool):
    xml = ensure_resources_file(path)

    light_status = "true" if light else "false"
    light_nav = "true" if light else "false"

    style = f'''    <style name="{theme_name}" parent="Theme.Material3.DayNight.NoActionBar">
        <item name="colorPrimary">@color/m3_primary</item>
        <item name="colorOnPrimary">@color/m3_on_primary</item>
        <item name="colorPrimaryContainer">@color/m3_primary_container</item>
        <item name="colorOnPrimaryContainer">@color/m3_on_primary_container</item>

        <item name="colorSecondary">@color/m3_secondary</item>
        <item name="colorOnSecondary">@color/m3_on_secondary</item>
        <item name="colorSecondaryContainer">@color/m3_secondary_container</item>
        <item name="colorOnSecondaryContainer">@color/m3_on_secondary_container</item>

        <item name="colorTertiary">@color/m3_tertiary</item>
        <item name="colorOnTertiary">@color/m3_on_tertiary</item>
        <item name="colorTertiaryContainer">@color/m3_tertiary_container</item>
        <item name="colorOnTertiaryContainer">@color/m3_on_tertiary_container</item>

        <item name="colorError">@color/m3_error</item>
        <item name="colorOnError">@color/m3_on_error</item>
        <item name="colorErrorContainer">@color/m3_error_container</item>
        <item name="colorOnErrorContainer">@color/m3_on_error_container</item>

        <item name="android:windowBackground">@color/m3_background</item>
        <item name="colorSurface">@color/m3_surface</item>
        <item name="colorOnSurface">@color/m3_on_surface</item>
        <item name="colorSurfaceVariant">@color/m3_surface_variant</item>
        <item name="colorOnSurfaceVariant">@color/m3_on_surface_variant</item>
        <item name="colorOutline">@color/m3_outline</item>

        <item name="android:statusBarColor">@color/m3_surface</item>
        <item name="android:navigationBarColor">@color/m3_surface</item>
        <item name="android:windowLightStatusBar">{light_status}</item>
        <item name="android:windowLightNavigationBar">{light_nav}</item>

        <item name="android:fontFamily">sans</item>
        <item name="android:windowNoTitle">true</item>
        <item name="windowNoTitle">true</item>
        <item name="windowActionBar">false</item>
    </style>
'''

    pattern = rf'\s*<style\s+name="{re.escape(theme_name)}"[^>]*>.*?</style>'
    if re.search(pattern, xml, flags=re.S):
        xml = re.sub(pattern, "\n" + style, xml, flags=re.S)
    else:
        xml = xml.replace("</resources>", style + "</resources>")

    path.write_text(xml)

# Atualizar styles.xml e styles-night.xml
upsert_style_file(Path("app/src/main/res/values/styles.xml"), theme_name, light=True)
upsert_style_file(Path("app/src/main/res/values-night/styles.xml"), theme_name, light=False)

print("styles.xml e styles-night.xml atualizados para Theme.Material3.DayNight.NoActionBar")

# Atualizar versão
if gradle.exists():
    s = gradle.read_text()
    s = re.sub(r'versionCode\s+\d+', 'versionCode 3', s)
    s = re.sub(r'versionName\s+"[^"]+"', 'versionName "0.2.1-m3skin"', s)
    gradle.write_text(s)
    print("Versão atualizada para 0.2.1-m3skin")

# Documentação
notes = Path("docs/releases/SPRINT_05B_MATERIAL3_SKIN.md")
notes.write_text("""# Aetheris Sprint 05B — Material 3 Skin Base

## Objetivo

Aplicar uma skin baseada em Material Design 3 Android usando Theme.Material3, tokens de cor e superfície oficiais do Material Components.

## Alterações

- Tema principal migrado para Theme.Material3.DayNight.NoActionBar.
- Tokens de cor Material 3 adicionados.
- Paleta light/dark criada com values e values-night.
- Status bar e navigation bar alinhadas à superfície do tema.
- Cores herdadas red/pink/purple/blue/teal/green/lime/yellow/orange/brown/grey preservadas para compatibilidade.
- Arquivo duplicado ic_launcher_background.xml removido.
- Versão ajustada para 0.2.1-m3skin.

## O que esta Sprint não altera

- Motor de navegação.
- Abas.
- Favoritos.
- Histórico.
- Downloads.
- Permissões.
- WebRTC.
- Extensões.
- Filtro de câmera.

## Checklist de teste

- [ ] APK instala.
- [ ] Nome continua Aetheris.
- [ ] App abre sem crash.
- [ ] Home/página inicial carrega.
- [ ] Menu principal abre.
- [ ] Menu está visualmente mais próximo de Material 3.
- [ ] Barra inferior continua funcionando.
- [ ] Abas funcionam.
- [ ] Favoritos funcionam.
- [ ] Downloads funcionam.
- [ ] Configurações abrem.
- [ ] Tema escuro continua legível.

## Observação

Esta Sprint aplica a base visual via tema Android XML. A refatoração de cada tela para componentes Material 3 específicos será feita em etapas seguintes.
""")

print("Documentação Sprint 05B criada")
print("Sprint 05B aplicada com sucesso.")
