from pathlib import Path
import re

print("Aplicando Sprint 05D — Material 3 Adaptive Icon")

# 1) Garantir cor de fundo no colors.xml sem criar arquivo duplicado
colors = Path("app/src/main/res/values/colors.xml")
if not colors.exists():
    colors.parent.mkdir(parents=True, exist_ok=True)
    colors.write_text("<resources>\n</resources>\n")

s = colors.read_text()

def upsert_color(xml, name, value):
    pattern = rf'<color name="{re.escape(name)}">.*?</color>'
    replacement = f'<color name="{name}">{value}</color>'
    if re.search(pattern, xml):
        return re.sub(pattern, replacement, xml)
    return xml.replace("</resources>", f"    {replacement}\n</resources>")

s = upsert_color(s, "ic_launcher_background", "#101820")
s = upsert_color(s, "aetheris_icon_cyan", "#7DEBFF")
s = upsert_color(s, "aetheris_icon_blue", "#4D8DFF")
s = upsert_color(s, "aetheris_icon_purple", "#B69CFF")
s = upsert_color(s, "aetheris_icon_white", "#F8FAFF")
colors.write_text(s)
print("colors.xml atualizado com cores do ícone")

# 2) Remover arquivo duplicado antigo se existir
dup = Path("app/src/main/res/values/ic_launcher_background.xml")
if dup.exists():
    dup.unlink()
    print("Removido arquivo duplicado:", dup)

# 3) Foreground vetorial Material 3 / Aetheris
Path("app/src/main/res/drawable/ic_aetheris_foreground.xml").write_text("""<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">

    <path
        android:fillColor="@android:color/transparent"
        android:strokeColor="@color/aetheris_icon_blue"
        android:strokeWidth="2.4"
        android:strokeAlpha="0.45"
        android:pathData="M18,54C30,30 72,20 90,44C73,41 51,49 33,69C27,66 22,61 18,54Z" />

    <path
        android:fillColor="@color/aetheris_icon_cyan"
        android:fillAlpha="0.95"
        android:pathData="M31,78L53,25C56,19 64,18 69,23L84,38C76,36 68,39 63,46L46,82C42,91 28,88 31,78Z" />

    <path
        android:fillColor="@color/aetheris_icon_blue"
        android:fillAlpha="0.96"
        android:pathData="M55,27L83,77C87,85 76,93 69,86L46,62L55,27Z" />

    <path
        android:fillColor="@color/aetheris_icon_purple"
        android:fillAlpha="0.88"
        android:pathData="M64,59L86,85C90,90 83,98 77,94L58,80L64,59Z" />

    <path
        android:fillColor="@android:color/transparent"
        android:strokeColor="@color/aetheris_icon_cyan"
        android:strokeWidth="5"
        android:strokeLineCap="round"
        android:strokeAlpha="0.95"
        android:pathData="M19,66C36,75 67,73 91,55" />

    <path
        android:fillColor="@android:color/transparent"
        android:strokeColor="@color/aetheris_icon_blue"
        android:strokeWidth="3"
        android:strokeLineCap="round"
        android:strokeAlpha="0.75"
        android:pathData="M25,70C45,82 76,78 94,60" />

    <path
        android:fillColor="@color/aetheris_icon_white"
        android:fillAlpha="0.82"
        android:pathData="M55,26L62,28L45,72L40,76Z" />

    <path
        android:fillColor="@color/aetheris_icon_white"
        android:fillAlpha="0.60"
        android:pathData="M66,39L78,45L69,47Z" />
</vector>
""")

print("Foreground vetorial criado")

# 4) Monochrome icon para Android 13+ themed icons
Path("app/src/main/res/drawable/ic_aetheris_monochrome.xml").write_text("""<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">

    <path
        android:fillColor="#FFFFFFFF"
        android:pathData="M31,78L53,25C56,19 64,18 69,23L84,38C76,36 68,39 63,46L46,82C42,91 28,88 31,78Z" />

    <path
        android:fillColor="#FFFFFFFF"
        android:pathData="M55,27L83,77C87,85 76,93 69,86L46,62L55,27Z" />

    <path
        android:fillColor="#FFFFFFFF"
        android:pathData="M64,59L86,85C90,90 83,98 77,94L58,80L64,59Z" />

    <path
        android:fillColor="@android:color/transparent"
        android:strokeColor="#FFFFFFFF"
        android:strokeWidth="5"
        android:strokeLineCap="round"
        android:pathData="M19,66C36,75 67,73 91,55" />
</vector>
""")

print("Ícone monocromático criado")

# 5) Adaptive icons
adaptive = """<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_aetheris_foreground" />
    <monochrome android:drawable="@drawable/ic_aetheris_monochrome" />
</adaptive-icon>
"""

Path("app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml").write_text(adaptive)
Path("app/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml").write_text(adaptive)

print("Adaptive icons atualizados")

# 6) Manifest: garantir icon/roundIcon
manifest = Path("app/src/main/AndroidManifest.xml")
if manifest.exists():
    ms = manifest.read_text()

    if 'android:icon=' in ms:
        ms = re.sub(r'android:icon="@[^"]+"', 'android:icon="@mipmap/ic_launcher"', ms)
    else:
        ms = ms.replace("<application", '<application android:icon="@mipmap/ic_launcher"', 1)

    if 'android:roundIcon=' in ms:
        ms = re.sub(r'android:roundIcon="@[^"]+"', 'android:roundIcon="@mipmap/ic_launcher_round"', ms)
    else:
        ms = ms.replace("<application", '<application android:roundIcon="@mipmap/ic_launcher_round"', 1)

    manifest.write_text(ms)
    print("Manifest atualizado com ícones do Aetheris")

# 7) Atualizar versão
gradle_paths = [Path("app/build.gradle"), Path("app/build.gradle.kts")]
for gradle in gradle_paths:
    if gradle.exists():
        gs = gradle.read_text()
        gs = re.sub(r'versionCode\\s+\\d+', 'versionCode 6', gs)
        gs = re.sub(r'versionCode\\s*=\\s*\\d+', 'versionCode = 6', gs)
        gs = re.sub(r'versionName\\s+"[^"]+"', 'versionName "0.2.3-m3icon"', gs)
        gs = re.sub(r'versionName\\s*=\\s*"[^"]+"', 'versionName = "0.2.3-m3icon"', gs)
        gradle.write_text(gs)
        print("Versão atualizada em:", gradle)

# 8) Documentação
notes = Path("docs/releases/SPRINT_05D_MATERIAL3_ADAPTIVE_ICON.md")
notes.write_text("""# Aetheris Sprint 05D — Material 3 Adaptive Icon

## Objetivo

Atualizar o ícone do APK para uma identidade visual moderna, adaptativa e coerente com Material Design 3 Android.

## Alterações

- Criado foreground vetorial próprio do Aetheris.
- Criado ícone adaptativo em `mipmap-anydpi-v26/ic_launcher.xml`.
- Criado ícone adaptativo round em `mipmap-anydpi-v26/ic_launcher_round.xml`.
- Criado ícone monocromático para Android themed icons.
- Mantida a cor `ic_launcher_background` somente em `colors.xml`.
- Removido `values/ic_launcher_background.xml` se existir, para evitar erro de recurso duplicado.
- Manifest atualizado para usar `@mipmap/ic_launcher` e `@mipmap/ic_launcher_round`.
- Versão atualizada para `0.2.3-m3icon`.

## Não alterado

- Motor WebView.
- Abas.
- Favoritos.
- Histórico.
- Downloads.
- Permissões.
- Configurações.
- Componentes internos do navegador.

## Checklist de teste

- [ ] APK compila.
- [ ] APK instala.
- [ ] Ícone aparece no launcher.
- [ ] Ícone aparece na tela de apps recentes.
- [ ] Ícone aparece nas informações do aplicativo.
- [ ] Nome continua Aetheris.
- [ ] App abre sem crash.
""")

print("Sprint 05D aplicada com sucesso.")
