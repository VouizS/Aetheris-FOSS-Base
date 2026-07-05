from pathlib import Path
import re

print("Aplicando Aetheris 0.3.0 — Sprint 07 Unique UI")

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def write(path, content):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)

# ------------------------------------------------------------
# Colors
# ------------------------------------------------------------

colors = Path("app/src/main/res/values/colors.xml")
if not colors.exists():
    colors.parent.mkdir(parents=True, exist_ok=True)
    colors.write_text("<resources>\n</resources>\n")

s = colors.read_text(errors="ignore")

def upsert_color(xml, name, value):
    pattern = rf'<color name="{re.escape(name)}">.*?</color>'
    item = f'<color name="{name}">{value}</color>'
    if re.search(pattern, xml):
        return re.sub(pattern, item, xml)
    return xml.replace("</resources>", f"    {item}\n</resources>")

palette = {
    "aetheris_void": "#050914",
    "aetheris_deep": "#07101F",
    "aetheris_panel": "#0B1628",
    "aetheris_panel_soft": "#101D33",
    "aetheris_panel_high": "#152845",
    "aetheris_orbit": "#42E8FF",
    "aetheris_orbit_soft": "#7DEBFF",
    "aetheris_nebula": "#5A7CFF",
    "aetheris_lumen": "#B69CFF",
    "aetheris_text": "#F6FAFF",
    "aetheris_text_soft": "#B8C7DA",
    "aetheris_line": "#28496C",
    "aetheris_success": "#53E6A4",
    "aetheris_warning": "#FFD166",
    "aetheris_error": "#FF6B81",
    "ic_launcher_background": "#050B18",
    "colorPrimary": "#5A7CFF",
    "colorPrimaryDark": "#050914",
    "colorAccent": "#42E8FF",
    "colorControlNormal": "#B8C7DA",
    "colorControlActivated": "#42E8FF",
    "colorBackground": "#050914",
    "colorSurface": "#0B1628",
    "colorOnSurface": "#F6FAFF",
    "m3_primary": "#42E8FF",
    "m3_onPrimary": "#00131A",
    "m3_primaryContainer": "#152845",
    "m3_onPrimaryContainer": "#D7F8FF",
    "m3_secondary": "#B69CFF",
    "m3_onSecondary": "#16002E",
    "m3_surface": "#0B1628",
    "m3_surfaceVariant": "#152845",
    "m3_background": "#050914",
    "m3_onSurface": "#F6FAFF",
    "m3_onSurfaceVariant": "#B8C7DA",
    "m3_outline": "#28496C",
}

for k, v in palette.items():
    s = upsert_color(s, k, v)

colors.write_text(s)
print("✓ Paleta Aetheris atualizada")

# Known duplicate safety
for dup in [Path("app/src/main/res/values/ic_launcher_background.xml")]:
    if dup.exists():
        dup.unlink()
        print("✓ Removido duplicado:", dup)

# ------------------------------------------------------------
# Drawables
# ------------------------------------------------------------

write("app/src/main/res/drawable/aetheris_screen_background.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient
        android:startColor="@color/aetheris_void"
        android:centerColor="@color/aetheris_deep"
        android:endColor="@color/aetheris_panel"
        android:angle="315" />
</shape>
""")

write("app/src/main/res/drawable/aetheris_panel_background.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/aetheris_panel" />
    <corners android:radius="24dp" />
    <stroke android:width="1dp" android:color="@color/aetheris_line" />
    <padding android:left="12dp" android:top="10dp" android:right="12dp" android:bottom="10dp" />
</shape>
""")

write("app/src/main/res/drawable/aetheris_card_background.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/aetheris_panel_soft" />
    <corners android:radius="22dp" />
    <stroke android:width="1dp" android:color="@color/aetheris_line" />
    <padding android:left="14dp" android:top="12dp" android:right="14dp" android:bottom="12dp" />
</shape>
""")

write("app/src/main/res/drawable/aetheris_input_background.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/aetheris_panel_high" />
    <corners android:radius="28dp" />
    <stroke android:width="1dp" android:color="@color/aetheris_orbit" />
    <padding android:left="18dp" android:top="10dp" android:right="18dp" android:bottom="10dp" />
</shape>
""")

write("app/src/main/res/drawable/aetheris_button_primary.xml", """<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_pressed="true">
        <shape>
            <solid android:color="@color/aetheris_lumen" />
            <corners android:radius="22dp" />
        </shape>
    </item>
    <item>
        <shape>
            <gradient android:startColor="@color/aetheris_orbit" android:endColor="@color/aetheris_nebula" android:angle="0" />
            <corners android:radius="22dp" />
        </shape>
    </item>
</selector>
""")

write("app/src/main/res/drawable/aetheris_button_ghost.xml", """<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_pressed="true">
        <shape>
            <solid android:color="@color/aetheris_panel_high" />
            <corners android:radius="22dp" />
            <stroke android:width="1dp" android:color="@color/aetheris_orbit" />
        </shape>
    </item>
    <item>
        <shape>
            <solid android:color="@color/aetheris_panel" />
            <corners android:radius="22dp" />
            <stroke android:width="1dp" android:color="@color/aetheris_line" />
        </shape>
    </item>
</selector>
""")

write("app/src/main/res/drawable/aetheris_bottom_bar_background.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/aetheris_panel" />
    <corners android:topLeftRadius="28dp" android:topRightRadius="28dp" android:bottomLeftRadius="0dp" android:bottomRightRadius="0dp" />
    <stroke android:width="1dp" android:color="@color/aetheris_line" />
</shape>
""")

write("app/src/main/res/drawable/aetheris_dialog_background.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/aetheris_panel_soft" />
    <corners android:radius="26dp" />
    <stroke android:width="1dp" android:color="@color/aetheris_orbit" />
</shape>
""")

print("✓ Drawables Aetheris criados")

# ------------------------------------------------------------
# Runtime helper
# ------------------------------------------------------------

write("app/src/main/java/de/baumann/browser/unit/AetherisUiIdentity.java", """package de.baumann.browser.unit;

import android.app.Activity;
import android.graphics.Color;
import android.os.Build;
import android.view.View;
import android.view.Window;

public final class AetherisUiIdentity {

    private AetherisUiIdentity() {
    }

    public static void apply(Activity activity) {
        if (activity == null) {
            return;
        }

        try {
            Window window = activity.getWindow();

            if (window != null) {
                window.setStatusBarColor(Color.parseColor("#050914"));
                window.setNavigationBarColor(Color.parseColor("#07101F"));

                if (Build.VERSION.SDK_INT >= 23) {
                    View decor = window.getDecorView();
                    if (decor != null) {
                        decor.setSystemUiVisibility(0);
                    }
                }
            }
        } catch (Exception ignored) {
        }
    }
}
""")

patched_activities = []
java_root = Path("app/src/main/java")
if java_root.exists():
    for p in java_root.rglob("*.java"):
        txt = p.read_text(errors="ignore")
        if "AetherisUiIdentity.apply(this)" in txt:
            continue
        if "setContentView(" not in txt:
            continue
        if "extends Activity" not in txt and "extends AppCompatActivity" not in txt and "extends PreferenceActivity" not in txt:
            continue

        lines = txt.splitlines()
        out = []
        inserted = False
        for line in lines:
            out.append(line)
            if not inserted and "setContentView(" in line and ";" in line:
                indent = re.match(r"^(\s*)", line).group(1)
                out.append(indent + "de.baumann.browser.unit.AetherisUiIdentity.apply(this);")
                inserted = True
        if inserted:
            p.write_text("\n".join(out) + "\n")
            patched_activities.append(str(p))

if patched_activities:
    print("✓ Status/navigation bar Aetheris aplicado em Activities")
    for item in patched_activities:
        print("  -", item)
else:
    print("• Nenhuma Activity detectada para injeção runtime")

# ------------------------------------------------------------
# Theme safe attrs
# ------------------------------------------------------------

def patch_theme(path):
    p = Path(path)
    if not p.exists():
        return False
    txt = p.read_text(errors="ignore")
    old = txt

    items = {
        "android:windowBackground": "@color/aetheris_void",
        "android:statusBarColor": "@color/aetheris_void",
        "android:navigationBarColor": "@color/aetheris_deep",
        "android:fontFamily": "sans",
        "colorPrimary": "@color/aetheris_nebula",
        "colorPrimaryDark": "@color/aetheris_void",
        "colorAccent": "@color/aetheris_orbit",
        "colorControlNormal": "@color/aetheris_text_soft",
        "colorControlActivated": "@color/aetheris_orbit",
    }

    for name, value in items.items():
        pattern = rf'<item name="{re.escape(name)}">.*?</item>'
        repl = f'<item name="{name}">{value}</item>'
        if re.search(pattern, txt):
            txt = re.sub(pattern, repl, txt)
        else:
            m = re.search(r'(<style[^>]+name="[^"]*(?:AppTheme|Theme)[^"]*"[^>]*>)', txt)
            if m:
                txt = txt[:m.end()] + f"\n        {repl}" + txt[m.end():]

    if txt != old:
        p.write_text(txt)
        return True
    return False

for theme_file in [
    "app/src/main/res/values/themes.xml",
    "app/src/main/res/values-night/themes.xml",
    "app/src/main/res/values/styles.xml",
    "app/src/main/res/values-night/styles.xml",
]:
    if patch_theme(theme_file):
        print("✓ Tema atualizado:", theme_file)

# ------------------------------------------------------------
# Cautious layout root background
# ------------------------------------------------------------

layout_dir = Path("app/src/main/res/layout")
patched_layouts = []
root_candidates = [
    "LinearLayout",
    "RelativeLayout",
    "FrameLayout",
    "ScrollView",
    "HorizontalScrollView",
    "androidx.constraintlayout.widget.ConstraintLayout",
    "androidx.coordinatorlayout.widget.CoordinatorLayout",
]

if layout_dir.exists():
    for p in layout_dir.rglob("*.xml"):
        txt = p.read_text(errors="ignore")
        old = txt
        head = txt[:700]
        if 'android:background="@drawable/aetheris_screen_background"' in head:
            continue
        if "<merge" in head or "<layout" in head:
            continue
        for tag in root_candidates:
            pattern = rf'(<{re.escape(tag)}\b(?=[^>]*xmlns:android="[^"]+")(?![^>]*android:background=)([^>]*)>)'
            m = re.search(pattern, txt, flags=re.S)
            if m and m.start() < 250:
                original = m.group(1)
                changed = original[:-1] + '\n    android:background="@drawable/aetheris_screen_background">'
                txt = txt[:m.start()] + changed + txt[m.end():]
                break
        if txt != old:
            p.write_text(txt)
            patched_layouts.append(str(p))

print(f"✓ Layouts com fundo Aetheris: {len(patched_layouts)}")

# ------------------------------------------------------------
# Version
# ------------------------------------------------------------

for gradle_name in ["app/build.gradle", "app/build.gradle.kts"]:
    p = Path(gradle_name)
    if p.exists():
        g = p.read_text(errors="ignore")
        old = g
        g = re.sub(r'versionCode\s+\d+', 'versionCode 9', g)
        g = re.sub(r'versionCode\s*=\s*\d+', 'versionCode = 9', g)
        g = re.sub(r'versionName\s+"[^"]+"', 'versionName "0.3.0-uniqueui"', g)
        g = re.sub(r'versionName\s*=\s*"[^"]+"', 'versionName = "0.3.0-uniqueui"', g)
        if g != old:
            p.write_text(g)
            print("✓ Versão atualizada em", gradle_name)

# ------------------------------------------------------------
# Docs
# ------------------------------------------------------------

write("docs/releases/SPRINT_07_AETHERIS_UNIQUE_UI.md", """# Aetheris 0.3.0 — Sprint 07 Unique UI

## Objetivo

Transformar a interface do Aetheris em uma identidade visual própria, deixando de parecer apenas uma base FOSS modificada.

## Direção visual

Aetheris passa a usar uma identidade orbital premium:

- Fundo azul escuro profundo.
- Superfícies em camadas.
- Ciano/azul como cor principal.
- Roxo/lilás como brilho secundário.
- Cards e painéis arredondados.
- Contraste melhor para modo escuro.
- Status bar e navigation bar coerentes com o app.
- Recursos visuais próprios em XML.

## Implementado

- Nova paleta Aetheris no `colors.xml`.
- Novos drawables da identidade Aetheris.
- Helper runtime `AetherisUiIdentity.java`.
- Aplicação de status bar/navigation bar nas Activities detectadas.
- Passagem cautelosa em layouts para fundo visual Aetheris.
- Versionamento atualizado para `0.3.0-uniqueui`.

## Não alterado

- Motor WebView.
- Ícone oficial aprovado.
- Downloads.
- Favoritos.
- Histórico.
- Base de links externos.

## Observação

Esta é a primeira grande virada visual. Alguns componentes antigos podem continuar com aparência herdada caso tenham background hardcoded ou sejam criados por Java em runtime. Esses componentes serão refinados em sprints posteriores.

## Checklist

- [ ] APK compila.
- [ ] APK instala.
- [ ] Ícone oficial continua correto.
- [ ] App abre sem crash.
- [ ] Telas internas usam identidade Aetheris.
- [ ] Barra de status e navegação estão escuras.
- [ ] Navegação básica continua funcionando.
""")

print("Sprint 07 Unique UI aplicada com sucesso.")
