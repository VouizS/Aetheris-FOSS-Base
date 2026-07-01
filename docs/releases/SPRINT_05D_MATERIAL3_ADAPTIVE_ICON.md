# Aetheris Sprint 05D — Material 3 Adaptive Icon

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
