import subprocess
import re

# ==============================================================================
# = CUSTOM ERROR TYPES =========================================================
class ParseException(Exception):
    pass

# ==============================================================================
# = GLOBALS ====================================================================

FILE_RES=r"^\+\+\+\s*(?P<toml>.*?)\s*\+\+\+\s*(?P<md>.*?)\s*$"
FIELD_RES=r"\s*<!-- \|\| -->\s*"
FILE_RE=re.compile(FILE_RES, re.DOTALL)
FIELD_RE=re.compile(FIELD_RES)

# ==============================================================================
# = FUNCTIONS ==================================================================

def convert_string(md_string):
    """Convert a Markdown string to HTML.

    arguments:
        md_string -- The Markdown string to convert.

    return:
        A string containing the converted HTML.
    """

    result = subprocess.run(
        [ "pandoc", "-f", "markdown", "-t", "html" ],
        input=md_string,
        capture_output=True,
        text=True
    )

    return result.stdout

def parse_file_string(file_string):
    """Parse a Markdown string read from a file into a dictionary structure.

    arguments:
        file_string -- The Markdown string to parse.

    return:
        A dictionary of the following form:
        {
            "toml": "string"     // The TOML metadata header.,
            "md":   [ "string" ] // A list of strings, each entry containing
                                 // one field of the parsed file.
        }
    """

    match = FILE_RE.match(file_string)

    if not match:
        raise ParseException("File string did not parse.")

    result = match.groupdict()
    result["md"] = FIELD_RE.split(result["md"])

    return result


def convert_file(in_file, out_file):
    """Convert a Markdown file to a Anki line file.

    arguments:
        in_file  -- The filename of the file to convert.
        out_file -- The filename of the file to write to.

    returns:
        None
    """

    log.info(f"Converting {in_file} -> {out_file}")

    # Read file into data structure.
    with open(in_file) as file:
        file_str = file.read()
        data_dict = parse_file_string(file_str)

    return None


def convert(args, log):
    """Run the conversion stage based upon some parsed arguments.

    arguments:
        args -- The parsed arguments object (as returned by parse_args()).
        log  -- The logger object with which to produce log messages.

    return:
        None, but note that this function will modify the 'args.in_file' field
        to the list of /output/ files it produces, so that a potential link
        phase can be run directly afterwards on the same 'args' object.
    """

    log.info("Running conversion stage …")
