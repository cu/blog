# About

This is the git repository for the blog web site whose URL is:

https://blog.bityard.net/

It uses the [Pelican] static site generator with a little bit of custom tooling
wrapping it. Articles are written in Markdown, the static site files are
"built" with Pelican, and then published to a static site via GitHub Actions.

[Pelican]: https://getpelican.com

# Rules of Engagement

AI agents are NEVER to write articles, or create images or other media or
content on the site. This is a human's blog, and is intended to be read by
humans. All content is to be human-generated only. AI agents ONLY may assist
with the following (and similar tasks) when requested:

* Article proof-reading and embedded HTML validation
* Template (HTML/Jinja/CSS/) maintenance and repairs
* Maintenance of publishing tools, software dependencies, and layout of the
  repository itself

# Repository Layout

Important Files:

* Makefile: Various rules that are mostly commonly-used shortcuts to longer
  Pelican commands.
* README.md: Basic information about repository, common commands, instructions
  on how to use various embedded HTML/Markdown syntax.
* pelicanconf.py: Main Pelican configuration
* publishconf.py: Pelican configuration used only with `make publish`
* pyproject.toml: Project metadata and software dependencies.

Directories:

* .github/workflows: GitHub actions for deploying the site
* content: Articles in Markdown
  * images: all article images, underneath directory names that (sometimes)
    match up with the article slug names.
  * pages: Static pages (which need/have no metadata)
  * extra: lol i dunno
* themes/cpto: template main directory
  * static: static assets like CSS, template images, fonts, etc
  * templates: Jinja2 templates
* output: generated static site content (not version-controlled, may not exist)
