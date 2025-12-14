# Repository Documentation Policy

## Preamble

Documentation is a communication strategy. In the Agile hierarchy of effective
knowledge transfer, documentation comes dead last. It is vital, though, as a
reference and to support the other strategies such as face-to-face meetings,
remote video meetings, online training, and so forth.

## Policy

In order to make documentation as easy to understand as possible, it must be
clear, concise, entertaining (yes), and easy on the eyes. For the sake of
professionalism, spell checking must be used. This repository uses Canadian
standards, which always seems to be a mix of European and American preferences.
In this case, British spelling with U.S. punctuation[^1].

### Architecture

Documentation will be stored and accessible in accordance with Information
Architecture theory in Morville2011[^2].

### Clarity

For documents meant for the general public, the writer is encouraged to write
plain english. To assist the writer, they should aim for Flesch reading score 60
to 70 or Flesch-Kincaid U.S. 8th grade.

For engineering documentation, the writer should aim for no lower that Flesch
reading score 50, i.e. grade 12.

In both cases, use the score as a guide, but do not chase it. As Orwell wrote,
"Break any of these rules sooner than say anything outright barbarous."[^3]. You
may wish to read Orwell's thoughts on effective writing as a guide.

#### Automatic Document Checking

I use _hunspell_ with both the "en-ca" dictionary and my own "controlled
vocabulary" (see Morville2001[^2]). In addition, I use
[py-readability-metrics](https://pypi.org/project/py-readability-metrics/) for
readability.

As for markdown documents, I use vanilla
[Marksman](https://github.com/artempyanykh/marksman) for _nvim_,
and David Anson's [markdownlint](https://github.com/DavidAnson/markdownlint) on
Visual Studio Code.

### Conciseness

Stick to the facts. This seems at first glance to fly in the face of
_entertainment_, but one can be concise while making documentation a joy to
read. You may wish to read
[Orwell1946](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/)[^3] for additional guidance.

### Entertainment

After making mistakes, the second way someone retains lessons is through an
emotional memory. Make 'em laugh, make 'em cry. Keep it professional.

### Easy on the Eyes

- Use technical writing skills to break up long sentences, format lists,
  and emphasize points. I refer to Pringle2009[^4] as I am a perpetual
  beginner.
- For page displays, make good decisions for white space, fonts, kerning,
  spacing, and so forth. I am personally a fan of
  [Butterick2018](https://typographyforlawyers.com/)[^5].

______________________________________________________________________

[^1]: Public Works and Government Services Canada, _The Canadian Style: A
      Guide to Writing and Editing_, rev. ed. Dundurn Press, 1997.

[^2]: Peter Morville and Louis Rosenfeld, _Information Architecture for the World
     Wide Web_. O'Reilly Media, 2011.

[^3]: Orwell, George. _Politics and the English Language_. Penguin Classics,
      2013.

[^4]: Pringle, Alan. _Technical Writing 101: A Real-World Guide to Planning and
      Writing Technical Content_. Scriptorium, 2009.

[^5]: Butterick, Matthew. _Typography for Lawyers_, 2nd ed. Jones McClure, 2018.
