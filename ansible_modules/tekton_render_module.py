#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
from jinja2 import Environment, FileSystemLoader, select_autoescape

def main():
    module = AnsibleModule(
        argument_spec=dict(
            tmpldir=dict(type='str', required=True),
            rndrdir=dict(type='str', required=True),
            urls=dict(type='list', required=True),
            vars=dict(type='list', required=True),
        )
    )

    tmpldir = module.params['tmpldir']
    rndrdir = module.params['rndrdir']
    urls = module.params['urls']
    vars = module.params['vars']

    # Get filenames from URLs
    tfnames = [url.split('/')[-1] for url in urls]

    # Get template variables
    jjv = dict(zip(vars[::2], vars[1::2]))

    # Initialize Jinja environment
    env = Environment(
        loader=FileSystemLoader(tmpldir),
        autoescape=select_autoescape(['html', 'xml']),
        lstrip_blocks=False,
        keep_trailing_newline=True
    )

    results = []

    # Render templates
    for tname in tfnames:
        tmpl = env.get_template(tname)
        tren = tmpl.render(jjv)
        rfname = rndrdir + '/' + tname

        # Write result to file
        with open(rfname, "w") as rfile:
            rfile.write(tren)

        results.append({
            'template_name': tname,
            'rendered_file': rfname,
        })

    module.exit_json(changed=True, results=results)

if __name__ == '__main__':
    main()
