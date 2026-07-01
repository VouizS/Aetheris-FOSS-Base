# Aetheris WebView FOSS Base — Test Notes

## Purpose

This build tests whether the FOSS Browser open-source base is suitable as the practical WebView foundation for Aetheris.

## Technical profile

- Language: Java
- UI: Android XML Views / Material Components
- Engine: Android WebView
- Build: Gradle Groovy
- License: AGPL-3.0-or-later

## Test application id

`com.aetheris.browser.fossbase`

This allows testing beside the previous Aetheris package without immediately replacing it.

## Included changes

- App name changed to Aetheris.
- Icon changed to Aetheris icon.
- Version changed to `0.1.0-foss-base`.
- GitHub Actions workflow added.
- Main package/namespace kept as `de.baumann.browser` to avoid breaking Java imports in the first test.

## Security notes for testing

Permissions remain mostly as in the original base for this test. When a website requests location, camera, or microphone, the app/browser mediates Android permissions, but the final data may be delivered to the website being used. Do not grant location/camera/microphone to websites you do not trust.

Before public distribution, hardening should remove or restrict broad storage, file URL access, cleartext traffic, and overly broad JavaScript bridge behavior.
