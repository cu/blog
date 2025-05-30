# About

[This is my blog.](https://blog.bityard.net/)

# Development/Preview Environment

This repo uses [uv](https://docs.astral.sh/). If it is not installed, make it
so.

The `Makefile` is set up to run Pelican within a local virtualenv. It has
various interesting targets, some of which are listed below.

To run the Pelican development server:

```
make devserver
```

Publish the site (output HTML to the `content` directory).

```
make publish
```

Get the size of the repo (minus git metadata, output dir, etc)

```
make reposize
```

# Images

Images are generally a maximum of 640 pixels wide.

Easily the most annoying part of writing content for this is handling the images. Oh, markdown has ways of inserting images into a document, but there are "issues" If you want to style article images in some way differently from the other images on the page, good luck because unless you write your own extension, the parser only outputs the barest of plain HTML, which makes writing CSS targeting these images difficult to impossible. (This is totally reasonable behavior on the part of the parser, but is highly inconvenient when using markdown for publishing.)

The markdown parser that Pelican uses (and probably most others) allow for an image to have a title, which most browsers render as a tool-tip when hovering over the image. If you want a caption above or below (which is more useful than a tool-tip), there is no markdown for that, without an extension.

For reference, this is the syntax for inserting an image:

```md
![Alt text](https://example.com/some-image.png "a title")
```

And this is how you would use an image as a link (to another page or image):

```md
[![a x0xb0x]({static}/images/x0x-2/thumb-x0x1-1.JPG)]({static}/images/x0x-2/x0x1-1.JPG "x0xb0x r0x ur s0x")
```

## Markdown image extensions?

[flywire/caption](https://github.com/flywire/caption) looks interesting and _claims_ to do pretty much what I want, but the project is not under very active development and might even be a little broken in its current state. [The rest](https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions) are hacky in various ways.

Someday, I may write my own markdown extension to do this. Today is not that day.

## Jinja in Markdown?

If Pelican had a way to write Jinja2 macros in the markdown content, this would work for me even if it meant making the content somewhat less future-proof. However, this isn't possible. There is [an extension](https://github.com/pelican-plugins/jinja2content) that does this but it's not heavily maintained and has some caveats.

## The HTML way

This is what we're left with. Carving out our ideas into stone tablets with a hammer and chisel. These are all of the permutations that I use:

A regular image:

```html
<figure>
  <img src="{static}/images/article-name/image.png">
</figure>
```

An image with a title (tooltip):

```html
<figure>
  <img src="{static}/images/article-name/image.png" title="title for the image">
</figure>
```

An image as a link (usually a thumbnail to a full-size image):

```html
<figure>
  <a href="{static}/images/image.png">
    <img src="{static}/images/thumbnail.png">
  </a>
</figure>
```

An image with a caption:

```html
<figure>
  <img src="{static}/images/article-name/image.png">
  <figcaption>This is a caption.</figcaption>
</figure>
```

An image as a link with a caption:

```html
<figure>
  <a href="{static}/images/image.png">
    <img src="{static}/images/thumbnail.png">
  </a>
  <figcaption>This is a caption</figcaption>
</figure>
```
