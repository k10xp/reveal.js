from pathlib import Path
import shutil

if __name__ == "__main__":
    # use set for faster lookups
    include_list = {
        # required
        "cleanup.py",
        "dist",
        "plugin",
        # repo
        ".git",
        ".gitignore",
        "LICENSE",
    }

    base = Path(".")

    for path in base.iterdir():
        if path.name in include_list:
            continue

        # delete files, symlinks, directories
        if path.is_file() or path.is_symlink():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)

    index_html_content = """<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <title>reveal.js</title>

    <link rel="stylesheet" href="dist/reset.css">
    <link rel="stylesheet" href="dist/reveal.css">
    <link rel="stylesheet" href="dist/theme/black.css">

    <link rel="stylesheet" href="plugin/highlight/dracula.css">
</head>

<body>
    <div class="reveal">
        <div class="slides">
            <section>Slide 1</section>
            <section>Slide 2</section>
        </div>
    </div>

    <script src="dist/reveal.js"></script>
    <script src="plugin/notes/notes.js"></script>
    <script src="plugin/markdown/markdown.js"></script>
    <script src="plugin/highlight/highlight.js"></script>
    <script>
        Reveal.initialize({
            hash: true,
            plugins: [RevealMarkdown, RevealHighlight, RevealNotes]
        });
    </script>
</body>

</html>"""

    Path("index.html").write_text(index_html_content, encoding="utf-8")

    readme_content = """# RevealJS template

```shell
git clone --single-branch --branch template https://github.com/k10xp/reveal.js
```
"""
    Path("README.md").write_text(readme_content, encoding="utf8")
