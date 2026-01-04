from rest_framework.renderers import JSONRenderer
import json


class PrettyJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data is None:
            return b''
        
        charset = self.charset or 'utf-8'
        return json.dumps(
            data,
            ensure_ascii=self.ensure_ascii,
            allow_nan=not self.strict,
            indent=2,
            separators=(',', ': ')
        ).encode(charset)
