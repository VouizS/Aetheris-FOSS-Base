# Aetheris Sprint 05B — Material 3 Skin Base

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
