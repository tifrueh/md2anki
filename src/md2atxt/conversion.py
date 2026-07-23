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
