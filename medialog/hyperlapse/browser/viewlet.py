from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize



class Hyperlapse(ViewletBase):
    """nothing here yet"""

    @property
    def construct_url(self):
        """returns the urls that will embed the map """
        
        return """http://s3.tripgeo.com/dirmap/map.htm?from=%(fromlocation)s&to=%(tolocation)s"""  % {
        'fromlocation' : self.context.fromlocation,
        'tolocation'   : self.context.tolocation,
        }