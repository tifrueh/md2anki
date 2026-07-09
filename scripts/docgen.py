from hatchling.builders.hooks.plugin.interface import BuildHookInterface

import subprocess
from pathlib import Path
from datetime import datetime

class DocGenBuildHook(BuildHookInterface):

    def initialize(self, version, build_data):

        doc_path = Path(self.root + "/Documentation")
        md_paths = doc_path.glob("*.md")
        today = datetime.today().strftime('%Y-%m-%d')

        for md_path in md_paths:

            man_path = md_path.with_suffix("")

            subprocess.run(
                [
                    "pandoc",
                    "--from=markdown",
                    "--standalone",
                    "--variable",
                    f"footer=v{str(self.metadata.version)}",
                    "--variable",
                    f"date={str(today)}",
                    "--to=man",
                    str(md_path),
                    "-o",
                    str(man_path),
                ],
                check=True,
        )

    def clean(self, versions):

        doc_path = Path(self.root + "/Documentation")
        md_paths = doc_path.glob("*.md")

        for md_path in md_paths:
            man_path = md_path.with_suffix("")
            man_path.unlink(missing_ok=True)
