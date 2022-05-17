# Architecture

1. seperate logic, data and configuration
Example folders:
- `source`  
    `crawler`
    - `config` *config reader*
    - `persistence` *store module*
    - `spider`
    - `proxy`
    - `header` *user agent generator*
    - `item_factory`
    - `logging`
    - `exception`

- `output` *your output files*
- `config` *your config files*
- `tests` *your tests*
- `install`
    - `install.md` *how to install via pip*
    - `requirements.yaml`

2. use a formatter (like flake8, autopep8)

3. missing pip install script file

4. Exceptions