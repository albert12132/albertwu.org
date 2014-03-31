introduction = """
<p>Hello world!</p>
"""

recent = [
    (
        'example-blog', 'Example article', '7/11/2014',
        """This is a description
        of an article here and there and everywhere."""
    ),
]

def make_recent(recent):
    def make_article_link(article):
        return """
        <div onclick='location.href="{0}"' class='link-block'>
          <h3>{1}</h3>

          <i>Published {2}</i>
          <p>{3}</p>
        </div>
        """.format(*article)
    return '\n'.join(map(make_article_link, recent))

recent = make_recent(recent)


attrs = globals()
