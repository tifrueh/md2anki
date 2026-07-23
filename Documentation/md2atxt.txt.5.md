---
title: "md2atxt.txt"
section: "5"
---

# NAME

md2atxt.txt - md2atxt Anki import file format

# DESCRIPTION

An Anki import file (of the kind used by **md2atxt**(1)) consists of two parts;
a header and a body.

**Header Format**
: The header consists of key-value pairs formatted as "`#key:value`". The two
headers "`separator`" and "`html`" shall always be set, to "`semicolon`" and to
"`true`", respectively. This is to make sure that the body is interpreted
correctly.

**Body Format**
: The body follows after the header and is a concatenation of one or more Anki
line files (see **md2atxt.al**(5)), separated by a newline character.

  Note that while it is not technically incorrect to link Anki line files with
  an inconsistent number of fields into a single Anki import file, doing this is
  discouraged due to the way Anki handles such files. See the Anki documentation
  for reference.

Also note that a file of this format is also exactly what the link stage of
**md2atxt**(1) produces if applied to one or more Anki line files.

# NOTES

For the full documentation of the import file format used by Anki, see

<https://docs.ankiweb.net/importing/text-files.html>

# EXAMPLE

The approximate Anki import file linked from the Anki line file given as example
in **md2atxt.al**(5) (and another one in interest of a more expressive example)
would look as follows:

```csv
#separator:semicolon
#html:true
"foo";"<h2>What is a bar?</h2>";"<p>A bar is usually a baz.</p>"
"bar";"<h2>What is a baz?</h2>";"<p>A baz is usually a bar.</p>"
```

# SEE ALSO

**pandoc**(1), **md2atxt**(1), **md2atxt.md**(5), **md2atxt.al**(5)
