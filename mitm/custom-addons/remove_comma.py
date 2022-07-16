"""
Use mitmproxy's filter pattern in scripts.
"""
from mitmproxy import flowfilter
from mitmproxy import ctx, http
from bs4 import BeautifulSoup

dependencies = {
    '//cdn.jsdelivr.net/npm/@clappr/player@0.4.0/dist/clappr.min.js',
    '//cdn.jsdelivr.net/npm/cdnbye@latest/dist/hlsjs-p2p-engine.min.js',
    '//cdn.jsdelivr.net/npm/cdnbye@latest/dist/clappr-plugin.min.js',
    '//cdn.jsdelivr.net/gh/clappr/clappr-level-selector-plugin@latest/dist/level-selector.min.js'
}


class Filter:
    def __init__(self):
        pass    
        # self.filter: flowfilter.TFilter = None

    '''
    def configure(self, updated):
        if "flowfilter" in updated:
            self.filter = flowfilter.parse(ctx.options.flowfilter)

    def load(self, l):
        l.add_option("flowfilter", str, "", "Check that flow matches filter.")
    '''

    def filterScripts(self, tag):
        return (
            tag.name == 'script' and
            (tag['src'] not in dependencies if tag.has_attr('src') else True)
        )

    def response(self, flow: http.HTTPFlow) -> None:
        if flow.request.path.startswith('/streams/'):
            ctx.log.info("Flow matches filter:")
            ctx.log.info(flow)
            #ctx.log.info('Logging soup...')
            soup = BeautifulSoup(flow.response.content, features="html.parser")
            #ctx.log.info(soup.prettify())
            #ctx.log.info('Done logging soup.')
            tags = soup.findAll(self.filterScripts)
            for i, tag in enumerate(tags):
                if i == 0: # first tag is what we want
                    new_tag = soup.new_tag('script')
                    new_script = tag.string.replace('gethlsUrl(vidgstream, )', 'gethlsUrl(vidgstream)')
                    new_tag.string = new_script
                    tag.replace_with(new_tag)
                else:
                    tag.decompose()
            flow.response.text = str(soup)
            ctx.log.info('Set flow.response.text to this:')
            ctx.log.info(soup)

addons = [Filter()]
