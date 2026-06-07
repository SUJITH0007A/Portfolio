"""
Placeholder Python entrypoint to satisfy Vercel project configuration.
This file is a no-op and exists only so a configured `main.py` entrypoint
does not cause the build to fail. If you prefer a proper static deployment,
remove the Python entrypoint in your Vercel project settings and keep
`vercel.json` which forces `@vercel/static`.
"""

def handler(environ=None, start_response=None):
    # Minimal WSGI-compatible callable to avoid runtime errors if invoked.
    if start_response:
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'OK']
    return b'OK'

if __name__ == '__main__':
    print('Placeholder main.py present')
