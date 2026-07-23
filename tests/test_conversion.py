import md2atxt.conversion as module

test_convert_string_in = """# Testfile
Some more **text** here.
"""

test_convert_string_out = """<h1 id="testfile">Testfile</h1>
<p>Some more <strong>text</strong> here.</p>
"""

def test_convert_string():
    result = module.convert_string(test_convert_string_in)
    assert result == test_convert_string_out

test_parse_file_string_in = """+++
title = "thisisatitle"
noteid = "foo"
+++

## What is a bar?

<!-- || -->

A bar is usually a baz.

<!-- || -->

There's a second part here.

<!-- || -->

And a third.
"""

test_parse_file_string_out = {
    "toml": "title = \"thisisatitle\"\nnoteid = \"foo\"",
    "md": [
        "## What is a bar?",
        "A bar is usually a baz.",
        "There's a second part here.",
        "And a third.",
    ]
}

def test_parse_file_string():
    result = module.parse_file_string(test_parse_file_string_in)
    assert result == test_parse_file_string_out
