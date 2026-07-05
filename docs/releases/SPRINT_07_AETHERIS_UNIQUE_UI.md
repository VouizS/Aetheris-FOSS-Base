# Aetheris 0.3.0 — Sprint 07 Unique UI

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
