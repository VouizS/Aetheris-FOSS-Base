from pathlib import Path
import re

print("Aplicando Sprint 05A — Aetheris Identity Test")

# 1) Atualizar nome do app
strings = Path("app/src/main/res/values/strings.xml")
if strings.exists():
    s = strings.read_text()

    if 'name="app_name"' in s:
        s = re.sub(
            r'<string name="app_name">.*?</string>',
            '<string name="app_name">Aetheris</string>',
            s
        )
    else:
        s = s.replace("</resources>", '    <string name="app_name">Aetheris</string>\n</resources>')

    s = s.replace("FOSS Browser", "Aetheris")
    s = s.replace("FOSS", "Aetheris")
    strings.write_text(s)
    print("strings.xml atualizado")

# 2) Atualizar versão da build piloto
gradle = Path("app/build.gradle")
if gradle.exists():
    s = gradle.read_text()

    s = re.sub(r'versionCode\s+\d+', 'versionCode 2', s)
    s = re.sub(r'versionName\s+"[^"]+"', 'versionName "0.2.0-pilot"', s)

    gradle.write_text(s)
    print("app/build.gradle atualizado para versão 0.2.0-pilot")

# 3) Garantir cores Aetheris e cores usadas pelo código
colors = Path("app/src/main/res/values/colors.xml")
if colors.exists():
    s = colors.read_text()

    palette = {
        "aetheris_bg": "#050B18",
        "aetheris_surface": "#0B1224",
        "aetheris_primary": "#35D8FF",
        "aetheris_secondary": "#7C4DFF",
        "aetheris_accent": "#00E5FF",
        "aetheris_text": "#EAF7FF",

        # Cores esperadas por partes herdadas da base
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

    insert = ""
    for name, value in palette.items():
        if f'name="{name}"' not in s:
            insert += f'    <color name="{name}">{value}</color>\n'

    if insert:
        s = s.replace("</resources>", insert + "</resources>")

    # Mantém launcher background único
    s = re.sub(
        r'<color name="ic_launcher_background">.*?</color>',
        '<color name="ic_launcher_background">#050B18</color>',
        s
    )

    colors.write_text(s)
    print("colors.xml atualizado")

# 4) Garantir que não volte o arquivo duplicado
dup = Path("app/src/main/res/values/ic_launcher_background.xml")
if dup.exists():
    dup.unlink()
    print("Arquivo duplicado ic_launcher_background.xml removido")

# 5) Atualizar metadados se existirem
for p in [
    Path("fastlane/metadata/android/en-US/title.txt"),
    Path("fastlane/metadata/android/pt-BR/title.txt"),
]:
    if p.exists():
        p.write_text("Aetheris\n")
        print("metadata title atualizado:", p)

# 6) Criar documentação da Sprint
notes = Path("docs/releases/SPRINT_05A_IDENTITY_TEST.md")
notes.write_text("""# Aetheris Sprint 05A — Identity Test

## Objetivo

Aplicar a primeira camada de identidade Aetheris na base FOSS aprovada como piloto.

## Alterações

- Nome visual do app ajustado para Aetheris.
- Versão de teste ajustada para 0.2.0-pilot.
- Paleta base Aetheris adicionada.
- Cores herdadas necessárias preservadas para evitar erro de build.
- Arquivo duplicado de launcher background removido.
- Metadados básicos atualizados quando disponíveis.

## O que esta Sprint NÃO altera

- Motor do navegador.
- Abas.
- Histórico.
- Downloads.
- Favoritos.
- Permissões.
- WebView/WebRTC.
- Regras de privacidade.
- Fluxo de navegação.

## Checklist de teste

- [ ] APK instala.
- [ ] Nome aparece como Aetheris.
- [ ] App abre sem crash.
- [ ] Página inicial carrega.
- [ ] Campo de busca funciona.
- [ ] Abas funcionam.
- [ ] Favoritos funcionam.
- [ ] Histórico funciona.
- [ ] Downloads funcionam.
- [ ] Configurações abrem.
- [ ] Sites com vídeo carregam.
- [ ] Sites que pedem câmera/microfone pedem permissão corretamente.

## Observação legal

A interface principal pode usar a marca Aetheris, mas os créditos open source devem permanecer em área de licenças/créditos.
""")
print("Documentação da Sprint criada")

print("Sprint 05A aplicada com sucesso.")
