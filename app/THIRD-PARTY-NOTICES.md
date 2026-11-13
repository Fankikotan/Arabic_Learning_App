# Third-party dictionary attribution

The built-in Arabic–English lookup dataset is derived from English Wiktionary contributors via Kaikki / Wiktextract.

- Dataset page: https://kaikki.org/dictionary/Arabic/index.html
- Download used: https://kaikki.org/dictionary/Arabic/kaikki.org-dictionary-Arabic.jsonl.gz
- Wiktionary: https://en.wiktionary.org/ (individual headword/history pages linked in lookup)
- Text license: Creative Commons Attribution-ShareAlike 4.0 International, https://creativecommons.org/licenses/by-sa/4.0/
- Copyright information: https://en.wiktionary.org/wiki/Wiktionary:Copyrights
- Processing date: 2026-11-13. The local downloaded snapshot contains 233,417 records before filtering. This is a snapshot, not a claim to mirror all current Wiktionary entries.
- Local modifications: retained Arabic headwords, English glosses, part of speech, form-of and inflection links; removed media and unrelated fields; normalized diacritics for search; merged matching keys and limited displayed senses.
- Extracted dictionary text and modified dictionary data remain available under CC BY-SA 4.0. Preserve attribution, license link and modification notice when redistributing. The application source code is a separate work; no blanket source-code license has been selected yet.
- Media from Wiktionary/Commons is not included. The dictionary has no bundled pronunciation audio.

Extraction software: Tatu Ylonen and Wiktextract contributors, https://github.com/tatuylonen/wiktextract . The code license of the extractor does not replace the dictionary content license.

## Learning content

The textbook is newly authored educational content. The fisherman story is a simplified original Arabic retelling of the traditional Fisherman and the Jinni plot, with Chinese translations and original AI-generated cover art. Plot reference: https://www.gutenberg.org/files/20916/20916-h/20916-h.htm . It is not a quotation from a modern Arabic/Chinese translation.

Learning audio is synthesized (not a human recording) with the ar-SA-HamedNeural voice through Edge TTS. Word timestamps use the service's WordBoundary metadata; independent vocabulary pronunciations are separately synthesized. These audio assets are not part of the Wiktionary license. Before public distribution, the generated audio service's applicable output/reuse terms must be reviewed; this repository does not assert that third-party voice rights are unrestricted.

The Edge TTS utility is a separate dependency: https://github.com/rany2/edge-tts . It is used at material-authoring time, not required on the phone.


## Capacitor browser runtime

app/capacitor-runtime.js is distributed from @capacitor/core 8.6.2. Source: https://github.com/ionic-team/capacitor . License follows:

```text
MIT License

Copyright (c) 2017-present Drifty Co.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
