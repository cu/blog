# About

[This is my blog.](https://blog.bityard.net/)

# Development/Preview Environment

This repo uses [uv](https://docs.astral.sh/). If it is not installed, make it
so.

The `Makefile` is set up to run Pelican within a local virtualenv. It has
various interesting targets, some of which are listed below.

To run the Pelican development server on `localhost:8000`:

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

With the current stylesheet, images are generally a maximum of 640 pixels wide.

Easily the most annoying part of writing articles for this blog is handling the images. Oh, markdown has ways of inserting images into a document, but there are "issues." If you want to style article images in some way differently from the other images on the page, good luck because unless you write your own extension, the parser only outputs the barest of plain HTML, which makes writing CSS targeting these images difficult to impossible. (This is totally reasonable behavior on the part of the parser, but is highly inconvenient when using markdown for publishing.)

The markdown parser that Pelican uses (and probably most others) allows for an image to have a title, which most browsers render as a tool-tip when hovering over the image. If you want a caption above or below (which is more useful than a tool-tip), there is no markdown for that.

## The Markdown Way

For reference, this is the syntax for inserting an image:

```md
![Alt text]({static}/images/some-dir/some-file.jpg "Title text here")
```

And this is how you would use an image as a link (to another page or image):

```md
[![Alt text here]({static}/images/some-dir/thumbnail.jpg)]({static}/images/some-dir/full-size.jpg "Title text here")
```

## The HTML Way

This is what we're left with. Carving out our ideas into stone tablets with a hammer and chisel. These are all of the permutations that I use:

A regular boring image:

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

An image with alt text as a link with title text (for attribution):

```html
<figure>
  <a title="Title text here" href="{static}/images/image.png">
    <img alt="Alt text here" src="{static}/images/thumbnail.png">
  </a>
  <figcaption>This is a caption</figcaption>
</figure>
```

# Internal Links

```md
[Link text]({filename}/article-filename.md)
```
