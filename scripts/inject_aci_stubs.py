import requests

if __name__ == '__main__':
    """
    Inject configurable ACI classes into core.pyi for type hints.
    """

    aci_url = '<>'
    output = requests.get(aci_url, verify=False).json()['classes']
    # TODO: Some stubs won't get generated for some reason, so add
    #  these manually:
    configurable_stubs = """
    @property
    def children(self) -> children_type: ...
    @property
    def status(self) -> Mo: ...
    @property
    def property_names(self) -> Mo: ...
    @property
    def non_empty_property_names(self) -> Mo: ...
    @property
    def is_configurable(self) -> bool: ...
    @property
    def is_configurable_property(self) -> bool: ...
    @property
    def json(self) -> dict: ...
    @property
    def xml(self) -> str: ...
"""
    for class_name, values in output.items():
        properties = ', '.join(f"{prop}: str = ''" for prop in values['properties'])
        if values['isConfigurable']:
            configurable_stubs += f"""
    def {class_name}(self, {properties}) -> Mo: ..."""

    new_file_content = """from collections import OrderedDict
odict_values = type(OrderedDict().values())
children_type = odict_values[Mo]  # Used for .children prop
"""
    with open('aioci/core.pyi') as r_pyi:
        # Read file
        for line in r_pyi:
            new_file_content += line
            if 'def up(self, level: int = ...) -> Mo: ...' in line:
                new_file_content += configurable_stubs
                new_file_content += '\n'
    with open('aioci/core.pyi', 'w') as w_pyi:
        w_pyi.write(new_file_content)
