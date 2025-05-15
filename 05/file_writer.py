#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r'''
---
module: my_test

short_description: Create a text file with specific content

version_added: "1.0.0"

description: This module creates a text file with the specified content at a given path.

options:
    path:
        description: The full path to the file to be created.
        required: true
        type: str
    content:
        description: The content to write into the file.
        required: true
        type: str

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_own_module:
    path: /tmp/hello.txt
    content: "Hello, world!"
'''

RETURN = r'''
path:
    description: Path to the file that was created or modified.
    type: str
    returned: always
    sample: "/tmp/hello.txt"
changed:
    description: Whether the file was created or modified.
    type: bool
    returned: always
'''

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        path='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    result['path'] = path

    # Check if the file exists and whether its content matches
    file_exists = os.path.exists(path)
    current_content = ''

    if file_exists:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                current_content = f.read()
        except Exception as e:
            module.fail_json(msg=f"Failed to read existing file: {e}", **result)

    # Check mode: simulate the change
    if module.check_mode:
        if not file_exists or current_content != content:
            result['changed'] = True
        module.exit_json(**result)

    # Write the file only if it doesn't exist or content is different
    if not file_exists or current_content != content:
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            result['changed'] = True
        except Exception as e:
            module.fail_json(msg=f"Failed to write file: {e}", **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
